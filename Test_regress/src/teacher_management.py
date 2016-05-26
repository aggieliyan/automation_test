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
from PO.base import Base
from PO.org_teacher_page import OrgteacherManagePage, OrgteacherCreatePage

def create_teacher(cfg, driver, tea_name):

    ogteamanage = OrgteacherManagePage(driver, cfg)
    ogteamanage.open()
    ogteamanage.click_createacher()
    ogteacreate = OrgteacherCreatePage(driver, cfg)
    ogteacreate.input_name(tea_name)
    ogteacreate.input_recommend(tea_name)
    ogteacreate.click_publish()
    
def create_account_teacher(cfg, driver, tea_name,account_name,account_password,account_mail):

    ogteamanage = OrgteacherManagePage(driver, cfg)
    ogteamanage.open()
    ogteamanage.click_createacher()
    ogteacreate = OrgteacherCreatePage(driver, cfg)
    ogteacreate.input_name(tea_name)
    ogteacreate.input_recommend(tea_name)
    ogteacreate.select_true()
    ogteacreate.input_account(account_name)
    ogteacreate.input_password(account_password)
    ogteacreate.input_mail(account_mail)
    ogteacreate.click_publish()
    
def edit_teacher(cfg, driver, tea_name):
    
    ogteamanage = OrgteacherManagePage(driver, cfg)
    ogteamanage.open()
    ogteamanage.click_manage()
    ogteamanage.click_editeacher()
    ogteacreate = OrgteacherCreatePage(driver, cfg)
    ogteacreate.clear_name()
    ogteacreate.input_name(tea_name)
    ogteacreate.click_publish()
    
def delete_teacher(cfg, driver):
    
    ogteamanage = OrgteacherManagePage(driver, cfg)
    ogteamanage.open()
    ogteamanage.click_manage()
    ogteamanage.click_deleteacher()
    ogteamanage.click_sure()
    