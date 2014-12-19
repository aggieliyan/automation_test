# -*- coding: UTF-8 -*-
'''
Created on 2014-7-23

@author: guoyuling
'''


import unittest, time, re,random
from selenium.common.exceptions import NoSuchElementException

#scp=subject.cate.point
def create_subject(cfg, driver, base_url, org_name, subject_name):
    addscp = OrgExamCreateListPage(driver, cfg)
    addscp.open()
    addscp.click_create_sub()
    editscp = OrgExamInputListPage(driver, cfg)
    okscp = OrgExamiOkListPage(driver, cfg)
    try:
        editscp.clear_sub()
    except NoSuchElementException, e:
        print u"创建考试科目失败原因: 最多只能建10个科目,请删除一些科目再来创建!"
        return False
    else:
        editscp.input_sub(subject_name)
        okscp.click_addsub_ok()
        
    

def auto_create_subject(cfg, driver, base_url, org_name, sub_num):
    addscp = OrgExamCreateListPage(driver, cfg)
    addscp.open()
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

    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))    
    edit_name = driver.execute_script("return $('.subject-item-con').eq(0).children().eq(0).text()")
    subject_name = org_name[0] + "sub_" + prefix
    searchscp = OrgExamSearchListPage(driver, cfg)
    if edit_name != u'默认科目':  
        try:
            searchscp.click_sub_big1()
        except:
            print u"亲,先创建个科目再来编辑呗!"
            return "lack of subject"
        else:
            searchscp.click_sub_small1()
    else:
        driver.implicitly_wait(10)
        try:
            searchscp.click_sub_big2()
        except:
            print u"亲,先创建个科目再来编辑呗!"
            return "lack of subject"
        else:
            searchscp.click_sub_small2()
    editscp=OrgExamInputListPage(driver, cfg)
    editscp.clear_sub()
    editscp.input_sub()
    okscp=OrgExamiOkListPage(driver, cfg)
    okscp.click_addsub_ok()  
    return subject_name

def delete_subject(cfg, driver, base_url, org_name, sub_num=1):
    addscp = OrgExamCreateListPage(driver, cfg)
    addscp.open()
    del_name = driver.execute_script("return $('.subject-item-con').eq(0).children().eq(0).text()")
    searchscp = OrgExamSearchListPage(driver, cfg)  
    if del_name != u'默认科目': 
        try:
            searchscp.click_sub_big1()
        except NoSuchElementException, e:
            print u"亲,先创建个科目再来删除呗!"
            return False
        else:
            searchscp.click_sub_del1()
    else:
        driver.implicitly_wait(10)
        try:
            searchscp.click_sub_big2()
        except NoSuchElementException, e:
            print u"亲,先创建个科目再来删除呗!"
            return False
        else:
            searchscp.click_sub_del2()
            del_name = searchscp.click_sub_big2().text

    okscp=OrgExamiOkListPage(driver, cfg)
    okscp.click_delsub_ok():
    print del_name 
    return del_name

def create_exam_cate(cfg, driver, base_url, org_name, cate_name, cate_detail):
    addscp = OrgExamCreateListPage(driver, cfg)
    addscp.open()
    addscp.click_create_cate()
    searchscp = OrgExamSearchListPage(driver, cfg)
    searchscp.click_create()
    editscp = OrgExamInputListPage(driver, cfg)
    editscp.input_cname(cate_name)
    editscp.input_cdetail(cate_detail)
    okscp = OrgExamiOkListPage(driver, cfg)
    okscp.click_addcate_ok()

def auto_create_exam_cate(cfg, driver, base_url, org_name, cate_num):
    
    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    cate_info = []
    for i in range(cate_num):
        cate_name = org_name[0] + "cate_" + prefix + str(i)
        cate_detail = org_name[0] +"cate_" + prefix + str(i)
        create_exam_cate(cfg,driver, base_url,org_name,cate_name,cate_detail)
        cate_info.append(cate_name)
    return cate_info

def modify_exam_cate(cfg, driver, base_url, org_name):
    addscp = OrgExamCreateListPage(driver, cfg)
    addscp.open()
    addscp.click_create_cate()
    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    cate_name = org_name[0] + "cate_" + prefix
    cate_detail = org_name[0] + "cate_" + prefix
    searchscp = OrgExamSearchListPage(driver, cfg)
    searchscp.click_modify_cate()
    editscp = OrgExamInputListPage(driver, cfg)
    editscp.input_cname(cate_name)
    editscp.input_cdetail(cate_detail)
    okscp = OrgExamiOkListPage(driver, cfg)
    okscp.click_addcate_ok()


def delete_exam_cate(cfg, driver, base_url, org_name):
    addscp = OrgExamCreateListPage(driver, cfg)
    addscp.open()
    addscp.click_create_cate()
    searchscp = OrgExamSearchListPage(driver, cfg)
    searchscp.click_delete_cate()
    okscp = OrgExamiOkListPage(driver, cfg)
    okscp.click_addcate_ok()



def create_exam_point(cfg, driver, base_url, org_name, point_name, point_detail, other_groom):
    addscp = OrgExamCreateListPage(driver, cfg)
    addscp.open()
    addscp.click_point_page()
    searchscp = OrgExamSearchListPage(driver, cfg)
    searchscp.click_create_point()
    editscp = OrgExamInputListPage(driver, cfg)
    editscp.input_pname()
    editscp.pd_input()
    searchscp.click_add_course()
    searchscp.click_add_courses()
    okscp = OrgExamiOkListPage(driver, cfg)
    okscp.click_addcourse_ok()
    editscp.input_other_groom()
    okscp.click_addpoint_ok()


def auto_create_exam_point(cfg, driver, base_url, org_name, point_num):

    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    point_info = []
    for i in range(point_num):
        point_name = org_name[0] + "point_" + prefix + str(i)
        point_detail = org_name[0] + "point_" + prefix + str(i)
        other_groom = org_name[0] + "point_" + prefix + str(i)
        create_exam_point(cfg, driver, base_url, org_name, point_name, point_detail, other_groom)
        point_info.append(point_name)
    return point_info


def modify_exam_point(cfg, driver, base_url, org_name):
    addscp = OrgExamCreateListPage(driver, cfg)
    addscp.open()
    addscp.click_point_page()
    point_name = 'editpoint'
    point_detail = 'pointdetail'
    point_other = 'othergroom'
    searchscp = OrgExamSearchListPage(driver, cfg)
    searchscp.click_modify_point()
    editscp = OrgExamInputListPage(driver, cfg)
    editscp.input_pname()
    editscp.pd_input()
    driver.implicitly_wait(10)
    searchscp.click_lesdel_point()
    searchscp.click_add_course()
    searchscp.click_add_courses()
    okscp = OrgExamiOkListPage(driver, cfg)
    okscp.click_addcourse_ok()
    editscp.input_other_groom()
    okscp.click_addpoint_ok()

    

def delete_exam_point(cfg, driver, base_url, org_name):
    addscp = OrgExamCreateListPage(driver, cfg)
    addscp.open()
    addscp.click_point_page()
    searchscp = OrgExamSearchListPage(driver, cfg)
    searchscp.click_delete_point()
    okscp = OrgExamiOkListPage(driver, cfg)
    okscp.click_delpoint_ok()