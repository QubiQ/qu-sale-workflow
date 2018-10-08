# Copyright 2018 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    validated = fields.Boolean(
        string=_('Validated')
    )
    validation = fields.Boolean(
        related='company_id.validate_products',
        store=True,
        readonly=True,
        string=_('Validation')
    )

    """
    Inheritance to set the active value depending on the default selected
    company
    """
    @api.model
    def create(self, vals):
        res = super(ProductTemplate, self).create(vals)
        validation = self.env['res.company'].search([
            ('id', '=', vals['company_id'])
        ]).validate_products
        res.update(
            {'active': not validation}
        )
        return res

    """
    Inheritance to change the validated value when the active value is changed
    """
    @api.multi
    def write(self, vals):
        if 'active' in vals and 'validated' not in vals:
            if vals.get('active'):
                vals['validated'] = True
            else:
                vals['validated'] = False
        return super(ProductTemplate, self).write(vals)

    """
    Changes the active value when the company is changed and changes the
    validated value depending on the active value
    """
    @api.onchange('active', 'company_id')
    @api.multi
    def onchange_active_company(self):
        for sel in self:
            sel.active = not sel.validation
            if sel.active:
                sel.validated = True
            else:
                sel.validated = False

    """
    Validates products massively through a server action
    """
    @api.multi
    def validate_products(self):
        self.env['product.template'].browse(
            self._context.get('active_ids', [])).write(
                {
                    'active': True,
                    'validated': True,
                }
            )
