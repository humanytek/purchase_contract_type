from openerp import api, fields, models


class PurchaseContractType(models.Model):
    _inherit = 'purchase.order'

    contract_type = fields.Selection([
        ('axc', 'AxC'),
        ('pf', 'Precio Fijo'),
        ('pm', 'Precio Minimo'),
        ('pd', 'Precio Despues'),
        ('pb', 'Precio Base'),
        ('surplus', 'Excedente'),
        ('na', 'No aplica'),
    ], default='na', required=True)
