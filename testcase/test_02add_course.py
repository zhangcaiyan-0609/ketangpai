
"""
File name: test_02add_course.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/22 4:22 下午
"""
import pytest
from common.base_page import BasePage
from casedatas import course_data
from common.handle_log import log
import time


class TestAddCourse:
    @pytest.mark.parametrize('case',course_data.add_course_data_pass)
    def test_add_course_pass(self,course_setup,case):
        index_page = course_setup[1]
        # 1.加入课程--输入验证码--点击确认
        index_page.add_course(case['verificate_code'])
        expected = case["expected"]
        # 2.获取元素的属性
        time.sleep(2)
        res = index_page.get_add_toast()
        try:
            assert res == expected
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))

    @pytest.mark.parametrize('case',course_data.add_course_data_fail)
    def test_add_course_fail(self,course_setup,case):
        index_page = course_setup[1]
        # 1.加入课程--输入验证码--点击确认
        index_page.add_course(case['verificate_code'])
        expected = case["expected"]
        # 2.获取元素的属性
        time.sleep(2)
        res = index_page.get_add_toast()
        try:
            assert res == expected
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))
            index_page.close_add_toast()














