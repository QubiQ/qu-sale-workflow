# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    price_discount_total = fields.Float(
        string=_('Discount Total'),
        default=0.0,
    )
    price_discount_1 = fields.Float(
        string=_('Discount 1'),
        default=0.0,
    )
    price_discount_2 = fields.Float(
        string=_('Discount 2'),
        default=0.0,
    )
    price_discount_3 = fields.Float(
        string=_('Discount 3'),
        default=0.0,
    )

    @api.one
    @api.depends('categ_id', 'product_tmpl_id', 'product_id', 'compute_price',
                 'fixed_price', 'pricelist_id', 'percent_price',
                 'price_discount', 'price_surcharge')
    def _get_pricelist_item_name_price(self):
        super(PricelistItem, self)._get_pricelist_item_name_price()

        if self.compute_price != 'fixed' and\
                self.compute_price == 'percentage':
            self.price_discount_total = 100.0

            if self.price_discount_1 != 0.0:
                self.price_discount_total = self.price_discount_total * (
                                            1.0-(self.price_discount_1/100.0))
            if self.price_discount_2 != 0.0:
                self.price_discount_total = self.price_discount_total * (
                                            1.0-(self.price_discount_2/100.0))
            if self.price_discount_3 != 0.0:
                self.price_discount_total = self.price_discount_total * (
                                            1.0-(self.price_discount_3/100.0))
            self.price = _("%s %% discount") %\
                (round((100.0 - self.price_discount_total), 2))
            self.percent_price = round((100.0 - self.price_discount_total), 2)

    @api.onchange('price_discount_1', 'price_discount_2', 'price_discount_3')
    def onchange_discounts(self):
        if self.compute_price != 'fixed'\
         and self.compute_price == 'percentage':
            self.price_discount_total = 100.0
            if self.price_discount_1 != 0.0:
                self.price_discount_total = self.price_discount_total * (
                                            1.0-(self.price_discount_1/100.0))
            if self.price_discount_2 != 0.0:
                self.price_discount_total = self.price_discount_total * (
                                            1.0-(self.price_discount_2/100.0))
            if self.price_discount_3 != 0.0:
                self.price_discount_total = self.price_discount_total * (
                                            1.0-(self.price_discount_3/100.0))
        self.percent_price = (round((100.0 - self.price_discount_total), 2))
