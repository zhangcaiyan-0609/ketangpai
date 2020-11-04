"""
File name: test_04homework.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/23 11:19 上午
"""
"""
测试上传作业--查看作业状态的前置
前置条件
1.打开浏览器，访问登录页面
2.需要登录
3.选定课程--进入班级
4.切换到作业--点击上传作业
执行用例
操作步骤
0。首先获取作业的状态，从而判断是首次提交还是更新提交
1。添加作业文件(图片，文档，py文件，zip包)
2。点击提交
4. 更新提交
5。添加作业文件
6.点击更新提交

校验：
1。能否添加文件成功
3。能否上传成功
4。更新提交是否成功 
5。作业状态的变化
6。获取作业的留言

后置条件
关闭浏览器
"""
import pytest
from casedatas import homework_data
from common.handle_log import log
import time


class TestHomework:
    # 作业首次提交
    @pytest.mark.parametrize('case', homework_data.homework_data_success)
    def test_homework_pass(self, case, homework_setup):
        index_page = homework_setup[0]
        homework_page = homework_setup[1]
        start_status = homework_setup[2]
        if start_status == "未完成":
            # 1.点击作业上传
            homework_page.add_load_file()
            time.sleep(10)
            homework_page.handup_homework()
            expected = case["expected"]
            # 2.获取弹窗的文本
            res = homework_page.get_homework_toast()
            time.sleep(2)
            # 关闭弹窗
            homework_page.close_homework_toast()
            time.sleep(2)
            # 3.获取作业的状态
            # end_status = homework_page.get_homework_status()
            # 4.断言
            try:
                assert res == expected
            except AssertionError as e:
                log.error("用例--{}--执行失败".format(case['title']))
                log.exception(e)
                raise e
            else:
                log.info("用例--{}--执行成功".format(case['title']))
        else:
            pass
    # 作业更新提交
    @pytest.mark.parametrize('case', homework_data.homework_data_readd)
    def test_homework_readd(self, case, homework_setup):
        index_page = homework_setup[0]
        homework_page = homework_setup[1]
        start_status = homework_setup[2]
        if start_status == "已完成":
            # 1.点击作业上传
            homework_page.readd_homework()
            expected = case["expected"]
            # 2.获取弹窗的文本
            res = homework_page.get_homework_toast()
            time.sleep(2)
            # 关闭弹窗
            homework_page.close_homework_toast()
            # 3.断言
            try:
                assert res == expected
            except AssertionError as e:
                log.error("用例--{}--执行失败".format(case['title']))
                log.exception(e)
                raise e
            else:
                log.info("用例--{}--执行成功".format(case['title']))
        else:
            pass
    # 获取作业的留言
    @pytest.mark.parametrize('case', homework_data.homework_data_news)
    def test_homework_news(self, case, homework_setup):
        index_page = homework_setup[0]
        homework_page = homework_setup[1]
        # 1.点击作业上传
        expected = case["expected"]
        # 2.获取作业的留言
        news = homework_page.get_homework_news()
        # 3.断言
        try:
            assert news == expected
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行成功".format(case['title']))
