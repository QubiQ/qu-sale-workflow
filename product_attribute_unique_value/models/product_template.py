# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.constrains('attribute_line_ids')
    def check_attribute_unique_value(self):
        for line in self.attribute_line_ids:
            if line.attribute_id.unique_value and\
                    len(line.value_ids) > 1:
                raise UserError(_(
                    'You cannot add more than one value for the attribute ' +
                    line.attribute_id.name + '!'
                ))
