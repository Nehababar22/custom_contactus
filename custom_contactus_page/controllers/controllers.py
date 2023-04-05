# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CustomForm(http.Controller):
    @http.route(['/contact'], type='http', auth="public", website=True)

    def custom_form(self, **post):
        return request.render("contactus_trinesis.tmp_custom_form", {})
    
    # @http.route(['/contact/submit'], type='http',csrf=False, auth="public", website=True)
    # def custom_form_submit(self, **post):            
    #     partner = request.env['crm.lead'].sudo().create({
    #         'name': post.get('name'),
    #         'email_from': post.get('email_from'),
    #         'phone': post.get('phone'),
    #         'company_id':post.get('company_id'),
    #         'minRange':post.get('minRange'),
    #         'maxRange':post.get('maxRange'),
    #         'need_ids' : post.get('need_ids'),
    #         'timeframe':post.get('timeframe'),
    #         'thoughts':post.get('thoughts'),
    #         'attachment':post.get('attachment'),
            
    #     })
                
    #     vals = {
    #         'partner': partner,
    #     }
    #     return request.render("contactus_trinesis.tmp_custom_form_success", vals)
    
    


# class ContactusTrinesis(http.Controller):
#     @http.route('/contactus_trinesis/contactus_trinesis', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contactus_trinesis/contactus_trinesis/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contactus_trinesis.listing', {
#             'root': '/contactus_trinesis/contactus_trinesis',
#             'objects': http.request.env['contactus_trinesis.contactus_trinesis'].search([]),
#         })

#     @http.route('/contactus_trinesis/contactus_trinesis/objects/<model("contactus_trinesis.contactus_trinesis"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contactus_trinesis.object', {
#             'object': obj
#         })
