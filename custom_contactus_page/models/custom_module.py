# -*- coding: utf-8 -*-
from odoo import models, fields


class CustomModule(models.Model):
    _name = "custom.module"
    _description = 'Custom module'
    
    need_name = fields.Char()