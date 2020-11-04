"""
File name: conftest.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/12 11:02 上午
"""
import pytest
from selenium.webdriver import Chrome
from common.handle_config import conf
from page.Index_page import IndexPage
from page.login_page import LoginPage
from page.homework_page import HomeworkPage
from page.personal_page import PersonalPage
from selenium import webdriver
import time
import os
#读取配置文件中的配置，判断是否是以无头浏览器模式运行
#chromedriver = "/usr/local/bin/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver


# 创建driver对象
def create_dirver():
    boll = conf.getboolean("run","headless")
    if boll:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options,executable_path="/usr/local/bin/chromedriver")
    else:
        driver = Chrome(executable_path="/usr/local/bin/chromedriver")
    return driver
# 登录页面的前置
@pytest.fixture(scope="class")
def login_setup():
    driver = create_dirver()
    driver.implicitly_wait(15)
    driver.get(conf.get('env', 'base_url') + conf.get('env', 'url_path'))
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page,index_page
    driver.quit()

# 课堂主页的前置
@pytest.fixture(scope="class")
def course_setup():
    driver = create_dirver()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get(conf.get('env', 'base_url') + conf.get('env', 'url_path'))
    login_page = LoginPage(driver)
    # 登录
    login_page.login(conf.get("test_data", "phone"), conf.get("test_data", "pwd"))
    # 创建首页对象
    index_page = IndexPage(driver)
    yield login_page,index_page
    driver.quit()

# 作业页面的前置
@pytest.fixture(scope="class")
def homework_setup():
    driver = create_dirver()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get(conf.get('env','base_url') + conf.get("env","url_path"))
    login_page = LoginPage(driver)
    # 登录
    login_page.login(conf.get("test_data", "phone"), conf.get("test_data", "pwd"))
    # 创建首页对象
    index_page = IndexPage(driver)
    # 选定课程进入班级,切换到作业，进入到第一个作业

    index_page.add_course("P69UVV")
    index_page.take_course()
    homework_page = HomeworkPage(driver)
    homework_page.take_homework()
    # 获取作业的状态
    start_status = homework_page.get_homework_status()
    yield index_page,homework_page,start_status
    driver.quit()

# 私信页面的前置
@pytest.fixture(scope='class')
def personal_setup():
    driver = create_dirver()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get(conf.get('env', 'base_url') + conf.get("env", "url_path"))
    login_page = LoginPage(driver)
    # 登录
    login_page.login(conf.get("test_data", "phone"), conf.get("test_data", "pwd"))
    # 创建首页对象
    index_page = IndexPage(driver)
    # 进入班级
    index_page.take_course()
    time.sleep(3)
    # 创建班级作业对象
    homework_page = HomeworkPage(driver)
    # 进入私信
    homework_page.take_personal()
    # 创建私信对象
    personal_page = PersonalPage(driver)
    yield homework_page,personal_page
    driver.quit()







