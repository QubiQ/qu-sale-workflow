# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, _


class PosSaleReport(models.Model):
    _inherit = 'report.all.channels.sales'

    division_id = fields.Many2one(
        comodel_name='partner.division',
        string=_('Division'),
        readonly=True
    )

    def _so(self):
        position = 'so.team_id AS team_id'
        so_str = super(PosSaleReport, self)._so()
        return so_str[:so_str.find(position) + len(position)] +\
            ',so.division_id AS division_id' +\
            so_str[so_str.find(position) + len(position):]

    def get_main_request(self):
        position = 'team_id,'
        request = super(PosSaleReport, self).get_main_request()
        return request[:request.find(position) + len(position)] +\
            'division_id,' +\
            request[request.find(position) + len(position):]
