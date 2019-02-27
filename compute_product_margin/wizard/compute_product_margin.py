# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class ComputeProductMargin(models.TransientModel):
    _name = 'compute.product.margin'

    category_ids = fields.Many2many(
        comodel_name='product.category',
        string=_('Categories')
    )

    @api.multi
    def compute_product_margin(self):
        for sel in self:
            category_ids =\
                sel.category_ids or self.env['product.category'].search([])
            for category in category_ids:
                category.compute_product_margin()
