"""
File name: test_05personal.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/11/1 4:02 下午
"""
import pytest
from casedatas import personal_data
from common.handle_log import log
import time



class TestPersonal:

    # 测试屏蔽功能
    @pytest.mark.parametrize('case', personal_data.sheild_data)
    def test_sheild(self, case, personal_setup):
        homework_page = personal_setup[0]
        personal_page = personal_setup[1]
        personal_page.choose_pass_people()
        # 1.点击屏蔽
        personal_page.refuse()
        # 2.获取屏蔽弹窗
        res = personal_page.get_refuse_toast()
        # 3.断言
        try:
            assert res == case["expected"]
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))
            personal_page.close_toast()

    # 测试搜索功能
    @pytest.mark.parametrize('case',personal_data.search_data_by_code)
    def test_search_code(self,case,personal_setup):
        homework_page = personal_setup[0]
        personal_page = personal_setup[1]
        #1.搜索
        res = personal_page.get_search_code(case['code'])
        #2.断言
        try:
            assert res
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))

    @pytest.mark.parametrize('case',personal_data.search_data_by_name)
    def test_search_name(self,case,personal_setup):
        homework_page = personal_setup[0]
        personal_page = personal_setup[1]
        #1.搜索
        res = personal_page.get_search_name(case['code'])
        #2.断言
        try:
            assert res == case['code']
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))

    @pytest.mark.parametrize('case',personal_data.search_data_error)
    def test_search_error(self,case,personal_setup):
        homework_page = personal_setup[0]
        personal_page = personal_setup[1]
        # 1.搜索
        res = personal_page.get_search_error(case['code'])
        # 2.断言
        try:
            assert res == case["expected"]
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))
    # 测试发送消息与附件
    @pytest.mark.parametrize("case", personal_data.personal_data_is_none)
    def test_send_new_is_none(self, case, personal_setup):
        homework_page = personal_setup[0]
        personal_page = personal_setup[1]
        # 1.选择好友
        personal_page.choose_pass_people()
        time.sleep(2)
        expected = case["expected"]
        # 2,定位输入框，点击发送
        personal_page.send_news(case["message"])
        # 3.断言
        res = personal_page.get_send_news_toast()
        try:
            assert res == expected
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))

    @pytest.mark.parametrize('case',personal_data.personal_data_send_success)
    def test_send_news_success(self,case,personal_setup):
        homework_page = personal_setup[0]
        personal_page = personal_setup[1]
        # 1.选择好友
        personal_page.choose_pass_people()
        time.sleep(2)
        # 2,定位输入框，点击发送
        personal_page.send_news(case["message"])
        # 3.获取页面的上发送内容
        res = personal_page.get_send_content()
        # 4.断言
        try:
            assert res == case["message"]
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))

    @pytest.mark.parametrize('case', personal_data.personal_data_send_fail)
    def test_send_news_fail(self, case, personal_setup):
        homework_page = personal_setup[0]
        personal_page = personal_setup[1]
        # 1.选择好友
        personal_page.choose_fail_people()
        time.sleep(2)
        # 2,定位输入框，点击发送
        personal_page.send_news(case["message"])
        # 3.获取页面的上发送内容
        res = personal_page.get_send_news_toast()
        # 4.断言
        try:
            assert res == case["expected"]
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))

    @pytest.mark.parametrize('case', personal_data.personal_data_send_file)
    def test_send_files(self, case, personal_setup):
        homework_page = personal_setup[0]
        personal_page = personal_setup[1]
        # 1.选择好友
        personal_page.choose_pass_people()
        time.sleep(2)
        # 2.上传附件
        personal_page.send_file()
        # 3.获取页面的上发送内容
        res = personal_page.get_send_file_name()
        # 4.断言
        try:
            assert res == case["expected"]
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))
