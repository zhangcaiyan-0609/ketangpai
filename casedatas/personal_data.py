
"""
File name: personal_data.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/30 7:03 下午
"""
personal_data_is_none =[
    {"title":"私信内容为空","message":" ","expected":"私信内容不能为空"}
]
personal_data_send_fail=[
    {"title":"不是好友，私信发送失败","message":"hello world","expected":"你们没有共同班级，无法发送私信"}
]
personal_data_send_success=[
    {"title":"是好友，私信发送成功","message":"hello python"}
]
personal_data_send_file =[
    {"title": "发送附件","expected":"test.py"}
]
search_data_by_code= [
    {"title":"以学号搜索","code":"002"}
]
search_data_by_name =[
    {"title": "以姓名搜索", "code": "小简"}
]
search_data_error =[
    {"title":"搜索内容不存在","code":" 00e","expected":"未搜索到结果"}
]
sheild_data =[
    {"title":"屏蔽某人","expected":"操作成功"},
    {"title":"取消屏蔽","expected":"操作成功"}
]