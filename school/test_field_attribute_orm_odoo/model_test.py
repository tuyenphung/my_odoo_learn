from odoo import fields,models,api
from odoo.exceptions import ValidationError

class TestTable(models.Model):
    _name = 'test'
    #tên của model
    _description = 'Test'
    #Tên gọi không theo quy chuẩn
    _rec_name = 'email' # nhãn của model ,đặt 'email' làm nhãn
    #mặc định là trường 'name'
    _auto = True # có lưu bảng vào database k, mặc định True với model tiêu chuẩn và TransientModel, False với AbtractMOdel
    _table = 'test_table' # tên bảng lưu vào database mặc định sẽ lấy trường _name #nếu trong tên có dấu '.' sẽ đổi thành '_'
    _registry = False # có đăng ký tạo instance không
    _log_access = False #có tạo trường tự động hay không (create_uid,write_uid,create_date)
    #vẫn có cột ID
    # _sequence = 'test_id_seq' #tên bảng để tạo các quy luật săp xếp cho trường id , bắt đầu, kết thúc , bước nhảy....
    _sql_constraints = [('name', 'unique(name)', "The student code must be unique!")]
    #ràng buộc tại database, nên dùng trong trường hợp xử lý với dữ liệu ở trong database, vd : check trùng tên
    @api.constrains('email')
    def _check_email(self):
        for r in self:
            if r.email:
                if r.filtered(lambda r: '@' not in r.email):
                    raise ValidationError(("email khong hợp lệ"))
    #ràng buộc tại server, nên dùng khi xử lý dữ liệu phức tạp, vd kiểm tra email, tính toán logic
    _abstract = False #nếu bằng True thì chỉ định model là abstract model
    _transient = False #nếu bằng True thì chỉ định model là transient model
    _order = 'id' # 'str' sắp xếp bản ghi theo tên trường vd : 'id' ....
    # _check_company_auto = False
    # _parent_name = 'parent_id'
    # _parent_store = False                                                                                                                        
    # _date_name = 'date'
    # _fold_name = 'fold'
    name = fields.Char(string = 'Tên',required= True)
    #name là trường dành riêng mặc định sử dụng cho _rec_name nếu không khai báo rec_name
    ## các thuộc tính của trường
    ''' *required bool , có bắt buộc có trường này hay không
        *store bool , có lưu vào database không
        *help (string) , hướng dẫn , trên view khi di vào tên trường trên form sẽ hiện chỉ dẫn
        *invisible bool có ẩn trường này không , ** thử nghiệm k được ,trong state thì được
        *readonly bool , chế dộ chỉ đọc không được sửa trên form , sửa được bằng code
        *index bool , thiết lâp chế độ indexing trong sql => nhóm các giá trị gần giống nhau để truy vấn rõ hơn, chỉ nên thiết lập với trường có khả năng tìm kiếm cao.
        *default -> giá trị mặc định nhận đầu vào là bool int string hoặc ** 1 hàm nhận vào recordset trả về giá trị tương ứng
        *groups = str sercurity câps độ field :xác định những nhóm người dùng 'str' có thể tương tác với trường này
        *copy bool trường này có được copy khi dùng hàm copy() trong ORM ,mặc định True với các trường lưu trong database
        *group_operator  bool : có thể hay không được sử dụng phương thức read_group ( array_agg :các giá trị ghép thành 1 mảng ,count :đếm số lượng ,count_distinct:số record không trùng lặp
            bool_and:băng True nếu các giá trị trả về là True và ngược lại , bool_or True nếu 1 True False nếu all False ,min max,avg giá trị lớn nhất nhỏ nhất, trung bình , sum tổng các giá trị
        *groupp_expand bool : mở rộng phương thức read_group()
        '''
    active = fields.Boolean(string='active',default=True)
    #trường dành riêng : để tạo thuộc tính active nếu bằng true sẽ ẩn khỏi tìm kiếm và danh sách
    state = fields.Selection(string='Status', selection=[('new', 'New'),
                                                        ('studying', 'Studying'),
                                                        ('off', 'Off')],
                                                    )
    lever = fields.Integer(string='Level',
                                       states={'new': [('invisible', True),('readonly', True)],
                                               'studying': [('invisible', False),('readonly', False)],
                                               'off': [('invisible', True),('readonly', True)]})
    '''trường state là trường dành riêng kiểu Selection dùng để khai báo thuộc tính states  '''
    
    
    email = fields.Char(string = 'Email')
    email_text = fields.Text(string='Email text',translate=True)
    ''' fields.Char : nhập string thường là 1 dòng , có thể set giới hạn qua thuộc tính size :int
                                        trim = bool xóa khoảng trắng đầu cuối, thực hiện trên viewview
                                        translate =bool hoặc callable True để dịch toàn bộ , callable dịch 1 phần translate(callable , value) chưa hiểu callable
        fields.Text : nhập string thường là đoạn văn bản , hiển thị dưới dạng hộp văn bản, cũng có thuộc tính translate 
                    có hàm callback để truy xuất các bản dịch ,** chưa hiểu
    '''
    def _test_default(self):
        return 1
    code = fields.Integer(string = 'code',default=_test_default)

    star  = fields.Float(string = 'Star',digits=(1,2))
    test_float = fields.Float()
    ''' fields.Interger số nguyên
        fields.Float số thập phân  **thuộc tính digits để xác định phần chữ số sau phần thập phân
            digits= tuple(int,int)
                        str tham chiếu đến bảng decimalprecsioncsion
        fields.Float.round(): làm tròn đên phần thập phân
        fields.Float.is_zero
        fields.Float.compare yêu cầu thực hành để hiểu
    ''' 
    document = fields.Binary(string='Tài liệu')
    images = fields.Image(string='Tài liệu')
    ''' 
        fields.Binary lưu tệp tin, ảnh. 
            attachment bool mặc đinh là True , lưu trong database hay trong bảng ir_actachment
            prefect  bool mặc định False ,có hay không tìm nạp trước
            _depends_context = 'str' phụ thuộc vào ngữ cảnh ** phải hỏi lại
        fields.Image lưu ảnh
            max_width,max_height dài và rộng tối đa, nếu lớn hơn thì sẽ thu lại bằng với width và height đã set
            verify_resolution : bool có hay không giới hạn độ phân giải . odoo.tools.image.ImageProcess
    '''
    currency_id = fields.Many2one('res.currency')
    curency = fields.Monetary(string='Curency', currency_field = 'currency_id')
    ''' 
        fields.Monetary đóng gói Float để biểu thị loại tiền tệ nhất định , độ chính xác phần thập phân được thể hiênh băng curency_field
            currency_field mặc định bằng 'currency_id' là một trường many2one đến model res.currency
    '''
    #tìm hiểu về selection
    html = fields.Html(string='HTML')
    ''' đóng gói mã Html 
        fields.Html
            sanitize = bool , có được làm sạch hay không
            sanitize_tag = bool có làm sạch thẻ hay không
            sanitize_attribute = bool có làm sạch thuộc tính hay không , sanitize _stype,strip_style,strip_classes
    '''
    date_start = fields.Datetime(string='datetime')
    date_start_context_today = fields.Datetime()

    date_start_day = fields.Date(string='date')
    date_start_add = fields.Datetime(compute='_day_start')
    date_subtract = fields.Date(compute='_subtract')
    @api.depends('date_start_day')
    def _day_start(self):
        for r in self:
            r.date_start_add = fields.Datetime.to_datetime(fields.Date.today())
    test_end_of = fields.Date(compute='_end_of')
    def _subtract(self):
        for r in self:
            if r.date_start_day:
                r.date_subtract = fields.Date.subtract(r.date_start_day, days=-10)
            else : r.date_subtract = r.date_start_day
        
    @api.depends('date_start_day')
    def _end_of(self):
        for r in self:
            if r.date_start_day:
                r.test_end_of = fields.Date.start_of(r.date_start_day,'month')
            else : r.test_end_of = r.date_start_day
    '''
    chỉ gán : +đối tượng date hoặc đối tượng datetime có trường date và datetimedatetime
                +chuỗi đúng dịnh dạng yyyy-mm-dd date hoặc yyyy-mm-dd hh-mm-ss chp datetimedatetime
                +có thể gán bằng False hoặc NONE
            to_date() phân tích cú pháp thành date
            to_datetime thành datetime
            có thẻ so sánh giữa các đối tượng date vs date và datetime vơis datetime 
            so sánh giữa 2 đối tượng datetime và date kết quả k như mong đợi vì chuỗi datetime luôn lớn hơn date
            có các phép toán cộng trừ ... odoo.tools.date_untils
            ** múi giờ, các trường datetime được lưu trong database dưới dạng cột timestimestamp_without_timezone
    '''


    
    
    @api.autovacuum
    def _test_autovacuum(self):
        if self.date_start > fields.Date.context_today():
            return self.unlink()
    
    