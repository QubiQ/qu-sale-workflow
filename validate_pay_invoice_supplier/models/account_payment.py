# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    @api.multi
    def post(self):
        for sel in self:
            for invoice in sel.invoice_ids.filtered(
               lambda r: not r.check_pay_supplier
               and r.type == 'in_invoice'):
                raise ValidationError(
                    _("Can not pay the supplier invoice"))
        return super(AccountPayment, self).post()
