# Copyright 2018 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    validate_partners = fields.Boolean(
        default=False,
        string=_('Validate partners')
    )
