# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import base
from myoffice_page import MyOfficePage

class SubjectListPage(base.Base):


    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')

    def open(self):
        self.dr.get("%sexam/" %(self.base_url))
        self.dr.implicitly_wait(10)

    #试卷库
    def click_exampaper(self):
        self.dr.find_element_by_link_text(u"试卷库").click()

    #创建科目
    def click_create_sub(self):
        self.dr.find_element(self.cfg.get('exam', 'new_subject_by'), \
        	self.cfg.get('exam', 'new_subject_id')).click()
        self.dr.implicitly_wait(10)

    #类目管理
    def click_cate_page(self):
        self.dr.find_element_by_link_text(u"类目管理").click()
        self.dr.implicitly_wait(10)

    #考点库
    def click_point_page(self):
        self.dr.find_element_by_link_text(u"考点库").click()
    
     #输入科目名称,分成两个方法为了验证
    def clear_sub(self):
        sub_c = self.dr.find_element(self.cfg.get('exam', 'sub_name_by'), \
            self.cfg.get('exam', 'sub_name'))
        sub_c.clear()

    def input_sub(self):
        sub_c = self.dr.find_element(self.cfg.get('exam', 'sub_name_by'), \
            self.cfg.get('exam', 'sub_name'))
        sub_c.clear()
        sub_c.send_keys(subject_name)

    #第一个科目外面的框
    def click_sub_big1(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_big1_by'), \
        	self.cfg.get('exam', 'sub_big1_xpath')).click()
    #第一个科目
    def click_sub_small1(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_small1_by'), \
        	self.cfg.get('exam', 'sub_small1_xpath')).click()

    #第二个科目外面的框
    def click_sub_big2(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_big2_by'), \
        	self.cfg.get('exam', 'sub_big2_xpath')).click()

    #第二个科目
    def click_sub_small2(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_small2_by'), \
        	self.cfg.get('exam', 'sub_small2_xpath')).click()
    #删除科目
    def click_sub_del1(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_del1_by'), \
        	self.cfg.get('exam', 'sub_del1_xpath')).click()
    #删除另一个科目
    def click_sub_del2(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_del2_by'), \
        	self.cfg.get('exam', 'sub_del2_xpath')).click()

    #确认删除科目
    def click_delsub_ok(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_delok_by'), \
            self.cfg.get('exam', 'sub_delok_xpath')).click()
        self.dr.implicitly_wait(10)

    #新建科目OK
    def click_addsub_ok(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_ok_by'), \
        	self.cfg.get('exam', 'sub_ok')).click()
        self.dr.implicitly_wait(30)
    



    #试题库
    def click_examquestion(self):
        pass

    #学员管理
    def click_stu_manage(self):
        pass