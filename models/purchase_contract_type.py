from openerp import api, fields, models


class PurchaseContractType(models.Model):
    _inherit = 'purchase.order'
