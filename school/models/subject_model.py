from odoo import fields,models

class SubjectMOdel(models.Model):
    _name = 'subject'
    _description = 'MÔn HỌc'
    
    name = fields.Char(string = 'tên môn học',required=True)
    author = fields.Char(string = 'tác giả')
    credit = fields.Integer(string='Số tín chỉ')