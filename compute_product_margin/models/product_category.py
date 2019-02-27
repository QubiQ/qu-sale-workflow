# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class ProductCategory(models.Model):
    _inherit = 'product.category'

    product_ids = fields.One2many(
        comodel_name='product.template',
        inverse_name='categ_id',
        string=_('Products'),
    )
    profit_percent = fields.Float(
        string=_('Profit Percent'),
        default=0.0,
    )

    @api.multi
    def compute_product_margin(self):
        for sel in self:
            for product in sel.product_ids:
                profit_percent = sel.profit_percent
                if product.profit_percent != 0.0:
                    profit_percent = product.profit_percent
                if product.base_price != 0.0 and profit_percent != 0.0:
                    product.list_price =\
                        product.base_price * (1 + profit_percent / 100)
