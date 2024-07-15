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
        # groups
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'security/model_access.xml',
        'security/ir_rule.xml',

        #views
        'views/property.xml',
        'views/property_type.xml',
        'views/property_tags.xml',
        'views/property_offer.xml',
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