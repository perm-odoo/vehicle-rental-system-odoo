from odoo import models, fields

class Owners(models.Model) :
    _name = 'rental.owners'
    _description = 'Owners of rented vehicles'

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address', required=True)
    postcode = fields.Integer(string='Post Code', required=True)
    phone = fields.Integer(string='Phone Number', required=True)
    aadhar_card = fields.Binary(string='Aadhar Card', required=True)
    aadhar_number = fields.Integer(string='Aadhar Number', required=True)
    pan_card = fields.Binary(string='PAN Card', required=True)
    pan_number = fields.Integer(string='PAN Number', required=True)