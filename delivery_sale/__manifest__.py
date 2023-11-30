{
    'name': "Venta por delivery",
    'version': "1.0",
    'author': "Anthony Loayza",
    'category': "venta",
    'website': "https://escuelafullstack.com/",
    'description': """Modulo para venta por delivery""",
    'depends': [
        'mail',
        'account'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/customers_view.xml',
        'views/product_view.xml',
        'views/order_view.xml',
        'views/menu.xml',
    ],
    'installable': True
}