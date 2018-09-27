# Copyright 2018 Oscar Navarro <oscar.navarro@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Tax Name in Report",
    "summary": "Tax Name in Report",
    "version": "11.0.1.0.0",
    "category": "Custom",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "sale",
    ],
    "data": [
        "reports/report_templates.xml",
    ],
}
