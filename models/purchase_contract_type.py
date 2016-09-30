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

    tons = fields.Float(compute='_compute_tons', store=False)
    tons_text = fields.Text(compute='_compute_tons_text', store=False)
    product = fields.Many2one('product.product', compute='_compute_product', store=False)

    @api.one
    @api.depends('order_line')
    def _compute_tons(self):
        self.tons = 0;
        for line in self.order_line:
            self.tons = line.product_qty
            break

    @api.one
    @api.depends('tons')
    def _compute_tons_text(self):
        self.tons_text = "TODO"

    @api.one
    @api.depends('order_line')
    def _compute_product(self):
        product = False
        for line in self.order_line:
            product = line.product_id
            break
        self.product = product
