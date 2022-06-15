from odoo import fields,models,api

class ClassModel(models.Model):
    _name = 'class'
    _description = 'Danh sách lớp'
    _parent_name = 'parent_id'
    parent_id = fields.Many2one('class', index=True, ondelete='cascade')
    _parent_store = True
    parent_path = fields.Char() 
    
    name = fields.Char(string='Tên lớp', required=True )
    quantity = fields.Integer(string='Sỹ số',compute='_total')
    @api.depends('student_list')
    def _total(self):
        for r in self:
            if r.student_list:
                r.quantity=len(r.student_list)
            else :
                r.quantity=0
    teacher_id = fields.Many2one('teacher',string='Giáo viên chủ nhiệm', ondelete='set null')
    #ondelete : sẽ làm gì khi đối tượng được liên kết bị xóa(nghĩa là đối tượng ONE)
    #set null: đặt trường liên kết -nghĩa là đặt giá trị cột thành NULL
    #cascade: xóa ONE thì xóa hết MANY
    #restrict: không thể xóa ONE khi có MANY liên kết tới . ấn xóa sẽ báo lỗi ràng buộc 
    #ondelete chỉ hỗ trợ M2O và M2M 
    grage = fields.Char(string='Khối', compute='_grage')
    @api.model
    def _grage(self):
        for r in self:
            r.grage = r.name[0:2]
    school_id = fields.Many2one('school',string='Trường',ondelete='set null')
    test_relate = fields.Integer(related = 'school_id.id')
    student_list=fields.One2many('student','class_id',string='Danh sachs học sinh',store=True)
    #trường One2many là trường ảo , không lưu trong database. 