# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    @api.constrains('amount_untaxed', 'payment_mode_id')
    def amount_validation(self):
        for sel in self:
            if sel.type == 'out_invoice' and\
                sel.company_id.validation_bool and\
                    sel.amount_untaxed >= sel.company_id.validation_amount and\
                    (
                        sel.payment_mode_id.id in sel.company_id.validation_payment_mode.ids or not
                        sel.company_id.validation_payment_mode
                    ):
                raise UserError(
                    _("The invoice exceeds the allowed amount for that payment mode!")
                )
