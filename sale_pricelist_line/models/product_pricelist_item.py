# Copyright 2019 Joan Segui <joan.segui@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    name = fields.Char(
        store=True
    )
