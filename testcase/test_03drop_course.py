
"""
File name: test_03drop_course.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/22 9:50 下午
"""
import pytest
from casedatas import course_data
from common.handle_log import log
import time
class TestDropCourse:
    @pytest.mark.parametrize('case',course_data.drop_course_data)
    def test_drop_course_pass(self,course_setup,case):
        index_page = course_setup[1]
        # 1.退课
        index_page.choose_course()
        index_page.drop_course(case["password"])
        expected = case["expected"]
        # 2.获取弹窗的文本
        res = index_page.get_add_toast()
        time.sleep(5)
        # 3.断言
        try:
            assert res == expected
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))

