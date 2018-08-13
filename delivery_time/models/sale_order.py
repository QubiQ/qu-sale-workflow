# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_hour = fields.Float(
        string=_("Delivery Hour")
    )

    @api.multi
    @api.onchange('partner_id')
    def _get_delivery_hour(self):
        for sel in self:
            if sel.partner_id.delivery_hour:
                sel.delivery_hour = sel.partner_id.delivery_hour

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for sel in self:
            sel.picking_ids.write({'delivery_hour': sel.delivery_hour})
        return res
