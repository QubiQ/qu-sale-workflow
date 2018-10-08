# Copyright 2018 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Validate Product",
    "version": "10.0.1.0.0",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "website": "https://www.qubiq.es",
    "category": "Sale",
    "license": "AGPL-3",
    "depends": [
        "base",
        "product",
        "sale",
    ],
    "data": [
        'data/groups.xml',
        'views/product.xml',
        'wizards/validate_product.xml',
        'views/res_company.xml'
    ],
    'installable': True,
    'application': False,
}
