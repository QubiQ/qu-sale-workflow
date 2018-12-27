# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Sales Channel",
    "summary": "Default Sales Channel on partners",
    "version": "11.0.1.0.0",
    "category": "Account",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "sale",
        "account",
        "sales_team"
    ],
    "data": [
        "data/partner_division.xml",
        "views/res_partner.xml",
        "views/partner_division.xml",
        "views/sale_order.xml",
        "views/account_invoice.xml",
        "views/crm_team.xml"
    ],
}
