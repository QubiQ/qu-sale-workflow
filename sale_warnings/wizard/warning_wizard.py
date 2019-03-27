# -*- coding: utf-8 -*-
# Copyright 2019 Jesus Ramoneda <jesus.ramonedae@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _


class WarningWizard(models.TransientModel):
    _name = 'warning.wizard'
    _description = 'custom wizard for warning the customer'

    name = fields.Char(
        string=_('Name'),
        readonly=True,
        default=_('Warning')
    )
    title = fields.Char(
        string=_('Title'),
        readonly=True
    )
    message = fields.Text(
        string=_('Message'),
        readonly=True
    )
    action_id = fields.Integer(
        string=_('Action ID')
        )

    # Esta funcion devuelve la vista con los parametros pasados
    @api.multi
    def get_view(
        self, title=_('Warning'), message="", action_id=False, target='new',
        ctx=False
    ):
        # Creamos un wizard para mantener el contexto del formulario inicial
        wizard = self.env['warning.wizard'].create({
            'message': message,
            'title': title,
            'ctx': ctx,
            'action_id': action_id
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'warning.wizard',
            'res_id': wizard.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': target,
            'context': ctx
        }

    @api.multi
    def confirm(self):
        try:
            action = self.env['ir.actions.act_window'].search_read(
                [('id', '=', self.action_id)]
            )[0]
        except ValueError:
            return None
        return {
            'type': action['type'],
            'res_model': action['res_model'],
            'view_type': action['view_type'],
            'view_mode': action['view_mode'],
            'name': action['name'],
            'target': action['target'],
            'context': self._context
        }
