from odoo import models, fields, api, _

#------------------- MODEL CAR ---------------------#
class MycarsCar(models.Model):
    _name = 'car.cars'
    _description = 'model car cars'

    name = fields.Char("Name Cars")
    car_sequence = fields.Char(string='Name Cars', required=True, copy=False, readonly=True,
                               index=True, default=lambda self: _('New'))
    horse_power = fields.Integer()
    door_number = fields.Integer()
    owner_id = fields.Many2one('res.partner')
    parking_id = fields.Many2one('parking.parking')
    feature_list = fields.Many2many('car.feature', 'relation_feature_car',
                                    'car_idc', 'feature_idc', string=" Car and Feature")
    total_speed = fields.Integer(compute="_value_speel", store=True)
    status = fields.Selection([("new", "new"), ("user", "user"), ("sold", "sold")], default="new")
    last_check = fields.datetime()

    @api.depends('horse_power')
    def _value_speel(self):
        for record in self:
            record.total_speed = record.horse_power * 5

    @api.model
    def create(self, vals):
        if vals.get('car_sequence', _('New')) == _('New'):
            vals['car_sequence'] = self.env['ir.sequence'].next_by_code('seq.cars.name') or _('New')
        result = super(MycarsCar, self).create(vals)
        return result

#------------------- MODEL FEATURE ---------------------#
class MycarsFeaature(models.Model):
    _name = 'car.feature'
    _description = 'model car feature'

    name = fields.Char()

#------------------- MODEL PARKING ---------------------#
class MycarsParking(models.Model):
    _name = 'parking.parking'
    _description = 'model parking parking'

    name = fields.Char()
    active = fields.Boolean("Active", default="True")
    car_ids = fields.One2many('car.cars', 'parking_id')
    number_car = fields.Integer()
