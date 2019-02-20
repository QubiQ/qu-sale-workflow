# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from odoo.exceptions import UserError


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    @api.model
    def create(self, vals):
        res = super(ProductAttributeValue, self).create(vals)
        attribute_id = self.env['product.attribute'].browse(
            res.attribute_id.id
        )
        if not attribute_id.no_create or (
            self._context.get('params') and
            self._context.get('params').get('action') and
            self.env['ir.actions.act_window'].browse(
                self._context['params']['action']
            ).res_model == 'product.attribute.value'
        ):
            return res
        else:
            raise UserError(_(
                'You cannot create new values for this attribute from the '
                'product template'
            ))
