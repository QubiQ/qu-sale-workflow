# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    division_id = fields.Many2one(
        comodel_name='partner.division',
        string=_('Division'),
    )

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        division = False
        if self.partner_id.division_id:
            division = self.partner_id.division_id
        self.division_id = division
        return super(SaleOrder, self).onchange_partner_id()

    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            'division_id': self.division_id.id
        })
        return res
