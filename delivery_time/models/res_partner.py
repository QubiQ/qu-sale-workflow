# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    delivery_hour = fields.Float(
        string=_("Delivery Hour")
    )
