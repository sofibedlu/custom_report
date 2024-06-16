{
    'name': 'Sales Report',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Adds a report for sales order',
    'author': 'sofi',
    'website': 'https://erp.sofii.me',
    'depends': ['sale', 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_report.xml',
        'views/sales_report_wizard.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    'assets': {
        'web.report_assets_common': [
            'custom_sales_report/static/src/css/custom_styles.css',
        ],
    },
}