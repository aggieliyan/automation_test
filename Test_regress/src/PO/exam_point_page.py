# -*- coding: UTF-8 -*-
'''
Created on 2014-12-20

@author: guoyuling
'''
import time

from selenium.webdriver.support.wait import WebDriverWait

import base
from myoffice_page import MyOfficePage

class ExamPointListPage(base.Base):

    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
    
    #新建考点
    def click_create_point(self):
        self.dr.find_element(self.cfg.get('exam', 'point_addnewid_by'), \
            self.cfg.get('exam', 'point_addnewid')).click()

    
    #加课程推荐
    def click_add_course(self):
        self.dr.find_element_by_link_text("+").click()

    #选择两个课程
    def click_add_courses(self):
        self.dr.find_element(self.cfg.get('exam', 'point_address_by'), \
            self.cfg.get('exam', 'point_address_xpath1')).click()
        
        self.dr.find_element(self.cfg.get('exam', 'point_address_by'), \
            self.cfg.get('exam', 'point_address_xpath2')).click()
        
    #输入考点名称
    def input_pname(self, point_name):
        time.sleep(3)
        p_input = self.dr.find_element(self.cfg.get('exam', 'point_addname_by'), \
            self.cfg.get('exam', 'point_addname'))
        p_input.clear()
        p_input.send_keys(point_name)

    #输入考点介绍
    def input_pdetail(self, point_detail):
        pd_input = self.dr.find_element(self.cfg.get('exam', 'point_desname_by'), \
            self.cfg.get('exam', 'point_desname'))
        pd_input.clear()
        pd_input.send_keys(point_detail)
        

    #填写其他推荐
    def input_other_groom(self, other_groom):
        og_input = self.dr.find_element(self.cfg.get('exam', 'point_othergroom_by'), \
            self.cfg.get('exam', 'point_othergroom'))
        og_input.clear()
        og_input.send_keys(other_groom)
        

    #确认添加考点
    def click_addpoint_ok(self):
        self.dr.find_element(self.cfg.get('exam', 'point_okbotton_by'), \
            self.cfg.get('exam', 'point_okbotton')).click()
        
    
    #确认删除考点
    def click_delpoint_ok(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('exam', 'point_delokbot_by'), \
            self.cfg.get('exam', 'point_delokbot_xpath')).click()
        

    #确认添加课程
    def click_addcourse_ok(self):
        self.dr.find_element(self.cfg.get('exam', 'point_ok_lessbotton_by'), \
            self.cfg.get('exam', 'point_ok_lessbotton')).click()
        

    #编辑考点
    def click_modify_point(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('exam', 'point_edit_by'), \
            self.cfg.get('exam', 'point_edit')).click()
        

    #删除考点
    def click_delete_point(self):
        self.dr.find_element(self.cfg.get('exam', 'point_delete_by'), \
            self.cfg.get('exam', 'point_delete_xpath')).click()
        
    #
    def click_lesdel_point(self):
        self.dr.find_element(self.cfg.get('exam', 'point_lesdel_botton_by'), \
            self.cfg.get('exam','point_lesdel_botton')).click()
        
