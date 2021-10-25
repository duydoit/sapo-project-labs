from odoo import models, fields, api

class MyProduct(models.Model):
    _name = "your_products.your_products"
    _description = "My product model"

    name = fields.Char('Tên sản phẩm', required=True)
    description = fields.Text('Thông tin sản phẩm')
    price = fields.Integer('Giá bán', default=1)
    price_input = fields.Integer('Giá nhập', default=1)
    weight = fields.Float('Cân nặng (kg)')
    dob = fields.Date('Ngày tạo', required=False)
    product_image = fields.Binary("Ảnh sản phẩm", attachment=True, help="Pet Image")

    owner_id = fields.Many2one('res.partner', string='Owner')
    # product_ids = fields.Many2many(comodel_name='product.product',
    #                                string="Related Products",
    #                                relation='prods_product_rel',
    #                                column1='col_prods_id',
    #                                column2='col_product_id')