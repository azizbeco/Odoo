from odoo import models,fields

class Log(models.Model):
    _name = "odoo_log.log"
    _description = "log"

    username = fields.Char()
    message = fields.Text()

    product_id = fields.Many2one("product.product")
