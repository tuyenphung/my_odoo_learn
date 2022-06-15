from odoo import fields,models

class CreateClassModel(models.TransientModel):
    _name = 'create.class'
    _inherit = 'class'
    _description = 'Tạo Class'
    
    def create_class(self):
        for r in self:
            if r.name and r.school_id:
                self.env['class'].create([{'name':r.name,'school_id':r.school_id.id}])