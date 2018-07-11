# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    validation_bool = fields.Boolean(
        default=False,
        string=_('Invoices and Sale Orders Validation')
    )
    validation_amount = fields.Float(
        string=_('Amount Untaxed'),
        default=0.0
    )
    validation_payment_mode = fields.Many2many(
        comodel_name='account.payment.mode',
        inverse_name='company',
        string=_('Payment mode')
    )
