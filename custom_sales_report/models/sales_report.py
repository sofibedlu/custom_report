from odoo import models, api

class SalesReport(models.AbstractModel):
    _name = 'report.custom_sales_report.report_sales_details'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_from = data.get('date_from')
        date_to = data.get('date_to')
        product_id = data.get('product_id')
        partner_id = data.get('partner_id')
        domain = []
        if date_from:
            domain.append(('order_id.date_order', '>=', date_from))
        if date_to:
            domain.append(('order_id.date_order', '<=', date_to))
        if product_id:
            domain.append(('product_id', '=', product_id))
        if partner_id:
            domain.append(('order_id.partner_id', '=', partner_id))
        orders_lines = self.env['sale.order.line'].search(domain)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order.line',
            'orders_lines': orders_lines,
        }
