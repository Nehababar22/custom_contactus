# -*- coding: utf-8 -*-
from odoo import models, fields,api


class CustomCrmModule(models.Model):
    """ Custom Crm module"""
    
    _inherit = 'crm.lead'
    _description = 'custom crm lead'

    minRange = fields.Integer()
    maxRange = fields.Integer()
    timeframe = fields.Char('Timeframe')
    thoughts = fields.Text('Thoughts')  
    need_ids = fields.Many2many('custom.module',string="Need Id")  
    attachment = fields.Binary(string='Attachments')
      
    def send_mail(self,lead_id):
        email_template_obj = self.env['mail.template']
        template_ids = email_template_obj.search([('name','=','RFQ - Send by Email'),('model_id.model', '=', 'crm.lead')])
        if template_ids:
            email=self.env['mail.template'].browse(template_ids.id).send_mail(lead_id)
            self.env['mail.mail'].browse(email).send()

        return True