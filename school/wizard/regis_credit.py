from odoo import fields, models, api

from odoo.exceptions import ValidationError

class StudentInheritMOdel(models.TransientModel):
    _name = 'student.regis'
    _inherit = 'student'

    school_ids = fields.Many2one('school', string='Danh sach truong')
    subject_list = fields.Many2many('subject', 'map_student_subject_regis', 'student_regis_id', 'subject_id', string='Đăng ký môn học :')
    class_list = fields.Many2one('class', string='danh sachs lớp')
    student_list = fields.Many2one('student' , string='danh sách học sinh',readonly=False)
    subject_list_regis = fields.Many2many(related='student_list.subject_list', string='MÔn học đã đăng ký',compute='_compute_student')
    @api.depends('student_list')
    def _compute_student(self):    
        if self.student_list:
            self.subject_list_regis = self.student_list.subject_list
    def action_regis(self):
        for r in self:
            if not r.subject_list_regis:
                if r.student_list:
                    student_regis = self.env['student'].search([('name', '=', r.student_list.name)])
                    if r.subject_list:
                        student_regis.write({
                            'subject_list': [(6, 0, r.subject_list.mapped('id'))]})
            else:
                raise ValidationError('bạn đã đã đăng ký môn học trước đó vui lòng chọn chức năng cập nhật (UPDATE)')
    def action_regis_update(self):
        for r in self:
            if r.subject_list_regis:
                if r.student_list:
                    student_regis = self.env['student'].search([('name', '=', r.student_list.name)])
                    print(student_regis.id)
                    print(r.subject_list)
                    if r.subject_list_regis:
                        for subject in r.subject_list:
                            if subject not in r.subject_list_regis:
                                student_regis.write({'subject_list':[(4,subject.id)]})
                            else:
                                raise ValidationError('bạn chỉ đợc đăng ký những môn học mới chưa có trong danh sách bạn đã đăng ký')
class SchooalModel(models.Model):
    _name = 'tests'
    _inherit = 'school','class'


#
# class ClassModel(models.Model):
#     _inherit = 'class'
#
#     regis_id = fields.One2many('student.regis', 'class_list')
#
#
# class StudentModel(models.Model):
#     _inherit = 'student'
#
#     regis_id = fields.One2many('student.regis', 'student_list')
