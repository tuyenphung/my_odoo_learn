{
    'name': "Shool_Manager and registration Credit",
    'name_vi_VN': "Quản lý trường học và đăng ký TÍn chỉ",

    'summary': """
Look up student information
and registration credit for student
""",
    'summary_vi_VN': """
Tra cứu thông tin học sinh và Đăng ký tín chỉ cho sinh viên
""",

    'description': """
Manager and registration
============
Long description of module's purpose

Key Features
============
1. Feature 1

   * Sub-Feature 1
   * Sub-Feature 2

     * Sub-sub-feature 1
     * Sub-sub-feature 2

2. Feature 2

   * Sub-Feature 1
   * Sub-Feature 2

Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Ứng dụng này làm gì
===================
Mô tả chi tiết về module

Tính năng chính
===============
1. Manager
   for Manager
     * quảng lý thêm tạo sửa xóa trường , lớp , sinh viên, giảng viên, cũng như đăng ký tín chỉ cho sinh viên
2. for EMPLOYED_regis

   *Tạo sinh viên
   * Đăng ký môn học cho sinh viên
3. for sinh viên
    xem danh sách môn học đã đăng ký , học phí
Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

""",

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v14demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v14demo-vn.viindoo.com",
    'support': "apps.support@viindoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/school_security.xml',
        'security/ir.model.access.csv',
        'data/data_subject.xml',
        'data/data_student.xml',
        'data/data_class.xml',
        'data/data_school.xml',
        'data/data_teacher.xml',
        'data/data_student.xml',
        'views/school_view.xml',
        'views/class_view.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/subject_view.xml',
        'views/view_test.xml',
        'test_field_attribute_orm_odoo/test_view.xml',
        'wizard/regis_credit.xml',
        'wizard/create_student_view.xml',
        'wizard/create_school_view.xml',
        'wizard/create_class_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'images': [
        ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 99.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
