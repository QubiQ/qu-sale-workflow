# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class AccountPaymentMode(models.Model):
    _inherit = 'account.payment.mode'

    company = fields.Many2one(
        comodel_name='res.company',
        string=_('Company')
    )
