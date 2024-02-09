from odoo import models, fields

class Vehicles(models.Model) :
    _name = 'rental.vehicles'
    _description = 'Vehicle given on rent'

    vehicle_name = fields.Char(string='Vehicle Name', required=True)
    vehicle_model = fields.Char(string='Vehicle Model', required=True)
    license_plate = fields.Char(string='License Plate', required=True)
    vehicle_image = fields.Binary(string='Vehicle Image')
    rc = fields.Binary(string='Registration Certificate', required=True)
    puc = fields.Binary(string='PUC Certificate', required=True)
    insurance = fields.Binary(string='Vehicle Insurace', required=True, help='Upload valid car insurance cover note')
    purchase_doc = fields.Binary(string='Vehicle Purchase', required=True, help='Upload valid vehicle purchase documents')
    vehicle_transmission = fields.Selection(
        string='Transmission Mode',
        selection=[('automatic', 'Automatic'), ('manual', 'Manual')],
        default='manual'
    )
    fuel_type = fields.Selection(
        string='Fuel Type',
        selection=[('cng', 'CNG'), ('petrol', 'Petrol'), ('diesel', 'Diesel')],
        default='petrol'
    )
    