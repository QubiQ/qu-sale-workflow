# Copyright 2019 Valentin Vinagre <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Warranty Sales Invoice",
    "summary": "Allows to generate sales order guarantee invoices.",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "sale",
        "account",
    ],
    "data": [
        'views/account_invoice.xml',
        'views/res_company.xml',
        'wizards/sale_advance_payment_inv.xml',
    ],
}
