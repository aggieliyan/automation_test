# -*- coding: UTF-8 -*-
'''
Created on Jun 2, 2012
@author: yilulu
modified on Dec. 24, 2014
@author: liuhongjiao
added: manage_course_numdetail
       manage_course_num
       buy_open_num
'''

import time, random, unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from PO.org_student_page import OrgStudentManagePage
from PO.base import Base
from PO.myoffice_page import MyOfficePage

def import_one_student(cfg, driver, base_url):

    ogstumanage = OrgStudentManagePage(driver, cfg)
    ogstumanage.open()
    stu_name = ogstumanage.delete_firstudent()
    ogstumanage.input_studentname(stu_name)
    ogstumanage.click_import()
    return stu_name

def import_multi_student(cfg, driver, base_url, stu_txt):

    ogstumanage = OrgStudentManagePage(driver, cfg)
    ogstumanage.open()
    ogstumanage.click_import_multi()
    ogstumanage.save_screenshot()
    ogstumanage.click_importchoose()
    ogstumanage.click_importfile(stu_txt)
    ogstumanage.click_importmulti()

def create_student(cfg, driver, base_url, stu_txt):

    ogstumanage = OrgStudentManagePage(driver, cfg)
    ogstumanage.open()
    cm = ogstumanage.click_create_multi()
    if cm == 1:
        pass
    else:
        ogstumanage.save_screenshot()
        ogstumanage.click_createchoose()
        ogstumanage.click_createfile(stu_txt)
        ogstumanage.click_createmulti()

def auto_create_student(cfg, driver, base_url, stu_num):
    #自动生成用户名文件创建学员
    #stu_num为需要创建学员的数量
    prefix = chr(random.randint(97, 122)) + chr(random.randint(97, 122)) \
     + chr(random.randint(97, 122))
    stu_txt = r"C:\create_stu.txt"
    stu_file = open(stu_txt, 'w')
    for i in range(stu_num):
        stu_name = 'stu_' + prefix + str(i)
        stu_psw = '1234aa'
        if i == 0:
            stu_file.writelines(" \n")
        stu_file.writelines(stu_name + " " + stu_psw + "\n")
    stu_file.close()
    time.sleep(2)
    create_student(cfg, driver, base_url, stu_txt)
    time.sleep(5)
 
def open_course_for_one(cfg, driver, base_url):
    
    ogstumanage = OrgStudentManagePage(driver, cfg)
    ogstumanage.open()
    ogstumanage.click_open_course()
    ogstumanage.save_screenshot()
    ogstumanage.click_opencate()
    ogstumanage.click_openchoose()
    ogstumanage.click_openok()
    ogstumanage.save_screenshot()
    ogstumanage.click_opensure()
    ogstumanage.save_screenshot()

def open_course_for_multi(cfg, driver, base_url):
    
    ogstumanage = OrgStudentManagePage(driver, cfg)
    ogstumanage.open()
    ogstumanage.click_open_list()
    ogstumanage.click_open_choose()
    ogstumanage.click_open_check()
    ogstumanage.save_screenshot()
    ogstumanage.click_opencate()
    ogstumanage.click_class_openchoose()
    ogstumanage.save_screenshot()
    ogstumanage.click_openok()
    ogstumanage.click_openaway()

#管理播放授权数
#管理播放授权数页面操作
def manage_course_numdetail(cfg, driver, base_url, user_name):

    ogstumanage = OrgStudentManagePage(driver, cfg)
    try:
        ogstumanage.click_pushcourse()
        ogstumanage.click_pushcontent()
        try:
            ogstumanage.click_changenum()
            ogstumanage.click_course_num()
            ogstumanage.click_save()
            ogstumanage.save_screenshot()
        except:
            pass
    except:
        pass
    ogstumanage.click_coursenum_all()
    ogstumanage.click_coursenum_allnum()
    ogstumanage.save_screenshot()
    ogstumanage.click_coursenum_apply()
  
#学员管理页面操作
def manage_course_num(cfg, driver, base_url, user_name):

    ogstumanage = OrgStudentManagePage(driver, cfg)
    ogstumanage.open()
    ogstumanage.click_stu_select()
    ogstumanage.click_stu_selectuser()
    ogstumanage.click_stu_selectinput(user_name)
    ogstumanage.click_stu_selectsearch()
    ogstumanage.save_screenshot()
    try:
        ogstumanage.click_managenum()
        ogstumanage.save_screenshot()
        manage_course_numdetail(cfg, driver, base_url, user_name)
    except:
        ogstumanage.self_dr_refresh()
#        ogstumanage.click_managenum()
        ogstumanage.save_screenshot()
        manage_course_numdetail(cfg, driver, base_url, user_name)

#购买开通授权数 bnum为购买的数量
def buy_open_num(cfg, driver, base_url):

    ba = Base(driver)
    m = MyOfficePage(driver, cfg)
    m.open()
    m.click_org_firstage()
    m.click_num_record()
    
    ogstumanage = OrgStudentManagePage(driver, cfg)
    ogstumanage.save_screenshot()
    ogstumanage.input_num()
    ogstumanage.click_buy()
    ogstumanage.save_screenshot()
    #判断余额是否充足
    re = ba.is_element_present("xpath", "//div[1]/p/span[2]")
    if re == True:
        pass
    else:
        ogstumanage.click_sure()
