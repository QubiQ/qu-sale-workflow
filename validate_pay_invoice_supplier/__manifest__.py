# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Validate Pay Invoice Supplier",
    "version": "10.0.1.0.0",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "website": "https://www.qubiq.es",
    "category": "Account",
    "license": "AGPL-3",
    "depends": [
        "base",
        "account",
    ],
    "data": [
        'security/groups.xml',
        'views/account_invoice.xml',
    ],
    'installable': True,
    'application': False,
}
