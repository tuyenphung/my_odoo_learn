from odoo import fields, models , api

from odoo.exceptions import ValidationError


class SchoolModel(models.Model):
    '''
    các trường tự động khi tạo model : id(Integer) , create_date(datetime), create_uid(many2one)
    write_date(datetime), write_uid(many2one)
    '''
    '''trường đặc biệt :
    *name: được lấy để đặt giá trị mặc định cho _rec_name,
    *active:chuyển đổi chế độ hiển thị của bản ghi, nếu active được đặt thành False bản ghi
    là ẩn trong hầu hết các tìm kiếm và danh sách, kiểu Boolean.
    *state :được sử dụng trong thuộc tính states của fields, kiểu Selection
    *parent_id: giá trị mặc định của _parent_name, được sử dụng để tổ chức các bản ghi trong cấu trúc cây,
    cho phép sử dụng toán tử child_of và parent_of trong các miền, kiểu Many2one.
    *parent_path: nếu 'parent_store' = True khai báo trường này để lưu trữ đường dẫn của cấu trúc cây
    *company_id: kiểm tra tính nhất quán của các công ty. TỨc là xacs đinh 1 bản ghi đựơc xem bởi nhiều công ty
    hay chỉ những người trong công ty nhất định mới đươc truy cập
    ''' 
    _date_name = 'days'
    _fold_name = 'price'
    _name = 'school'
    parent_id = fields.Many2one('school', index=True, ondelete='cascade')
    _parent_store = True
    parent_path = fields.Char() 
    # Tên của bảng trong database, khi lưu vào trong database nếu có ký tự '.' sẽ thay thành '_'
    _description = 'Danh sách trường học'
    # Nhãn của bảng
    _auto = True  # có lưu trong database hay không mặc đinh False với AbstractMOdel
    _registry = True
    _log_access = True  # có tạo hay không những trường thông tin tự động
    _table = 'school'  # set tên bảng được lưu trong database, mặc định lấy _name
    days = fields.Date()
    
    
    # _sequence = 5
    # các fields Char,Integer,Float,Selection,Date,Datetime,Text,Binary,Image,Các trường quan hệ 
    name = fields.Char(string='Tên Trường')
    name_context = fields.Char(compute='_context_test')
    # string = 'unicode' nhãn dán hiển thị của trường
    # required=bool => có bắt buộc nhập hay không
    email = fields.Char(string='Email',group_operator = 'array_agg')
    type = fields.Selection(selection=[('private', 'Dân Lập'), ('public', 'Công Lập')], string='Loại Trường', default='public')
    # selection nhận vào 1 list các tuple với cặp giá trị key và string, selection lưu vào database với kiểu Char 
    # default => có thể nhận int , str , bool , 1 hàm nhận vào recordset trả về giá trị tương ứng
    phone = fields.Char(string='Số điện thoại')
    add = fields.Char(string='Địa chỉ', index=True)
    # index thiết lập chế dộ index cho cột đó, sql sẽ thực hiện chế độ index nhóm các giá trị theo quy luật 
    # để thực hiện tìm kiếm nhanh hơn, chỉ nên dùng ở những trường có xu hướng tìm kiếm cao 
    price = fields.Float(string='Giá tiền 1 học phần' , compute='_pricee',group_operator = 'sum')
    date_start = fields.Datetime()
    date_end = fields.Datetime()
    # compute là hàm tính toán lạilại
    ahihi = fields.Html(string='ahaha', default=('<h1>ahaha</h1>'))
    dated = fields.Date(string='Ngày thành lập' , compute='_datedd')
    test_group = fields.Integer(group_operator = 'sum')
    @api.depends('create_date')
    def _datedd(self):
        for r in self:
            if r.create_date:
                
                r.dated = r.create_date
            else: r.dated = '1999-01-01'

    ''' compute nhận đầu vào là một phương thức  
        thuộc tính : compute_sudo bool xác đinh trường này sẽ được tính toán với quyền cao nhất tưc là không bị giới hạn bởi các phân quyền
                    vd nó liên quan đến bảng mà không được quyền truy cập thì vẫn dùng đc mà k lỗi , mặc định là True với các hàm compute lưu trong database
                    inverse nhận giá trị là hàm đảo ngược phương thức nghĩa là hàm nhập ngược, sửa giá trị compute sẽ thay đổi ngược giá trị phụ thuộc , phải set readonly =False
                    search nhận hàm tìm kiếm giá trị cụ thể cho trường này
                    related str chuỗi các tên trường được related
    '''

    @api.depends('type')   
    def _pricee(self):
        # self là recordset chứa các record
        # trong view form thì recordset chứa 1 record với id tương ứng
        for r in self:
            if r.type:
                if r.type == 'private':
                    r.price = 500000
                else:
                    r.price = 300000 
            else: r.price = 0

    class_list = fields.One2many('class', 'school_id', string='Danh sách lớp')
    # one2many là trường ảo và không lưu trong database
    teacher_list = fields.One2many('teacher', 'school_id', string='Danh sách giang viên')
    _sql_constraints = [('age_erro', 'CHECK(age>0)', "tuổi phải lớn hơn 0")]

    # sql constraints thực thi và thực hiện ràng buộc tai CSDL 
    # api.constraints thực hiện chặn record ngay trên server
    # nên dùng sql constrain khi các ràng buộc giữa các dữ liệu trong sql với nhau, vd kiểm tra trùng tên trùng email
    # nên dùng sql python (api.constraints) khi thực hiện các phép logic python với record đó
    # VD kiểm tra email hợp lệ
    @api.constrains('email')
    def _check_email(self):
        for r in self:
            if r.email:
                if self.filtered(lambda r: '@' not in r.email):
                    raise ValidationError(("email khong hợp lệ"))
    

    # @api.depends_context('lang')
    def _context_test(self):
        
        for r in self:
            r.name_context = r.name.upper() + r._context['lang']
    @api.model
    def create(self, vals):
        if 'name' in vals:
            vals['name'] = vals['name'].upper()
        return super(SchoolModel, self).create(vals)
        
        
class Modeltesss(models.Model):
    _name = 'tesss'
    _inherit = 'school'
