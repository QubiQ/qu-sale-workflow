# Copyright 2018 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Pricelist Triple Discount',
    'version': '10.0.1.0.0',
    'category': 'Sales Management',
    'author': 'QubiQ',
    'website': 'https://qubiq.es',
    'license': 'AGPL-3',
    'summary': 'Manage triple discounts on pricelists.',
    'depends': [
        'sale',
        'product',
        'account_invoice_triple_discount',
        'sale_triple_discount',
    ],
    'data': [
        'views/sale_order_view.xml',
        'views/product_pricelist_views.xml',
    ],
    'installable': True,
    'Application': False,
}
