from odoo import fields,models
from odoo.exceptions import UserError

class CreateStudentModel(models.TransientModel):
    _name = 'create.student'
    _inherit = 'student'
    
    subject_list = fields.Many2many(store=False)
    school_id = fields.Many2one('school', string='Trường')
    
    def create_student(self):
        for r in self:
            if r.school_id and r.class_id and r.name and r.dob:
                self.env['student'].create([{'name':r.name,'dob':r.dob,'class_id':r.class_id.id}])
            else : raise UserError(('Vui lòng nhập  đầy đủ thông tin '))           