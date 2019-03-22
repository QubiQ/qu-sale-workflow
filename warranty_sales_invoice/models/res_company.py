# Copyright 2019 Valentin Vinagre <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class ResCompany(models.Model):
    _inherit = "res.company"

    warranty_account_income_id = fields.Many2one(
        'account.account',
        string=_("Income Warranty Account"),
        domain=[('deprecated', '=', False)],
        help=_("Default account for the product warranty.")
    )
