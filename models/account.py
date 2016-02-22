from openerp import models, fields, api


class AccountFilePathMaryun(models.Model):
    _name = 'account.filepath'

    txt_path = fields.Char('Ruta del archivo txt')
    txt_boolen = fields.Boolean('Estado')
