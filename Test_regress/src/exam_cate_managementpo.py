# -*- coding: UTF-8 -*-
'''
Created on 2014-7-23

@author: guoyuling
'''


import unittest, time, re,random
from selenium.common.exceptions import NoSuchElementException
from PO.exam_subject_page import SubjectListPage
from PO.exam_cate_page import ExamCateListPage
from PO.exam_point_page import ExamPointListPage

def create_subject(cfg, driver, base_url, org_name, subject_name):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    exam_subject.click_create_sub()
    try:
        exam_subject.clear_sub()
    except NoSuchElementException, e:
        print u"创建考试科目失败原因: 最多只能建10个科目,请删除一些科目再来创建!"
        return False
    else:
        exam_subject.input_sub(subject_name)
        exam_subject.click_addsub_ok()
        
    

def auto_create_subject(cfg, driver, base_url, org_name, sub_num):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    subject_info = []
    for i in range(sub_num):
        subject_name = org_name[0] + "sub_" + prefix + str(i)
        rs = create_subject(cfg, driver, base_url, org_name, subject_name)
        subject_info.append(subject_name)
        if rs == False:
            break
    return subject_name


def modify_subject(cfg, driver, base_url, org_name):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    time.sleep(2)    
    edit_name = driver.execute_script("return $('.subject-item-con').eq(0).children().eq(0).text()")
    subject_name = org_name[0] + "sub_" + prefix
    print edit_name
    if edit_name != u'默认科目':  
        try:
            exam_subject.click_sub_big1()
        except:
            print u"亲,先创建个科目再来编辑呗!"
            return "lack of subject"
        else:
            
            exam_subject.click_sub_small1()
    else:
        time.sleep(1)
        try:
            
            exam_subject.click_sub_big2()
        
        except:
            print u"亲,先创建个科目再来编辑呗！！！！！！！！!"
            return "lack of subject"
        else:
            time.sleep(1)
            #button = driver.execute_script("return $('.subject-item-con').eq(1).children().eq(2).children().eq(0).attr('href')")
            #button.click()
            
            exam_subject.click_sub_small2()
    exam_subject.clear_sub()
    exam_subject.input_sub(subject_name)
    exam_subject.click_addsub_ok()  
    return subject_name

def delete_subject(cfg, driver, base_url, org_name, sub_num=1):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    del_name = driver.execute_script("return $('.subject-item-con').eq(0).children().eq(0).text()")
    total_num = driver.execute_script("return $('.subject-item-con').size()")
    if del_name != u'默认科目': 
        try:
            exam_subject.click_sub_big1()
        except NoSuchElementException, e:
            print u"亲,先创建个科目再来删除呗!"
            return False
        else:
            exam_subject.click_sub_del1()
    else:
        driver.implicitly_wait(10)
        try:
            exam_subject.click_sub_big2()
        except NoSuchElementException, e:
            print u"亲,先创建个科目再来删除呗!"
            return False
        else:
            exam_subject.click_sub_del2()
            #del_name = exam_subject.click_sub_big2().text
    time.sleep(2)
    exam_subject.click_delsub_ok()
    print del_name 
    return total_num

def create_exam_cate(cfg, driver, base_url, org_name, cate_name, cate_detail):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    exam_subject.click_cate_page()
    exam_cate = ExamCateListPage(driver, cfg)
    exam_cate.click_create()
    exam_cate.input_cname(cate_name)
    exam_cate.input_cdetail(cate_detail)
    exam_cate.click_addcate_ok()
    return cate_name

def auto_create_exam_cate(cfg, driver, base_url, org_name, cate_num):
    
    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    cate_info = []
    for i in range(cate_num):
        cate_name = org_name[0] + "cate_" + prefix + str(i)
        cate_detail = org_name[0] +"cate_" + prefix + str(i)
        create_exam_cate(cfg,driver, base_url,org_name,cate_name,cate_detail)
        cate_info.append(cate_name)
    return cate_name

def modify_exam_cate(cfg, driver, base_url, org_name):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    exam_subject.click_cate_page()
    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    cate_name = org_name[0] + "cate_" + prefix
    cate_detail = org_name[0] + "cate_" + prefix
    exam_cate = ExamCateListPage(driver, cfg)
    exam_cate.click_modify_cate()
    exam_cate.input_cname(cate_name)
    exam_cate.input_cdetail(cate_detail)
    exam_cate.click_addcate_ok()
    return cate_name


def delete_exam_cate(cfg, driver, base_url, org_name):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    exam_subject.click_cate_page()
    total_num = driver.execute_script("return $('.categTitleFalse').size()")
    exam_cate = ExamCateListPage(driver, cfg)
    exam_cate.click_delete_cate()
    exam_cate.click_addcate_ok()
    return total_num



def create_exam_point(cfg, driver, base_url, org_name, point_name, point_detail, other_groom):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    exam_subject.click_point_page()
    exam_point = ExamPointListPage(driver, cfg)
    exam_point.click_create_point()
    exam_point.input_pname(point_name)
    exam_point.input_pdetail(point_detail)
    exam_point.click_add_course()
    exam_point.click_add_courses()
    exam_point.click_addcourse_ok()
    exam_point.input_other_groom(other_groom)
    exam_point.click_addpoint_ok()
    return point_name


def auto_create_exam_point(cfg, driver, base_url, org_name, point_num):

    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    point_info = []
    for i in range(point_num):
        point_name = org_name[0] + "point_" + prefix + str(i)
        point_detail = org_name[0] + "point_" + prefix + str(i)
        other_groom = org_name[0] + "point_" + prefix + str(i)
        create_exam_point(cfg, driver, base_url, org_name, point_name, point_detail, other_groom)
        point_info.append(point_name)
    return point_name


def modify_exam_point(cfg, driver, base_url, org_name):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    exam_subject.click_point_page()
    point_name = 'editpoint'
    point_detail = 'pointdetail'
    point_other = 'othergroom'
    exam_point = ExamPointListPage(driver, cfg)
    exam_point.click_modify_point()
    exam_point.input_pname(point_name)
    exam_point.input_pdetail(point_detail)
    #exam_point.click_lesdel_point()
    time.sleep(1)
    exam_point.click_add_course()
    exam_point.click_add_courses()
    exam_point.click_addcourse_ok()
    exam_point.input_other_groom(point_other)
    time.sleep(1)
    exam_point.click_addpoint_ok()
    return point_name


    

def delete_exam_point(cfg, driver, base_url, org_name):
    exam_subject = SubjectListPage(driver, cfg)
    exam_subject.open()
    exam_subject.click_point_page()
    time.sleep(1)
    total_num = driver.execute_script("return $('.categTitleFalse').size()")
    exam_point = ExamPointListPage(driver, cfg)
    exam_point.click_delete_point()
    exam_point.click_delpoint_ok()
    return total_num