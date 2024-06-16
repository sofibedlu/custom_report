from odoo import models, fields, api

class SalesReportWizard(models.TransientModel):
    _name = 'sales.report.wizard'
    _description = 'Sales Report Wizard'

    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    product_id = fields.Many2one('product.product', string='Product')
    partner_id = fields.Many2one('res.partner', string='Customer')
    report_type = fields.Selection([
        ('pdf', 'PDF'),
        ('xlsx', 'Excel'),
    ], string='Report Type', default='pdf')

    def print_report(self):
        self.ensure_one()
        data = {
            'date_from': self.date_from,
            'date_to': self.date_to,
            'product_id': self.product_id.id,
            'partner_id': self.partner_id.id,
            'report_type': self.report_type,
        }
        if self.report_type == 'pdf':
            return self.env.ref('custom_sales_report.sales_report').report_action(self, data=data)
        else:
            return self.env.ref('custom_sales_report.report_sales_details_xlsx').report_action(self, data=data)
