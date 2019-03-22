# Copyright 2019 Valentin Vinagre <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    warranty_percentage = fields.Float(
        string=_('Warranty Percentage'),
        default=0.0
    )

    @api.multi
    def create_invoices(self):
        sale_orders = self.env['sale.order'].browse(
            self._context.get('active_ids', []))
        if self.warranty_percentage < 0.0:
            raise UserError(
                _("The value of warranty must be positive."))
        if self.advance_payment_method == 'delivered':
            res = super(SaleAdvancePaymentInv, self).create_invoices()
        # Se arreglan todas las facturas y lineas de las sale.orders
        if self.advance_payment_method == 'all':
            if self.warranty_percentage > 0.0:
                for order in sale_orders:
                    warr_inv = order.invoice_ids.filtered(
                        lambda x: x.warranty_check and x.state == 'draft')
                    inv_total =\
                        sum(x.amount_untaxed for x in order.invoice_ids)
                    total = order.amount_untaxed - inv_total
                    total = total*(self.warranty_percentage/100.0)
                    # caso 1 no existe factura de garantia
                    if not warr_inv:
                        self.with_context(active_ids=[order.id]).create({
                            'advance_payment_method': 'fixed',
                            'amount': total,
                        }).create_invoices()
                        order.invoice_ids[-1].write({
                            'warranty_check': True,
                        })
                        if not order.company_id.warranty_account_income_id:
                            raise UserError(
                                _("Need configured the warranty account in the company."))
                        order.invoice_ids[-1].invoice_line_ids[-1].write({
                            'name': 'Garantía',
                            'account_id': order.company_id.warranty_account_income_id.id,
                        })
                        order.invoice_ids[-1].invoice_line_ids[-1].\
                            sale_line_ids[-1].write({
                                'name': 'Garantía',
                            })
                    # caso 2 existe factura de garantia
                    if warr_inv:
                        # Se calcula el importe total de la factura y se
                        # actualiza la warranty pertinente.
                        wil = warr_inv.invoice_line_ids.filtered(
                            lambda x: x.sale_line_ids)
                        wil.write({
                            'price_unit': wil.price_unit + total,
                        })
                        wil.sale_line_ids[0].write({
                            'price_unit': wil.sale_line_ids[0].price_unit +
                            total,
                        })
                        warr_inv.compute_taxes()
            # crea la factura normal....
            res = super(SaleAdvancePaymentInv, self).create_invoices()
        else:
            for order in sale_orders:
                total = self.amount
                warranty = False
                if self.advance_payment_method == 'percentage':
                    total = (self.warranty_percentage/100.0*self.amount/100.0)*100.0
                    self.amount = ((self.amount/100.0)-((self.amount/100.0) *
                                   (self.warranty_percentage/100.0)))*100.0
                    warranty = True
                else:
                    total = self.amount
                    self.amount -= self.amount*(self.warranty_percentage/100.0)
                    total -= self.amount
                    warranty = True
                res = super(SaleAdvancePaymentInv, self.with_context(
                    active_ids=[order.id])).create_invoices()
                warr_inv = order.invoice_ids.filtered(
                    lambda x: x.warranty_check and x.state == 'draft')
                # existe alguna factura de garantia actualiza el precio nuevo
                if warranty and warr_inv:
                    # se anyade el importe de garantia a la linea de factura y
                    # a la de la venta....
                    wil = warr_inv.invoice_line_ids.filtered(
                            lambda x: x.sale_line_ids)
                    wil.write({
                        'price_unit': wil.price_unit + total,
                    })
                    warr_inv.compute_taxes()
                    wil.sale_line_ids[0].write({
                        'price_unit': wil.sale_line_ids[0].price_unit + total,
                    })
                # si no existe ninguna factura de garantia la genera
                elif warranty and not warr_inv:
                    self.amount = total
                    res = super(SaleAdvancePaymentInv, self).create_invoices()
                    order.invoice_ids[-1].write({
                        'warranty_check': True,
                    })
                    if not order.company_id.warranty_account_income_id:
                        raise UserError(
                            _("Need configured the warranty account in the company."))
                    order.invoice_ids[-1].invoice_line_ids[-1].write({
                        'name': 'Garantía',
                        'account_id': order.company_id.warranty_account_income_id.id,
                    })
                    order.invoice_ids[-1].invoice_line_ids[-1].\
                        sale_line_ids[-1].write({
                            'name': 'Garantía',
                        })
        return res
