
from odoo import models,fields,api

class Product(models.Model):
    _name = "product.product"
    _inherit = "product.product"



    @api.model_create_multi
    def create(self,vals_list):

        records = super().create(vals_list)
        username = self.env.user.name
        for record in records:
            self.env["odoo_log.log"].create({
                "product_id":record.id,
                "username":username,
                "message":f"{username} {record.name} mahsulotni qo'shdi' "
            })
        return records

    def write(self, vals):

        old_name = self.name
        old_price = self.price
        old_quantity = self.quantity

        records = super(Product,self).write(vals)

        for record in records:
            if "name" in record:
                if old_name != record.name:
                    self.env["odoo_log.log"].create({
                        "username":self.env.user.name,
                        "message":f"{old_name} {record.name} ga o'zgardi "
                    })
            if "price" in record:
                if record.price > float(old_price):
                    self.env["odoo_log.log"].create({
                        "username":self.env.user.name,
                        "message":f"Mahsulot narxi {record.price - old_price} so'mga oshirildi "
                    })
                else:
                    self.env["odoo_log.log"].create({
                        "username": self.env.user.name,
                        "message": f"Mahsulot narxi {old_price - record.price} so'mga kamaytirildi "
                    })

            if "quantity" in record:
                if record.quantity > old_quantity:
                    sum = record.quantity + old_quantity
                    self.env["odoo_log.log"].create({
                        "username": self.env.user.name,
                        "message": f"Mahsulot qiymati {record.quantity} oshirildi. Jami miqdori {sum}"
                    })
                elif record.quantity < float(old_quantity):
                    sum = old_quantity - record.quantity
                    self.env["odoo_log.log"].create({
                        "username": self.env.user.name,
                        "message": f"Mahsulot qiymati {record.quantity} kamaytirildi. Jami miqdori {sum}"
                    })

                else:
                    self.env["odoo_log.log"].create({
                        "username": self.env.user.name,
                        "message": f"Mahsulot qiymati o'zgarmadi"
                    })
        return records

    def unlink(self):
        for record in self:
            self.env["odoo_log.log"].create({
                "username": self.env.user.name,
                "message": f" {record.name} nomli mahsulot o'cirildi "
            })
        return super().unlink()




