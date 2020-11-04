
"""
File name: Index_page.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/9/27 11:43 上午
"""
from selenium.webdriver.common.by import By
from common.base_page import BasePage
import time
class IndexPage(BasePage):
    quit_login_locator = (By.XPATH,'//a[text()="退出账户"]')
    loc_user_info = (By.XPATH,"//img[@class='avatar']")
    course_locator = (By.XPATH,"//span[text()='+ 创建/加入课程']")
    add_course_locator = (By.XPATH,"//a[text()='加入课程']")
    verification_code_locator =(By.XPATH,"//div[@class='chuangjiankccon']//input[@type='text']")
    password_locator = (By.XPATH,"//input[@type='password']")
    join_btn_locator = (By.XPATH,"//li[@class='cjli2']")
    add_course_btn_locator = (By.XPATH,"//a[text()='加入']")
    course_toast_locator =(By.XPATH,"//div[@class='gTips']")
    close_add_toast_locator= (By.XPATH,"//li[@class='cjli1']")
    choose_course_locator = (By.XPATH,"//div[@id='viewer-container-toplists']")
    drop_course_locator = (By.XPATH,"//a[text()='退课']")
    more_locator = (By.XPATH,"//span[text()='更多']")
    take_course_locator = (By.XPATH,"//a[text()='python-web项目实战- 考核项目']")
    homework_title_locator = (By.XPATH,"//a[text()='作业']")
    drop_btn_locator = (By.XPATH,"//li[@class='dli2']//a[text()='退课']")
    close_win_locator = (By.XPATH,"//a[@class='layui-layer-ico layui-layer-close layui-layer-close2']")
    login_locator = (By.XPATH,"//a[@class='login']")
    homework_locator = (By.XPATH, "(//h3[@class='work-title '])[1]")

    def is_login(self):
        try:
            self.get_element(self.loc_user_info,"首页_账户")
        except AssertionError as e:
            return False
        else:
            return True

    def add_course(self,verificate_code):
        # 点击加入课程--输入验证码
        self.click_element(self.course_locator,"首页_点击/创建课程")
        self.click_element(self.add_course_locator,"首页_点击加入课程")
        # self.clear_element(self.verification_code_locator,"加入课程_清除验证码")
        self.input_text(self.verification_code_locator,verificate_code,"首页_加入课程_输入验证码")
        res = self.wait_element_clickable(self.join_btn_locator,"加入课程_点击确定")
        res.click()

    def get_add_toast(self):
        res = self.get_element_text(self.course_toast_locator,"加入课程_弹窗提示")
        return res

    def close_add_toast(self):
        self.click_element(self.close_add_toast_locator,"加入课程_取消弹窗")

    def choose_course(self):
        self.get_element(self.choose_course_locator,"首页_选定课程")

    def take_course(self):
        # 进入班级
        self.click_element(self.take_course_locator,"首页_点击进入班级")
        self.click_element(self.homework_title_locator,"作业_切换到作业")

    def drop_course(self,password):
        # 点击更多--退课-输入验证码--点击确定
        self.click_element(self.more_locator,"首页_点击更多")
        self.click_element(self.drop_course_locator,"首页_点击退课")
        self.input_text(self.password_locator,password,"首页_退课_输入密码")
        self.click_element(self.drop_btn_locator,"退课_点击退课")

    def quit_login(self):
        # 退出登录--关闭弹窗
        self.click_element(self.loc_user_info,"首页_账户")
        self.click_element(self.quit_login_locator, "首页_点击退出")
        self.click_element(self.close_win_locator, "登录_关闭弹窗")
        self.click_element(self.login_locator, "登录_点击登录")







