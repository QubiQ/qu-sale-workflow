# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, _


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    division_ids = fields.Many2many(
        comodel_name='partner.division',
        string=_('Divisions')
    )
