# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Compute Product Margin",
    "summary": "Compute a product margin depending on a profit percent",
    "version": "10.0.1.0.0",
    "category": "Sales",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product",
        "sale"
    ],
    "data": [
        "views/product_template.xml",
        "views/product_category.xml",
        "wizard/compute_product_margin.xml"
    ],
}
