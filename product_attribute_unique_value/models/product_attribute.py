# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    unique_value = fields.Boolean(
        string=_('Unique Value'),
        help=_('Check to allow just one value for this attribute'),
        default=False
    )
