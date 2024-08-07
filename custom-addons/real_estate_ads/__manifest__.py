{
    "name": "Real Estate Ads",
    "version": "1.0",
    "author": "Afriza Gilleon",
    "maintainer": "Afriza Gilleon",

    "description" : """
        Real Estate module to show available properties
    """,
    "category" : "Sales",
    "depends" : ["base", "mail", "website"],
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
        'views/property_web_template.xml',

        # data
        'data/estate.property.type.csv',

        #demo
        'demo/estate.property.tags.csv',
        
        # report
        'report/property_report.xml',
        'report/report_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'real_estate_ads/static/src/js/custom_tag.js',
            'real_estate_ads/static/src/xml/custom_tag.xml',
        ]
    },
    "installable": True,
    "application": True,
    "license": "AGPL-3",
}