# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Product Attribute Unique Value",
    "summary": "Limit the product attribute values to one",
    "version": "10.0.1.0.0",
    "category": "Product",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product"
    ],
    "data": [
        "views/product_attribute.xml"
    ],
}
