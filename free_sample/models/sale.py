# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2018 QubiQ (http://www.qubiq.es)

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_sample = fields.Boolean(
        string='Free Sample',
        default=False
    )

    @api.multi
    @api.onchange('is_sample')
    def onchange_is_sample(self):
        for line in self:
            if line.is_sample:
                line.discount = 100.0
            else:
                line.discount = 0.0
