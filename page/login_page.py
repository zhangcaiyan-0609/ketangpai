
"""
File name: login_page.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/9/27 11:05 上午
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handle_config import conf
from common.base_page import BasePage
import time
class LoginPage(BasePage):
    # 手机号输入框
    input_phone_locator =(By.XPATH,"//input[@name='account']")
    # 密码输入框
    password_locator =(By.XPATH,"//input[@name='pass']")
    # 登陆按钮
    login_btn_locator = (By.XPATH,"//div[@class='padding-cont pt-login']//a[text()='登录']")
    # 登陆页面错误
    page_error_locator =(By.XPATH,'//p[@class="error-tips"]')

    loc_user_info_ = (By.XPATH, "//img[@class='avatar']")

    def __int__(self,driver):
        super.__init__(driver)
        self.driver.get(conf.get("env","base_url")+conf.get("env","url_path"))
        self.driver.implicitly_wait(15)

    def login(self,phone,pwd):
        """
        :param phone:
        :param pwd:
        :return:
        """
        # 1 输入账号
        self.clear_element(self.input_phone_locator,"登录页面_清空账户")
        self.input_text(self.input_phone_locator,phone,"登录页面_输入手机号")
        # 2 输入密码
        self.clear_element(self.password_locator,"登录页面_清空密码")
        self.input_text(self.password_locator,pwd,"登录页面_输入密码")
        # 3 点击登录
        self.click_element(self.login_btn_locator,"登录页面_点击登录")
    def max_win(self):
        self.driver.maximize_window()

    def is_login(self):
        try:
            self.get_element(self.loc_user_info,"首页_账户")
        except AssertionError as e:

            return False
        else:
            return True

    def get_page_error_info(self):
        # 获取页面上的错误提示
        res = self.get_element_text(self.page_error_locator,"登录页面_错误提示")
        return res

    def reset_login_page(self):
        self.driver.get(conf.get('env','base_url')+conf.get('env','url_path'))
