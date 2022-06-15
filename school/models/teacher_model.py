from odoo import fields,models,api

class TeacherModel(models.Model):
    _name = 'teacher'
    _description = 'Danh sách giảng viên'
    
    name = fields.Char(string = 'Tên giangr viên' , required=True)
    dob = fields.Date(string = 'Ngày sinh')
    age = fields.Integer(string = 'Tuổi', compute='_age')
    @api.depends('dob')
     
    def _age(self):
        for r in self:
            if r.dob:
                r.age = fields.Date.today().year - r.dob.year
            else :
                r.age = 0
    school_id = fields.Many2one('school',string='Trường')
    class_list = fields.One2many('class','teacher_id',string='Danh sách lớp')