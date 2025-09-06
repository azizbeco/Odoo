# -*- coding: utf-8 -*-
# from odoo import http


# class OdooLog(http.Controller):
#     @http.route('/odoo_log/odoo_log', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_log/odoo_log/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_log.listing', {
#             'root': '/odoo_log/odoo_log',
#             'objects': http.request.env['odoo_log.odoo_log'].search([]),
#         })

#     @http.route('/odoo_log/odoo_log/objects/<model("odoo_log.odoo_log"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_log.object', {
#             'object': obj
#         })

