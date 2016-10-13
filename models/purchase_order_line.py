from openerp import api, fields, models


class purchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    contract_type = fields.Selection(related="order_id.contract_type", readonly=True)
