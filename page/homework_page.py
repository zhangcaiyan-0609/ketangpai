"""
File name: homework_page.py.py
Author: caiyan
Email: caiyanyifei@163.com
Time : 2020/10/23 11:36 上午
"""
from selenium.webdriver.common.by import By
from common.base_page import BasePage
import pyautogui
import time


class HomeworkPage(BasePage):

    # 作业页面的定位表达式
    homework_locator = (By.XPATH,"(//h3[@class='work-title '])[1]")
    handup_locator = (By.XPATH, "//a[text()='提交']")
    add_homework_file_locator = (By.XPATH,"//a[@class='sc-btn webuploader-container']")
    news_locator = (By.XPATH,"//span[@class='s2']")
    score_locator = (By.XPATH,"//p[@class='score fr']")
    homework_status_locator = (By.XPATH,"//span[@class='ywc']")
    readd_handup_locator = (By.XPATH,"(//a[text()='更新提交'])[1]")
    second_readd_handup_locator = (By.XPATH,"(//a[text()='更新提交'])[2]")
    readd_btn_locator = (By.XPATH,"//div[@id='update-pop']//a[text()='确定']")
    delete_locator = (By.XPATH,"(//a[text()='删除'])[1]")
    homework_toast_locator = (By.XPATH,"//div[@class='weui_dialog_bd']")
    close_toast_locator = (By.XPATH,"//a[text()='知道了']")
    label_loactor = (By.XPATH,"(//a[@class='side-button'])[1]")
    personal_locator = (By.XPATH,"//b[text()='私信']")
    # 以下为作业页面的操作
    # 进入作业
    def take_homework(self):
        self.click_element(self.homework_locator,"作业_点击上传")

    # 上传作业的附件
    def add_load_file(self):
        files = ["/Users/zhangcaiyan/Desktop/log/test.py","/Users/zhangcaiyan/Desktop/log/web.py"]
        self.load_file(self.add_homework_file_locator,*files)
    # 点击提交作业
    def handup_homework(self):
        self.click_element(self.handup_locator,"作业_点击提交")
    # 获取作业的状态
    def get_homework_status(self):
        res = self.get_element_text(self.homework_status_locator,"作业_获取作业的状态")
        return res
    # 获取作业的留言
    def get_homework_news(self):
        res = self.get_element_text(self.news_locator,"作业_获取作业的留言")
        return res
    # 获取作业的分数
    def get_homework_score(self):
        res = self.get_element_attribute(self.score_locator,"span","作业_获取成绩")
        return res
    # 更新提交作业
    def readd_homework(self):
        self.click_element(self.readd_handup_locator,"作业_更新提交")
        time.sleep(3)
        self.click_element(self.readd_btn_locator,"更新作业_点击确定")
        time.sleep(2)
        self.add_load_file()
        time.sleep(1)
        self.click_element(self.second_readd_handup_locator,"作业_点击更新提交")
        time.sleep(2)
    # 获取弹窗的文本
    def get_homework_toast(self):
        res = self.get_element_text(self.homework_toast_locator,"作业_弹窗文本")
        return res
    # 关闭弹窗
    def close_homework_toast(self):
        self.click_element(self.close_toast_locator,"作业弹窗_关闭弹窗")
        self.driver.refresh()
    # 点击进入私信
    def take_personal(self):
        self.click_element(self.label_loactor,"作业_点击菜单")
        time.sleep(5)
        self.switch_to_window(self.personal_locator,"作业_切换到私信")



