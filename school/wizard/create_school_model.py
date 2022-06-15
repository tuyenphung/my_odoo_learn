from odoo import fields, models
from odoo.exceptions import ValidationError


class CreateSchoolModel(models.TransientModel):
    
    _name = 'create.school'
    _inherit = 'school'
    _description = 'Tạo Trường Đại Học'
    
    
    email = fields.Char(required=False)
    def create_school(self):
        for r in self:
            if r.name and r.email and r.phone and r.type and r.add:
                self.env['school'].create([{'name':r.name, 'email':r.email, 'phone':r.phone, 'type':r.type, 'add':r.add}])
            else:
                raise ValidationError('Vui lòng nhập đầy đủ các trường')