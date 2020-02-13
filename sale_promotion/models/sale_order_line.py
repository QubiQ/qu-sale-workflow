# (c) 2018 QubiQ
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    is_free = fields.Boolean(string="Is free", default=False)