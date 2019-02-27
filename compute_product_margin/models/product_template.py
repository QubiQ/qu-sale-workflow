# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    base_price = fields.Float(
        string=_('Base Price'),
        default=0.0,
        digits=dp.get_precision('Product Price'),
    )
    profit_percent = fields.Float(
        string=_('Profit Percent'),
        default=0.0,
    )

    @api.multi
    def compute_product_margin(self):
        for sel in self:
            if sel.base_price == 0.0:
                raise UserError(_('Set a Base Price!'))
            elif sel.profit_percent == 0.0 and\
                    sel.categ_id.profit_percent == 0.0:
                raise UserError(_('Set a Profit Percent!'))
            else:
                profit_percent = sel.categ_id.profit_percent
                if sel.profit_percent != 0.0:
                    profit_percent = sel.profit_percent
                sel.list_price = sel.base_price * (1 + profit_percent / 100)
