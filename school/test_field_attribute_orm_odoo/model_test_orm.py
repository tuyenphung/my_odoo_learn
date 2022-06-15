from odoo import fields, models, api


class Test2(models.TransientModel):
    _name = 'test.orm'
    _inherit = 'student'
    
    
    def button_onclick(self):
        print('')

    # school_ids = fields.Many2one('school', string='Danh sach truong')
    subject_list = fields.Many2many('subject', 'map_student_subject_orm', 'student_orm_id', 'subject_id', string='Đăng ký môn học :')
    # class_list = fields.Many2one('class', string='danh sachs lớp')
    # student_list = fields.Many2one('student' , string='danh sách học sinh',compute='_compute_student',readonly=False)
    # subject_list_regis = fields.Many2many(related='student_list.subject_list', string='MÔn học đã đăng ký')
    button_create = fields.Boolean(string='CLICK ON')
    button_default_get = fields.Boolean(string='CLICK ON')
    button_write = fields.Boolean(string='CLICK ON')
    button_copy = fields.Boolean(string='CLICK ON')
    button_browse = fields.Boolean(string='CLICK ON')
    button_name_search = fields.Boolean(string='CLICK ON')
    button_filtered = fields.Boolean(string='CLICK ON')
    button_filtered_domain = fields.Boolean(string='CLICK ON')
    button_mapped = fields.Boolean(string='CLICK ON')
    button_name_create = fields.Boolean(string='CLICK ON')
    button_read = fields.Boolean(string='CLICK ON')
    button_search_count = fields.Boolean(string='CLICK ON')
    button_search = fields.Boolean(string='CLICK ON')
    
    running_char = fields.Text(string='Luồng chạy' ,readonly=True)
    return_char = fields.Char(default='RETURN:',readonly=True)
    
    domain = [('name', '=', 'Student1')]
    val_list =[{'name':'TUyến'},{'name':'Tuyến1'}]
    
    
    default_get_char = fields.Char(default="self.default_get(['student_test_field','dsafadsfa'])",string='Cú pháp',readonly=True)
    name_create_char = fields.Char('Cú pháp' ,default = "self.env['student'].name_create('pvt')",readonly=True)
    copy_orm_char = fields.Char(string='Cú pháp', default="self.env['student'].search([('id','=',1)]).copy() " ,readonly=True)
    create_orm_char = fields.Char(string='Cú pháp', default="self.env['student'].create(self.val_list))",readonly=True)
    write_orm_char = fields.Char(string= 'Cú pháp', default="self.env['school'].search([('id','=','1')]).write({'class_list':[(0,0,{'name':'class'})]})",readonly=True)
    search_orm_char = fields.Char(string='Cú pháp',readonly=True, default="self.env['student'].search([('name','=','Student1')], offset=self.search_offset, limit=self.search_limit, order=self.search_order, count=self.search_countt)")
    browse_orm_char = fields.Char('Cú pháp', default="self.env['student'].browse([1,2,3,100])",readonly=True)
    search_count_orm_char = fields.Char('Cú pháp',default="self.env['student'].search_count()",readonly=True)
    name_search_orm_char = fields.Char('Cú pháp', default="self.env['student'].name_search()",readonly=True)
    read_orm_char = fields.Char('Cú pháp' , default="self.env['student'].search([]).read()",readonly=True)
    filtered_orm_char = fields.Char('Cú pháp', default="self.env['class'].search([]).filtered('school_id' )",readonly=True)
    filtered_domain_orm_char = fields.Char('Cú pháp', default="self.env['class'].search([]).filtered_domain([])",readonly=True)
    mapped_orm_char = fields.Char('Cú pháp',default="self.env['class'].search([]).mapped('')",readonly=True)
    
    search_domain = fields.Char(string='DOMAIN', default=domain, readonly=True)
    search_offset = fields.Integer(string='OFFSET')
    search_limit = fields.Integer(string='limit', default=100)
    search_order = fields.Char(string='order')
    search_countt = fields.Boolean(string='Count?')
    orm_return = fields.Text(string='KẾT QUẢ',readonly=True)
    create_val_list = fields.Char('Vals_list',default=val_list)


    #self.env


    def create_orm(self): #self.create() 
        self.running_char = ''' 
        hàm self.create() #các hàm liên quan self.browse 
        => truyền vào 1 list các dict
        check quyền create với người dùng hiện tại (True hoặc raise error)
        => phân loại các loại field(field , compute field, inverse field) để xử lý
        => gọi phương thức _create để query lưu vào database
        => check python constrain 
        **** cần debug rõ hơn, chi tiêt hơn nếu cần ***
        '''
        self.orm_return = str(self.env['school'].sudo().create([])) +'\n'+'NOTE\n'+'''*Nếu truyền vào list rỗng sẽ trả về record rỗng = không lưu gì vào database .
    Nếu truyền vào dict rỗng thì nếu không có trường nào required thì sẽ lưu 1 bản ghi vào database với 
    các trường có value là null .
    Trả về record với các trường là null,những trường có set default thì vẫn có giá trị default
    * Có thể truyền vào list rỗng, list các dict hoặc 1 dict duy nhất
    trả về recordset (rỗng hoặc các record được tạo) 
    ***nếu trong model có trường chứa required thì bắt buộc phải truyền 
    '''
        print(self._context)
    def orm(self):
        self.orm_return=self.sudo().create_orm()
        
        
    def copy_orm(self): #self.copy(),phương thức liên quan cần tìm hiểu self.copy_data(),self.copy_translations()
        self.running_char =  '''
        self.copy() luồng chạy : 
        =>truyền vào {} với key là giá trị mới muốn cập nhật,hoặc k truyền gì
        =>check 1 bản ghi
        => thực hiện xử lysd những data thay thế so với data của record gốc
        => tạo record mới sau khi đã xử lý với with_contex(lang=none) 
        => thực hiện translate với hàm copy_translations *** cần xem lại nếu rảnh
        => trả về record
        '''
        print(self._context)
        self.orm_return = str(self.env['student'].search([('id','=',1)]).copy()) + '\n' + '''NOTE
        Copy chỉ thực thi với 1 record duy nhất
        Thực hiện kiểm tra bởi hàm ensure_one() 
        trả về record vừa nhân bản 
        có thể truyền vào dict với giá trij mới cho key(field)
        chú y : ** các giá trị có vi phạm contrain k ,
        mặc định sẽ KHÔNG copy GIÁ TRỊ các trường O2M và M2M nếu muốn thì thêm attribute copy=True vào các trường đó
        không thể thực thi với recordset rỗng hoặc len(recordset) >1 '''
    def default_get_orm(self): #self.default_get() #conver_to_cache và convert_to_write cần tìm hiểu thêm
        self.running_char =  '''
        self.default_get() Luồng chạy
        =>truyền vào 1 list  các field cần tìm 
        =>check xem field đó có giá trị default ở trong (model.field , bangr ỉr.default, trong context hay không)
        =>convert giá trị của  các trường có default
        => trả về dict các key value (tên trường : giá trị default)
    
        '''
        
        self.orm_return = str(self.env['student'].default_get(['student_test_field','name'])) + ''' 
        NOTE 
        truyền vào field list (ORM thực hiện check xem trong list đó có field nào có giá trị mặc định không
        Trả về 1 dict với key là trường và value là giá trij mặc định
        *** chỉ trả về các field có giá trị mặc định 
        truyền vào field k tồn tại vẫn được nhưng k trả ra gía trị
        '''
    def name_create_orm(self): #self.name_create() #phương thức liên quan self.create
        self.running_char =  ''' 
        default_get() luồng chạy 
        => truyền vào string
        =>kiểm tra có trường name trong model k (if self._rec_name)
        =>gọi phương thức create với trường name = string
        '''
        self.orm_return = str(self.env['student'].name_create('pvt')) + '''
        NOTE 
        truyền vào str(name) sẽ tạo ra một record mới với tên truyền vào
        các trường có defaul cũng tự set giá trị default
        *** Nếu có trường required khác thì khi viết code sẽ gọi ra lỗi
        trường hợp sử dụng :Khi nhập many2one trên view form  nếu nhập 'One' là giá trij chưa có thì sẽ có lựa chọn taoj nhanh record với name=...
        trên view form nếu tạo 'One ' mà bên One có trường required thì sẽ gọi form của One ra
        '''
    def write_orm(self): #self.write()
        self.running_char =  '''
        record.write() luồng chạy
        =>truyền vào dict các giá trị cập nhật mới cho record gọi phương thức này
        => check bản ghi có tồn tại hay không => trả về true nếu k có
        =>check các quyền access right access rule và field access right với user hiện tại 
        '''
        
        self.orm_return = str(self.env['tesss'].search([('id','=','1')]).write({'type':'private'}))+'''
        NOTE 
        Chỉ trả về True hoặc Lỗi
        ***hàm write không viết  trực tiếp vào database mà chỉnh sửa trên recordset ***
        truyền vào 1 dict: keys là tên fields ,value là value muốn cập nhật cho trường đó(chú ý kiểu dữ liệu )
        many2one = id (One)
        one2many và many2many: dùng cú pháp đặc biệt
        'O2M or M2m field': [(0,,id)] tạo một record mới bên model many
                            [(1,id,value)] cập nhật record bên model many với id=id và value =value
                            [(2,id,0)] xóa record bên model many với id =id sau đó vào database và xóa
                            [(3,id,0)] chỉ xóa trong record nhưng k xóa trong database
                            [(4,id,0)] thêm 1 record bên many đã có vào One
                            [(5,0,0)] xóa hết các liên kết của bên many với one
                            [(6,0,ids)] xóa hết và thêm các ids mới 
        '''
    def search_orm(self):#self.search()
        self.running_char =  ''' 
        self.search() luồng chạy
        => nhập vào list domain , offset(int) , limit(int) , oder(str) , count(bool)
        => thực hiện query trong bảng của model self qua phương thức self._search() 
        *** xem thêm self._search()
        =>trả về recordset , nếu count=True thì trả về số lượng
        '''
        self.orm_return = str(self.env['student'].search([('test_search','=','12313')], offset=self.search_offset, limit=self.search_limit, order=self.search_order, count=self.search_countt)) + '''
        NOTE 
        có thể truyền vào list domain hoặc 1 list rỗng để trả về tất cả các record
        offset số lượng record bị bỏ qua
        limit số lượng tối đa hiển thị số bản ghighi
        oder thực hiện sắp xếp records theo trường nào
        count có thì trả về số lượng thay vì recordset
        search luôn vào database
        '''
    def browse_orm(self): #self.browse() self._browser
        self.running_char =  '''
        self.browse() luồng chạy
        => nhập vào 1 list ids hoặc 1 id (int) 
        => set định dạng trả về
        => trả về dưới dạng recordset
        
        '''
        self.orm_return = str(self.env['student'].browse([1,2,3,100]))+'''
        NOTE 
        có thể truyền vào bất kể gì (str,list,int,dict)
        phương thức chỉ thực hiện convert các giá trị truyền vào về dạng recordset thôi
        có thể thực hiện kiểm tra records có tồn tại hay không dùng hàm records.exists()
        *** exists() 
        '''
        print(self.env['student'].browse(False).exists())
        # for r in self.env['student'].browse([1,2,3]):
        #     if r.exists():
        #         print('a')

    def search_count_orm(self):#self.search_count()
        self.running_char =  ''''''
        self.orm_return = str(self.env['student'].search_count())+'''
        NOTE 
        phương thức self.search_count() gọi lại phương thức search với count =True
    
        '''
    def name_search_orm(self): #self.name_search()
        self.running_char =  '''
        self.name_search() luồng chạy
        =>truyền vào name = 'str' ,list(tuple) các domain, operator '=','like' ,..mặc định là ilike,
        limit
        =>dùng phương thức _name_search với các kiều kiện trên
        =>trả về kết quả của phương thức self.browse(ids).sudo().name_get()
        '''
        self.orm_return = str(self.env['student'].name_search())+'''
        NOTE 
        operator là toán tử dùng cho domain tìm kiếm cho name truyền vào
        trả về list các tuple gồm id và giá trị trường name của các record thỏa mãn điều kiênj
        '''
    def read_orm(self):#self.read()
        self.running_char =  '''
        self.read()
        => truyền vào list các trường cần đọc với các record đó,mặc định là tất cả các trường
        =>check quền đọc của người dùng hiện tại
        =>check field có tồn tại hay không, check field có lưu database hay k
        =>tìm các hàm phụ thuộc trước
        =>query vào trong database để lấy dữ liệu thông qua hàm _read
        => trả về list các dict chứa thông tin của các field của các bản ghi
        '''
        self.orm_return = str(self.env['student'].browse([1,2,3]).read())+'''
        NOTE 
        read query vào database,**** self._read()
        sau đó nạp vào cache, trả về list các dict mỗi dict là 1 record
        '''       
    def filtered_orm(self):#self.filtered()
        self.running_char =  '''
        self.filtered() luồng chạy
        =>truyền vào 1 hàm (hàm trả về các record phù hợp với hàm) 
        hoặc 1 string vd các trường chấm
        =>trả về các record thỏa mãn điều kiện của hàm 
        '''
        def testttt(self):
                
            return self if self.school_id.id == 1 else self.browse()
        classs = self.env['class'].search([])
        a =lambda clas2ss : clas2ss.school_id.id == 1 
        self.orm_return = str(self.env['class'].search([]).filtered(testttt))+'''
        NOTE 
        truyền vào string là những trường thuộc model
         hàm filter sẽ thực hiện locj những record mà trường đó có giá trị
        nếu truyền vào str k đúng sẽ báo lỗi
        truyền vào 1 hàm trả về *không có ý nghĩa* sẽ trả về tất cả record theo phương thức browse
        truyền vào hàm sẽ trả về recordset với các record phù hợp với điều kiện của hàm
        *** note nhỏ : k thể truyền vào False vì return có set điều kiện rec.id for rec in self if func(rec)
        '''     
    def filtered_domain_orm(self):#self.filtered_domain()
        self.running_char =  '''
        self.filtered_domain() luồng chạy
        =>truyền vào domain
        =>xử lý các mutiple domain
        =>xử lý các domain
        => trả về các record phù hợp với domain
        '''
        self.orm_return = str(self.env['class'].search([]).filtered_domain(False))+'''
        NOTE 
        nếu truyền vào list rỗng sẽ trả về tất cả các record
        '''     
    def mapped_orm(self):#self.mapped()
        self.running_char =  '''
        self.mapped() luồng chạy 
        => truyền vào 1 string tên trường để trả về list các giá trị của trường
        => trường là trường quan hệ sẽ trả về các record quan hệ hoặc giá trị của các trường của record quan hệ
        =>truyền vào hàm 
        =>trả về record hoặc list giá trị
        '''
        self.orm_return = str(self.env['class'].search([]).mapped('name'))+'''
        NOTE 
        nếu truyền vào str rỗng sẽ trả về tất cả các record
        truyền vào tên trường để trả về list các giá trị của trường
        trường là trường quan hệ sẽ trả về các record quan hệ hoặc giá trị của các trường của record quan hệ
        là 1 hàm sẽ trả về các record thỏa mãn hàm
        '''     
    