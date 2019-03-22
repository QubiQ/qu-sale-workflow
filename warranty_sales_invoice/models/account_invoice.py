# Copyright 2019 Valentin Vinagre <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    warranty_check = fields.Boolean(
        string=_('Warranty Invoice'),
        readonly=True,
        default=False
    )
