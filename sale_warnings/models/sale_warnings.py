# -*- coding: utf-8 -*-
# Copyright 2019 Jesus Ramoneda <jesus.ramonedae@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp.osv import osv
from openerp.exceptions import Warning
from openerp.tools.translate import _


class SaleOrderPaymentsWarnings(osv.osv):
    _inherit = 'sale.advance.payment.inv'

    def create_invoices(self, cr, uid, ids, context=None):
        sale_order = self.pool.get('sale.order').browse(cr, uid, context.get(
            'active_ids', False))[0]
        partner = sale_order.partner_id
        # Si tiene alguna alerta
        if partner.invoice_warn != 'no-message':
            # Bloqueamos el flujo
            if partner.invoice_warn == 'block':
                raise Warning(
                    _(' Block Warning for %s') % partner.name,
                    partner.invoice_warn_msg
                )
            # Mostramos el popup de alerta
            if not context.get('is_warned', False):
                title = _('Warning for %s') % partner.name
                message = partner.invoice_warn_msg

                # Devolvemos mostramos el popup
                action_id = self.pool.get('ir.actions.act_window').search_read(
                    cr, uid, [('res_model', '=', 'sale.make.invoice')], ['id']
                )[0]
                return self.pool.get('warning.wizard').get_view(
                    cr, uid, ids, title=title, message=message,
                    action_id=action_id['id'], target='new', ctx=context
                )
        return super(SaleOrderPaymentsWarnings, self).create_invoices(
                cr, uid, ids, context
        )


class SaleMakeINvoiceWarnings(osv.osv):
    _inherit = 'sale.make.invoice'

    def make_invoices(self, cr, uid, ids, context=None):
        sale_orders = self.pool.get('sale.order').browse(
            cr, uid, context.get('active_ids', False)
        )
        block = False
        message = ""
        for sale_order in sale_orders:
            parner = sale_order.partner_id
            if parner.invoice_warn != 'no-message':
                # Comprovamos si es un mensaje de bloqueo
                if parner.invoice_warn == 'block' and not block:
                    block = True
                    message += _('[Blocked] ')
                message += _("Warning for the sale order {0} from the customer"
                             + "{1} :\n").format(sale_order.name, parner.name)
                message += parner.invoice_warn_msg + '\n --- \n'
        # Si alguien tiene un mensaje lo mostramos
        if len(message) > 0:
            if block:
                raise Warning(message)
            # Si no es bloqueante obtenemos la id_action a devolver y
            # mostramos el pop up
            elif not context.get('is_warned', False):
                action_id = self.pool.get('ir.actions.act_window').search_read(
                    cr, uid, [('res_model', '=', 'sale.make.invoice')], ['id']
                )[0]
                return self.pool.get('warning.wizard').get_view(
                    cr, uid, ids, title=_('Warning'), message=message,
                    action_id=action_id['id'], target='new', ctx=context
                )
        return super(SaleMakeINvoiceWarnings, self).make_invoices(
            cr, uid, ids, context
        )
