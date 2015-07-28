# -*- coding: UTF-8 -*-
'''
Created on 2014-12-20

@author: guoyuling
'''
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
        

    #试卷库
    def click_exampaper(self):
        self.dr.find_element_by_link_text(u"试卷库").click()

    #试题库
    def click_questions(self):
        self.dr.find_element_by_link_text(u"试题库").click()

    #学员管理
    def click_stu_manage(self):
        self.dr.find_element(self.cfg.get('exam', 'stu_manage_by'), \
            self.cfg.get('exam', 'stu_manage')).click()

    #创建科目
    def click_create_sub(self):
        self.dr.find_element(self.cfg.get('exam', 'new_subject_by'), \
        	self.cfg.get('exam', 'new_subject_id')).click()
        

    #类目管理
    def click_cate_page(self):
        self.dr.find_element_by_link_text(u"类目管理").click()
        

    #考点库
    def click_point_page(self):
        self.dr.find_element_by_link_text(u"考点库").click()
    
     #输入科目名称,分成两个方法为了验证
    def clear_sub(self):
        sub_c = self.dr.find_element(self.cfg.get('exam', 'sub_name_by'), \
            self.cfg.get('exam', 'sub_name'))
        sub_c.clear()

    def input_sub(self, subject_name):
        sub_c = self.dr.find_element(self.cfg.get('exam', 'sub_name_by'), \
            self.cfg.get('exam', 'sub_name'))
        sub_c.clear()
        sub_c.send_keys(subject_name)

    #显示科目边框
    def click_sub_big(self):
        self.dr.execute_script("return $('.u-exam-btns').attr('style','display:block')")

    #修改第一个科目
    def click_sub_edit(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('exam', 'sub_edit_by'), \
            self.cfg.get('exam', 'sub_edit')).click()
                  
    #删除最后一个科目
    def click_sub_del(self):
        time.sleep(2)
        self.dr.find_elements(self.cfg.get('exam', 'sub_del_by'), \
        	self.cfg.get('exam', 'sub_del'))[-1].click()
            
    #确认删除科目
    def click_delsub_ok(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_delok_by'), \
            self.cfg.get('exam', 'sub_delok_xpath')).click()
        

    #新建科目OK
    def click_addsub_ok(self):
        self.dr.find_element(self.cfg.get('exam', 'sub_ok_by'), \
        	self.cfg.get('exam', 'sub_ok')).click()
