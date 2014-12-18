# -*- coding: UTF-8 -*-
'''
Created on Nov. 17, 2014

@author: guoyuling
'''
import time

import base
from myoffice_page import MyOfficePage
import unittest, time, re,random
from selenium.common.exceptions import NoSuchElementException

#创建科目、类目、考点
class OrgExamCreateListPage(base.Base):

    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')

    def open(self):
        c = MyOfficePage(self.dr, self.cfg)
        c.open_exam()
    #创建科目
    def click_create_sub(self):
        self.dr.driver.find_element(cfg.get('exam', 'new_subject_by'), \
        cfg.get('exam', 'new_subject_id')).click()
        driver.implicitly_wait(10)
    #创建类目
    def click_create_cate(self):
        self.dr.driver.find_element_by_link_text(u"类目管理").click()
        self.dr.driver.implicitly_wait(10)

    #新建考点
    def click_point_page(self):
        self.dr.driver.find_element_by_link_text(u"考点库").click()



#输入科目，类目，考点相关信息   
class OrgExamInputListPage(base.Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')

    #输入科目名称,分成两个方法为了验证
    def clear_sub(self):
        sub_c = self.dr.driver.find_element(cfg.get('exam', 'sub_name_by'), \
            cfg.get('exam', 'sub_name'))
        sub_c.clear()

    def input_sub(self, subject_name):
        sub_c = self.dr.driver.find_element(cfg.get('exam', 'sub_name_by'), \
            cfg.get('exam', 'sub_name'))
        sub_c.clear()
        sub_c.send_keys(subject_name)

    #填写类目名称
    def input_cname(self, cate_name):
        c_input = self.dr.driver.find_element(cfg.get('exam', 'cate_addname_by'), \
            cfg.get('exam', 'cate_addname'))
        c_input.clear()
        c_input.send_keys(cate_name)
        

    #填写类目描述
    def input_cdetail(self, cate_detail):
        cd_input = self.dr.driver.find_element(cfg.get('exam', 'cate_desname_by'), \
            cfg.get('exam', 'cate_desname'))
        cd_input.clear()
        cd_input.send_keys(cate_detail)
        driver.implicitly_wait(10)

    #输入考点名称
    def input_pname(self, point_name):
        p_input = self.dr.driver.find_element(cfg.get('exam', 'point_addname_by'), \
            cfg.get('exam', 'point_addname'))
        p_input.clear()
        p_input.send_keys(point_name)

    #输入考点介绍
    def input_pdetail(self, point_detail):
        pd_input = self.dr.driver.find_element(cfg.get('exam', 'point_desname_by'), \
            cfg.get('exam', 'point_desname'))
        pd_input.clear()
        pd_input.send_keys(point_detail)
        self.dr.driver.implicitly_wait(10)

    #填写其他推荐
    def input_other_groom(self, other_groom):
        og_input = self.dr.driver.find_element(cfg.get('exam', 'point_othergroom_by'), \
            cfg.get('exam', 'point_othergroom'))
        og_input.clear()
        og_input.send_keys(other_groom)
        self.dr.driver.implicitly_wait(10)

#确认按钮
class OrgExamiOkListPage(object):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')

    #新建科目OK
    def click_addsub_ok(self):
        self.dr.driver.find_element(cfg.get('exam', 'sub_ok_by'), \
                            cfg.get('exam', 'sub_ok_xpath')).click()
        self.dr.driver.implicitly_wait(30)
    
    #确认删除科目
    def click_delsub_ok(self):
        self.dr.driver.find_element(cfg.get('exam', 'sub_delok_by'), \
            cfg.get('exam', 'sub_delok_xpath')).click()
        self.dr.driver.implicitly_wait(10)
    
    #确认新建类目
    def click_addcate_ok(self):
        self.dr.driver.find_element(cfg.get('exam', 'cate_oknew_button_by'),\
            cfg.get('exam', 'cate_oknew_button')).click()
        self.dr.driver.implicitly_wait(10)

    #确认删除类目
    def click_delcate_ok(self):
        self.dr.driver.find_element(cfg.get('exam', 'cate_oknew_button_by'), \
            cfg.get('exam', 'cate_oknew_button')).click()
        self.dr.driver.implicitly_wait(10)

    #确认添加考点
    def click_addpoint_ok(self):
        self.dr.driver.find_element(cfg.get('exam', 'point_okbotton_by'), \
            cfg.get('exam', 'point_okbotton')).click()
        self.dr.driver.implicitly_wait(10)
    
    #确认删除考点
    def click_delpoint_ok(self):
        self.dr.driver.find_element(cfg.get('exam', 'point_delokbot_by'), \
            cfg.get('exam', 'point_delokbot_xpath')).click()
        self.dr.driver.implicitly_wait(10)

    #确认添加课程
    def click_addcourse_ok(self):
        self.dr.driver.find_element(cfg.get('exam', 'point_ok_lessbotton_by'), \
            cfg.get('exam', 'point_ok_lessbotton')).click()
        self.dr.driver.implicitly_wait(10)

class OrgExamSearchListPage(object):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')

    #第一个科目外面的框
    def click_sub_big1(self):
        self.dr.driver.find_element(cfg.get('exam', 'sub_big1_by'), \
                                cfg.get('exam', 'sub_big1_xpath')).click()
    #第一个科目
    def click_sub_small1(self):
        self.dr.driver.find_element(cfg.get('exam', 'sub_small1_by'), \
                                cfg.get('exam', 'sub_small1_xpath')).click()

    #第二个科目外面的框
    def click_sub_big2(self):
        self.dr.driver.find_element(cfg.get('exam', 'sub_big2_by'), \
                                cfg.get('exam', 'sub_big2_xpath')).click()

    #第二个科目
    def click_sub_small2(self):
        self.dr.driver.find_element(cfg.get('exam', 'sub_small2_by'), \
                                cfg.get('exam', 'sub_small2_xpath')).click()
    #删除科目
    def click_sub_del1(self):
        self.dr.driver.find_element(cfg.get('exam', 'sub_del1_by'), \
                                cfg.get('exam', 'sub_del1_xpath')).click()
    #删除另一个科目
    def click_sub_del2(self):
        self.dr.driver.find_element(cfg.get('exam', 'sub_del2_by'), \
                                cfg.get('exam', 'sub_del2_xpath')).click()

    #新增类目
    def click_create(self):
        self.dr.driver.find_element(cfg.get('exam', 'cate_newcateid_by'), \
            cfg.get('exam', 'cate_newcateid')).click()
        self.dr.driver.implicitly_wait(10)

    #编辑类目
    def click_modify_cate(self):
        self.dr.driver.find_element(cfg.get('exam', 'cate_mod_by'), \
            cfg.get('exam','cate_mod_xpath')).click()
       
    #删除类目
    def click_delete_cate(self):
        self.dr.driver.find_element(cfg.get('exam', 'cate_del_by'), \
            cfg.get('exam', 'cate_del_xpath')).click()
        self.dr.driver.implicitly_wait(10)

    #新建考点
    def click_create_point(self):
        self.dr.driver.find_element(cfg.get('exam', 'point_addnewid_by'), \
            cfg.get('exam', 'point_addnewid')).click()

    
    #加课程推荐
    def click_add_course(self):
        self.dr.driver.find_element_by_link_text("+").click()

    #选择两个课程
    def click_add_courses(self):
        self.dr.driver.find_element(cfg.get('exam', 'point_address_by'), \
            cfg.get('exam', 'point_address_xpath1')).click()
        self.dr.driver.implicitly_wait(10)
        self.dr.driver.find_element(cfg.get('exam', 'point_address_by'), \
            cfg.get('exam', 'point_address_xpath2')).click()
        self.dr.driver.implicitly_wait(10)
    
    #编辑考点
    def click_modify_point(self):
        self.dr.driver.find_element(cfg.get('exam', 'point_edit_by'), \
            cfg.get('exam', 'point_edit')).click()
        self.dr.driver.implicitly_wait(10)

    #删除考点
    def click_delete_point(self):
        self.dr.driver.find_element(cfg.get('exam', 'point_delete_by'), \
            cfg.get('exam', 'point_delete_xpath')).click()
        self.dr.driver.implicitly_wait(10)
    #
    def click_lesdel_point(self):
        self.dr.driver.find_element(cfg.get('exam', 'point_lesdel_botton_by'), \
            cfg.get('exam','point_lesdel_botton')).click()
        driver.implicitly_wait(10)

    