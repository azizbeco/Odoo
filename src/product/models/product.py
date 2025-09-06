from odoo import models,fields

class Product(models.Model):
    _name = "product.product"
    _description = "product"

    name = fields.Char(string="Mahsulot nomi",required=True)
    price = fields.Float(string="Mahsulot narxi",required=True)
    quantity = fields.Integer(string="Mahsulot miqdori",required=True)

    

