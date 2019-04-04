# Copyright 2019 Joan Segui <joan.segui@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sale Pricelist Line",
    "summary": "Pricelist line in sales",
    "version": "11.0.1.0.0",
    "category": "Sale",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'sale',
        'product',
    ],
    "data": [
        'views/pricelist_line_view.xml'
    ],
}
