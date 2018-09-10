# (c) 2018 QubiQ
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    promotion_id = fields.Many2one(
        string='Promotion',
    )
