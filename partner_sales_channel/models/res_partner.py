# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    division_id = fields.Many2one(
        comodel_name='partner.division',
        string=_('Division'),
    )
