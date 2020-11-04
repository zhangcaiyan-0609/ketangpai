
"""
File name: course_data.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/22 4:25 下午
"""
add_course_data_pass =[
    {"title":"加入课程成功", "verificate_code":"P69UVV","expected":"加入课堂成功"}
]
add_course_data_fail=[

    {"title":"验证码错误", "verificate_code":"P69YYY","expected":"该加课码不存在或者已经失效"},
    {"title":"验证码少于6位", "verificate_code": "P69","expected": "加课验证码必须是6位字符"},
    {"title":"验证码多于6位", "verificate_code": "P69P69UVVVV","expected": "该加课码不存在或者已经失效"},
    {"title":"课程已加过", "verificate_code":"P69UVV","expected":"你已经选过此课程"},
    {"title":"课程已停加","verificate_code":"L5JSSS","expected":"老师已经关闭加课"}
]

drop_course_data =[
    {"title":"退出课程成功", "password":"zhangcy4860801","expected":"课程退课成功"},
    {"title":"密码错误", "password":"zhangcy","expected":"密码错误"}
]