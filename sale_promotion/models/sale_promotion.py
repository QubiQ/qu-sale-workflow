# (c) 2018 QubiQ
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class SalePromotion(models.Model):
    _name = 'sale.promotion'
    _description = 'Promotion models'

    name = fields.Char(string='Name of promotion')

    date_from = fields.Datetime(string='Starting Date', required=True)
    date_to = fields.Datetime(string='Ending Date')
    partners = fields.Many2many('res.partner', string='Partners')
    products = fields.Many2many('product.product', string="Products")
    is_free_product = fields.Boolean(string='Is free product', default=False)
    promo_type = fields.Selection([
        ('free_product', 'Product free'),
        ('quantity_x_quantity', 'Quantity x Quantity')
        ], string='Promotion type')
    product_qty = fields.Integer(
        string="Quantity of products")
    product_free = fields.Many2one(
        'product.product',
        string="Free Product")
    product_free_qty = fields.Integer(
        string="Quantity of free products")

    @api.onchange('promo_type')
    def _onchange_promo_type(self):
        for sel in self:
            if sel.promo_type == 'free_product':
                sel.is_free_product = True
            elif sel.promo_type == 'quantity_x_quantity':
                sel.product_qty = 3
                sel.product_free_qty = 1
                sel.is_free_product = False
