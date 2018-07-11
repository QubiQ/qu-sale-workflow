# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains('amount_untaxed', 'payment_mode_id')
    def amount_validation(self):
        if self.company_id.validation_bool and\
            self.amount_untaxed >= self.company_id.validation_amount and (
                self.payment_mode_id.id in self.company_id.validation_payment_mode.ids or not\
                self.company_id.validation_payment_mode
                    ):
                        raise UserError(
                            _("The order exceeds the allowed amount for that payment mode!")
                        )
