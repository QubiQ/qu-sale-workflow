# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # Executed when view changed.
    @api.depends('discount1', 'discount2', 'discount3')
    def _compute_amount(self):
        for line in self:
            prev_price_unit = line.price_unit
            prev_discount = line.discount
            price_unit =\
                prev_price_unit * (1.0 - (prev_discount or 0.0) / 100.0)
            line.update({
                'price_unit': price_unit,
                'discount': 0.0,
            })
            super(SaleOrderLine, line)._compute_amount()
            price =\
                prev_price_unit * (1.0 - (prev_discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(
                price,
                line.order_id.currency_id,
                line.product_uom_qty,
                product=line.product_id,
                partner=line.order_id.partner_shipping_id
            )
            line.update({
                'price_unit': prev_price_unit,
                'discount': prev_discount,
                'price_tax': sum(
                    t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })

    discount1 = fields.Float(
        string=_('Disc. 1 (%)'),
        digits=dp.get_precision('Discount'),
        default=0.0,
    )

    base_discount = fields.Float(
        string=_('Base Discount'),
        digits=dp.get_precision('Discount'),
        default=0.0,
    )

    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        res.update({
            'discount': self.discount,
            'discount1': self.discount1,
        })
        return res

    # Executed when store.
    @api.onchange('discount1', 'discount2', 'discount3')
    def _get_price_reduce(self):
        for line in self:
            temp_discount = 100.0
            prev_price = line.price_unit
            super(SaleOrderLine, line)._get_price_reduce()

            if line.order_id.pricelist_id.discount_policy == 'with_discount':
                temp_discount = (temp_discount *
                                 (1.0-(line.base_discount/100.0))
                                 )
            if line.discount1 != 0.0:
                temp_discount = (temp_discount *
                                 (1.0-(line.discount1/100.0))
                                 )
            if line.discount2 != 0.0:
                temp_discount = (temp_discount *
                                 (1.0-(line.discount2/100.0))
                                 )
            if line.discount3 != 0.0:
                temp_discount = (temp_discount *
                                 (1.0-(line.discount3/100.0))
                                 )
            line.discount = round((100.0 - temp_discount), 2)
            line.price_reduce = prev_price * line.discount

    @api.onchange('product_id', 'price_unit', 'product_uom',
                  'product_uom_qty', 'tax_id')
    def _onchange_discount(self):
        super(SaleOrderLine, self)._onchange_discount()

        if not (self.product_id and self.product_uom and
                self.order_id.partner_id and self.order_id.pricelist_id and
                self.order_id.pricelist_id.discount_policy ==
                'without_discount' and
                self.env.user.has_group('sale.group_discount_per_so_line')):
            return
        context_partner = dict(
            self.env.context,
            partner_id=self.order_id.partner_id.id,
            date=self.order_id.date_order
        )
        pricelist_context = dict(
            context_partner,
            uom=self.product_uom.id
        )
        price, rule_id = self.order_id.pricelist_id\
            .with_context(pricelist_context).get_product_price_rule(
                self.product_id,
                self.product_uom_qty or 1.0,
                self.order_id.partner_id
            )

        new_rule = self.env['product.pricelist.item']\
            .search([('id', '=', rule_id)])
        vals = {
            'discount': new_rule.percent_price,
            'base_discount': new_rule.percent_price,
        }
        if new_rule.pricelist_id.discount_policy == "without_discount":
            vals['discount1'] = new_rule.price_discount_1
            vals['discount2'] = new_rule.price_discount_2
            vals['discount3'] = new_rule.price_discount_3
        self.write(vals)
