# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    no_create = fields.Boolean(
        string=_('No Create'),
        help=_(
            'Check to avoid creating new values for this attribute from the '
            'product template'
        ),
        default=False
    )
