# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, api, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    division_id = fields.Many2one(
        comodel_name='partner.division',
        string=_('Division'),
    )

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        division = False
        if self.type in ['out_invoice', 'out_refund'] and\
                self.partner_id.division_id:
            division = self.partner_id.division_id
        self.division_id = division
        return super(AccountInvoice, self)._onchange_partner_id()
