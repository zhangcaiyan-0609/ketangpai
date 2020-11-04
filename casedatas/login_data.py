
"""
File name: login_data.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/9/27 10:59 上午
"""
login_data_is_none = [
    {"title": "密码为空", "phone": "17610772806", "pwd": "", "expected": "密码不能为空"},
    {"title": "手机号为空", "phone": "", "pwd": "zhangcy4860801", "expected": "账号不能为空"},

]
login_data_password_wrong =[
    {"title":"密码长度少于6个字符","phone":"17610772806","pwd":"12345","expected":"密码有效长度是6到30个字符"},
    {"title":"密码长度大于30个字符","phone":"17610772806","pwd":"12345678901234567890123456789012","expected":"密码有效长度是6到30个字符"}
]
login_data_pass = [
    {"title": "登录成功", "phone": "17610772806", "pwd": "zhangcy4860801"}
]
login_data_fail = [
    {"title": "手机号错误", "phone": "17610772809", "pwd": "zhangcy4860801", "expected": "用户不存在"},
    {"title": "密码错误，登录第一次", "phone": "17610772806", "pwd": "python22", "expected": "密码错误, 你还可以尝试4次"},
    {"title": "密码错误，登录第二次", "phone": "17610772806", "pwd": "python22", "expected": "密码错误, 你还可以尝试3次"},
    {"title": "密码错误，登录第三次", "phone": "17610772806", "pwd": "python22", "expected": "密码错误, 你还可以尝试2次"},
    {"title": "密码错误，登录第四次", "phone": "17610772806", "pwd": "python22", "expected": "密码错误, 若再次失败, 10分钟内将禁止登入"}
]




