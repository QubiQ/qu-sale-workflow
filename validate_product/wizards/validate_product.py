# Copyright 2018 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class ValidateProduct(models.TransientModel):
    _name = 'validate.product'

    @api.multi
    def validate_products(self):
        self.env['product.template'].browse(
            self._context.get('active_ids', [])).write(
                {
                    'active': True,
                    'validation': True,
                }
            )
