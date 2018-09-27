# (c) 2018 QubiQ
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Sale Promotion',
    'version': '11.0.1.0.0',
    'author': 'QubiQ',
    'category': 'Custom / Sales',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'sale',
        'account',
        'product',
        'sale_commission',
    ],
    'data': [
        'data/free_product.xml',
        'security/security.xml',
        'views/sale_order.xml',
        'views/sale_promotion.xml',
    ],
    'installable': True,
}
