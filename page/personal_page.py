"""
File name: personal_page.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/30 6:20 下午
"""
from selenium.webdriver.common.by import By
from common.base_page import BasePage
import pyautogui
import time


class PersonalPage(BasePage):
    search_ele_locator = (By.XPATH,"//input[@placeholder='搜索学号、姓名']")
    refuse_ele_locator =(By.XPATH,"//div[@class='refuse']")
    inputnews_ele_locator = (By.XPATH,"//textarea[@class='ps-container']")
    send_ele_locator = (By.XPATH,"//a[text()='发送']")
    inputfile_locator = (By.XPATH,"//a[@id='upload']")
    search_list_locator = (By.XPATH,"//div[@class='search-list']")
    toast_locator = (By.XPATH,"//div[@class='gTips']")
    current_connect_locator = (By.XPATH,"//a[@class='lately active']")
    pass_list_locator =(By.XPATH,"(//div[@class='m-list']//ul//li)[1]")
    close_toast_locator =(By.XPATH,"//i[@class='icon icon-notify-close']")
    search_name_locator = (By.XPATH,"(//span[@title='小简'])[1]")
    search_fail_locator =(By.XPATH,"//p[@class='noResults']")
    send_context_locator = (By.XPATH,"(//div[@class='text'])[last()]")
    fail_list_locator = (By.XPATH,"(//div[@class='m-list']//ul//li)[last()]")
    send_file_content_locator = (By.XPATH,"(//a[@class='fileext preview'])[last()]")
    # 屏蔽/取消屏蔽
    def refuse(self):
        self.click_element(self.refuse_ele_locator,"私信_点击屏蔽")

    # 发送消息
    def send_news(self,message):
        self.input_text(self.inputnews_ele_locator,message,"私信_发送消息")
        self.click_element(self.send_ele_locator,"私信_点击发送")

    # 发送附件
    def send_file(self):
        self.click_element(self.inputfile_locator,"私信_点击附件")
        file = "/Users/zhangcaiyan/Desktop/log/test.py"
        pyautogui.write('{}'.format(file))
        time.sleep(3)
        pyautogui.press("enter", 2)
        time.sleep(4)

    # 获取搜索结果
    def get_search_code(self,code):
        self.clear_element(self.search_ele_locator, "私信_清除搜索")
        self.input_text(self.search_ele_locator, code, "私信_点击搜索")
        res = self.get_element_text(self.search_list_locator,"私信_获取搜索结果")
        return True

    def get_search_name(self,name):
        self.clear_element(self.search_ele_locator,"私信_清除搜索")
        self.input_text(self.search_ele_locator,name,"私信_点击搜索")
        res = self.get_element_attribute(self.search_name_locator,"title","私信_获取搜索结果")
        return res

    def get_search_error(self,code):
        self.clear_element(self.search_ele_locator, "私信_清除搜索")
        self.input_text(self.search_ele_locator, code, "私信_点击搜索")
        res = self.get_element_text(self.search_fail_locator, "私信_获取搜索结果")
        return res

    # 获取屏蔽弹窗
    def get_refuse_toast(self):
        res = self.get_element_text(self.toast_locator,"私信_屏蔽弹窗")
        return res

    # 关闭弹窗
    def close_toast(self):
        self.click_element(self.close_toast_locator,"私信_关闭弹窗")

    # 获取发送消息的弹窗
    def get_send_news_toast(self):
        res = self.get_element_text(self.toast_locator,"私信_发送消息弹窗")
        return res
    # 获取页面上的内容
    def get_send_content(self):
        res = self.get_element_text(self.send_context_locator,"私信_发送的内容")
        return res
    # 获取页面上附件的名字
    def get_send_file_name(self):
        res = self.get_element_text(self.send_file_content_locator,"私信_发送附件的名字")
        return  res
    # 点击好友列表，选择私信的人
    def choose_pass_people(self):
        self.click_element(self.current_connect_locator,"私信_点击最近联系人")
        self.click_element(self.pass_list_locator,"私信_点击选择私信的人")
    def choose_fail_people(self):
        self.click_element(self.current_connect_locator, "私信_点击最近联系人")
        self.click_element(self.fail_list_locator, "私信_点击选择私信的人")

