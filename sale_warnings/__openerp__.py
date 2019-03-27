# -*- coding: utf-8 -*-
# Copyright 2019 Jesus Ramoneda <jesus.ramonedae@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sale Warnings",
    "summary": "Allow sale invoices warnings when the invoice is created from the sale order.",
    "version": "8.0.1.0.0",
    "category": "Sales",
    "website": "https:/www.qubiq.es",
    "author": "Qubiq",
    "license": "AGPL-3",
    "depends": [
        "sale"
    ],
    "data": [
        "wizard/warning_wizard.xml",
    ],
    "application": False,
    "installable": True,
}
