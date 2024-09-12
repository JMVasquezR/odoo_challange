# -*- coding: utf-8 -*-
# from odoo import http


# class OdooChallenge(http.Controller):
#     @http.route('/odoo_challenge/odoo_challenge', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_challenge/odoo_challenge/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_challenge.listing', {
#             'root': '/odoo_challenge/odoo_challenge',
#             'objects': http.request.env['odoo_challenge.odoo_challenge'].search([]),
#         })

#     @http.route('/odoo_challenge/odoo_challenge/objects/<model("odoo_challenge.odoo_challenge"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_challenge.object', {
#             'object': obj
#         })

