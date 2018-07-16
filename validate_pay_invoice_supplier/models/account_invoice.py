# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    check_pay_supplier = fields.Boolean(
        string=_('Accept Pay'),
        default=False,
        copy=False
    )
