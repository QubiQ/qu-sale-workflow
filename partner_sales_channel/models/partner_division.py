# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PartnerDivision(models.Model):
    _name = 'partner.division'

    name = fields.Char(
        string=_('Name'),
    )
    sales_channel_ids = fields.Many2many(
        comodel_name='crm.team',
        string=_('Sales Channels')
    )

    @api.constrains('name')
    def _check_name(self):
        if self.search_count([
            ('name', '=', self.name),
        ]) > 1:
            raise ValidationError(
                _('Division name must be unique!')
            )
