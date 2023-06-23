from odoo import models, fields

class Covenantrecords(models.Model):

    _name = 'covenant.record'
    _description = 'covenant Management'


    name = fields.Char(string='Name',requird=True)
    type = fields.Char(string='Type')
    employee = fields.Char(string='Employee')
    date = fields.Date(string='Date')