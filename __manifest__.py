{
    'name':'Vehicle Rental',
    'description':'List vehicles on our platform and rent it.',
    'version':'1.1',
    'depends':['base'],
    'data' : [
        'security/ir.model.access.csv',

        'views/owner_views.xml',
        'views/vehicle_views.xml',
        'views/vehicle_rental_menus.xml'
    ],
    'installation':True,
    'application':True
}