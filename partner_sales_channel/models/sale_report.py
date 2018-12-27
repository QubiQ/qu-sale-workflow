# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, _


class SaleReport(models.Model):
    _inherit = 'sale.report'

    division_id = fields.Many2one(
        comodel_name='partner.division',
        string=_('Division'),
        readonly=True
    )

    def _select(self):
        position = 's.team_id as team_id,'
        select_str = super(SaleReport, self)._select()
        return select_str[:select_str.find(position) + len(position)] +\
            's.division_id as division_id,' +\
            select_str[select_str.find(position) + len(position):]

    def _group_by(self):
        position = 's.team_id,'
        group_by_str = super(SaleReport, self)._group_by()
        return group_by_str[:group_by_str.find(position) + len(position)] +\
            's.division_id,' +\
            group_by_str[group_by_str.find(position) + len(position):]
