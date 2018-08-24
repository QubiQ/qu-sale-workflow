# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Delivery Time",
    "summary": "Set a delivery time for every partner",
    "version": "11.0.1.0.0",
    "category": "Delivery",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "depends": [
        "base",
        "sale",
        "stock"
    ],
    "data": [
        "views/res_partner.xml",
        "views/sale_order.xml",
        "views/stock_picking.xml",
        "reports/sale_order.xml",
        "reports/stock_picking.xml"
    ],
    "application": False,
    "installable": True,
}
