# -*- coding: utf-8 -*-

import base64
from openerp import models, fields, api
from datetime import datetime
from openerp import tools
import time
import os


class SaleMaryun(models.Model):
    _inherit = 'sale.order'

    #CAMPOS ANADIDOS PARA MARYUN###
    ###############################
    #forma_pago = fields.Selection ([('1','Contado'),('2','Credito')],'Forma de Pago')
    metodo_despacho = fields.Selection ([('v1','Inmediato'),('v2','Posterior'),('v3','A Domicilio')],'Metodo de Despacho')
    documento_tributario = fields.Selection ([('V1','Factura'),('V2','Boleta'),('V3','Guia de despacho'),('V4','Factura exenta')],'Documento Tributario')


#CAMPOS ANADIDOS PARA MARYUN IMPRESION A TXT###
###############################################
class InvoiceMaryun(models.Model):
    _inherit = 'account.invoice'

    txt_filename = fields.Char()
    txt_binary = fields.Binary()

    @api.one
    @api.depends('partner_id.name','date_due','amount_total','amount_untaxed','amount_tax','company_id.display_name', 'company_id.vat', 'company_id.street',\
        'company_id.city','company_id.state_id','partner_id.vat','partner_id.street','partner_id.city','partner_id.state_id', 'invoice_line')
    def generate_file(self):
        """
        function called from button
        """
        lineas = ''
        for txt in self.invoice_line.invoice_id:
            lineas = str(self.invoice_line.price_unit)
        self.lineas = lineas

        content = 'A0;;;;;;;;;;;' +'\n'\
        +'A;'+';33;'+';1.0;'+';1;'+';'+ str(self.date_due)+';;;;;;;;;;;;;'+str(self.date_due)+';'+str(self.company_id.vat)+';'+str(self.company_id.display_name)\
        +';;;'+str(unicode(self.company_id.street).encode("utf-8"))+';'+str(unicode(self.company_id.state_id).encode("utf-8"))+';'+str(unicode(self.company_id.city).encode("utf-8"))\
        +';;;'+str(self.partner_id.vat)+';;'+str(unicode(self.partner_id.name).encode("utf-8"))+';;'+str(unicode(self.partner_id.street).encode("utf-8"))+';'+str(unicode(self.partner_id.state_id).encode("utf-8"))\
        +';'+str(unicode(self.partner_id.city).encode("utf-8"))+';;;;;;;NO ESPECIFICA;;;'+str(int(round(self.amount_untaxed)))+';0;;19;'+str(int(round(self.amount_tax)))+';;;;;;'+str(int(round(self.amount_total)))+';;;'+'\n'\
        +'A1;501020;'+'\n'\
        +'B'+lineas+';'+ '\n'\
        +'Z;1;1;1;;'

        filename = "archivo.txt"
        try:
            f = open("/tmp/%s" % filename, "w")
            try:
                f.writelines( "%s" % content)
            finally:
                f.close()
        except IOError:
            pass

        return self.write({
            'txt_filename': ("%s" % filename),
            'txt_binary': base64.encodestring(content)
        })