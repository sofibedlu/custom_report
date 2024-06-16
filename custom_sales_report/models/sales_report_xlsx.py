from odoo import models
from odoo.addons.report_xlsx.report.report_abstract_xlsx import ReportXlsxAbstract #You need to use report_xlsx module version which is the same as your odoo version 

class SalesReportXlsx(ReportXlsxAbstract, models.AbstractModel):
    _name = 'report.custom_sales_report.report_sales_details_xlsx'
    _description = 'Sales Report Excel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objects):
        sheet = workbook.add_worksheet('Sales Report')

        # Define some formats
        header_format = workbook.add_format({
            'bold': True, 
            'font_color': 'white', 
            'bg_color': 'blue',
            'border': 1,
            'align': 'center', 
            'valign': 'vcenter'
        })
        
        cell_format = workbook.add_format({
            'border': 1,
            'align': 'left', 
            'valign': 'vcenter'
        })
        
        money_format = workbook.add_format({
            'num_format': '$#,##0.00',
            'border': 1,
            'align': 'right', 
            'valign': 'vcenter'
        })
        
        bold = workbook.add_format({
            'bold': True,
            'border': 1,
            'align': 'right', 
            'valign': 'vcenter'
        })

        date_format = workbook.add_format({
            'num_format': 'yyyy-mm-dd',
            'border': 1,
            'align': 'left',
            'valign': 'vcenter'
            })
        
        # Set column widths
        sheet.set_column('A:A', 15)  # Column A width set to 15 characters
        sheet.set_column('B:B', 20)  # Column B width set to 20 characters
        sheet.set_column('C:C', 25)  # Column C width set to 25 characters
        sheet.set_column('D:D', 25)  # Column D width set to 25 characters
        sheet.set_column('E:E', 10)  # Column E width set to 10 characters
        sheet.set_column('F:F', 12)  # Column F width set to 12 characters
        sheet.set_column('G:G', 15)  # Column G width set to 15 characters

        sheet.write('A1', 'Date', header_format)
        sheet.write('B1', 'Reference', header_format)
        sheet.write('C1', 'Customer', header_format)
        sheet.write('D1', 'Product', header_format)
        sheet.write('E1', 'Quantity', header_format)
        sheet.write('F1', 'Unit Price', header_format)
        sheet.write('G1', 'Sub Total', header_format)
        row = 2
        total_sales = 0
        domain = []
        if data.get('date_from'):
            domain.append(('order_id.date_order', '>=', data.get('date_from')))
        if data.get('date_to'):
            domain.append(('order_id.date_order', '<=', data.get('date_to')))
        if data.get('product_id'):
            domain.append(('product_id', '=', data.get('product_id')))
        if data.get('partner_id'):
            domain.append(('order_id.partner_id', '=', data.get('partner_id')))
        objects = self.env['sale.order.line'].search(domain)
        for obj in objects:
            sheet.write('A' + str(row), obj.order_id.date_order.date(), date_format)
            sheet.write('B' + str(row), obj.order_id.name, cell_format)
            sheet.write('C' + str(row), obj.order_id.partner_id.name, cell_format)
            sheet.write('D' + str(row), obj.product_id.name, cell_format)
            sheet.write('E' + str(row), obj.product_uom_qty, cell_format)
            sheet.write('F' + str(row), obj.price_unit, money_format)
            sheet.write('G' + str(row), obj.price_subtotal, money_format)
            total_sales += obj.price_subtotal
            row += 1
        sheet.write('F' + str(row), 'Total Sales', bold)
        sheet.write('G' + str(row), total_sales, money_format)
