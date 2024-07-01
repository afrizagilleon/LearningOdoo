{
    "name": "Real Estate Ads",
    "version": "1.0",
    "author": "Afriza Gilleon",
    "maintainer": "Afriza Gilleon",

    "description" : """
        Real Estate module to show available properties
    """,
    "category" : "Sales",
    "depends" : ["base"],
    "data" : [
        'security/ir.model.access.csv',
        'views/property.xml',
        'views/property_type.xml',
        'views/property_tags.xml',
        'views/menu_items.xml',

        # data
        'data/estate.property.type.csv',

        #demo
        'demo/estate.property.tags.csv'
    ],
    "installable": True,
    "application": True,
    "license": "AGPL-3",
}