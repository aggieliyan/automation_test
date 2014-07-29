# -*- coding: UTF-8 -*-
'''
Created on 2014-7-23

@author: guoyuling
'''


import unittest, time, re,random


    
def create_subject(cfg,driver, base_url,org_name,subject_name):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(2)
    driver.find_element(cfg.get('exam','new_subject_id_by'),cfg.get('exam','new_subject_id')).click()
    driver.find_element(cfg.get('exam','sub_name_by'),cfg.get('exam','sub_name')).clear()
    driver.find_element(cfg.get('exam','sub_name_by'),cfg.get('exam','sub_name')).send_keys(subject_name)
    time.sleep(3)
    driver.find_element(cfg.get('exam','sub_ok_xpath_by'),cfg.get('exam','sub_ok_xpath')).click()
    time.sleep(1)

def auto_create_subject(cfg,driver,base_url,org_name,sub_num):
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    subject_info = []
    for i in range(sub_num):
        subject_name = org_name[0] +"sub_" +prefix+str(i)
        create_subject(cfg,driver, base_url,org_name,subject_name)
        subject_info.append(subject_name)
    return subject_info


def modify_subject(cfg,driver, base_url, org_name):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(5)
    subject_name= "subject001" 
    driver.find_element(cfg.get('exam','sub_big_xpath_by'),cfg.get('exam','sub_big_xpath')).click()
    driver.find_element(cfg.get('exam','sub_small_xpath_by'),cfg.get('exam','sub_small_xpath')).click()
    time.sleep(5)
    driver.find_element(cfg.get('exam','sub_name_by'),cfg.get('exam','sub_name')).clear()
    driver.find_element(cfg.get('exam','sub_name_by'),cfg.get('exam','sub_name')).send_keys(subject_name)
    driver.find_element(cfg.get('exam','sub_ok_xpath_by'),cfg.get('exam','sub_ok_xpath')).click()
    return subject_name

def delete_subject(cfg,driver, base_url, org_name, sub_num=1):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(5)
    driver.find_element(cfg.get('exam','sub_big_xpath_by'),cfg.get('exam','sub_big_xpath')).click()
    driver.find_element(cfg.get('exam','sub_del_xpath_by'),cfg.get('exam','sub_del_xpath')).click()
    time.sleep(5)
    driver.find_element(cfg.get('exam','sub_delok_xpath_by'),cfg.get('exam','sub_delok_xpath')).click()
    time.sleep(2)
    
    
def create_exam_cate(cfg,driver, base_url,org_name,cate_name,cate_detail):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(2) 
    driver.find_element_by_link_text(u"类目管理").click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','cate_newcateid_by'),cfg.get('exam','cate_newcateid')).click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','cate_addname_by'),cfg.get('exam','cate_addname')).send_keys(cate_name)
    driver.find_element(cfg.get('exam','cate_desname_by'),cfg.get('exam','cate_desname')).clear()
    driver.find_element(cfg.get('exam','cate_desname_by'),cfg.get('exam','cate_desname')).send_keys(cate_detail)
    time.sleep(1)
    driver.find_element(cfg.get('exam','cate_oknew_button_by'),cfg.get('exam','cate_oknew_button')).click()
    time.sleep(3)
    

def auto_create_exam_cate(cfg,driver, base_url,org_name,cate_num):
    
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    cate_info = []
    for i in range(cate_num):
        cate_name = org_name[0] +"cate_" +prefix+str(i)
        cate_detail = org_name[0] +"cate_" +prefix+str(i)
        create_exam_cate(cfg,driver, base_url,org_name,cate_name,cate_detail)
        cate_info.append(cate_name)
    return cate_info

def modify_exam_cate(cfg,driver, base_url,org_name):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(2) 
    driver.find_element_by_link_text(u"类目管理").click()
    time.sleep(1)
    cate_name = 'cate001'
    cate_detail = 'cate001describe'
    driver.find_element(cfg.get('exam','cate_mod_xpath_by'),cfg.get('exam','cate_mod_xpath')).click()
    driver.find_element(cfg.get('exam','cate_addname_by'),cfg.get('exam','cate_addname')).clear()
    driver.find_element(cfg.get('exam','cate_addname_by'),cfg.get('exam','cate_addname')).send_keys(cate_name)
    driver.find_element(cfg.get('exam','cate_desname_by'),cfg.get('exam','cate_desname')).clear()
    driver.find_element(cfg.get('exam','cate_desname_by'),cfg.get('exam','cate_desname')).send_keys(cate_detail)
    time.sleep(1)
    driver.find_element(cfg.get('exam','cate_oknew_button_by'),cfg.get('exam','cate_oknew_button')).click()
    time.sleep(3)
    
def delete_exam_cate(cfg,driver, base_url,org_name):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(2) 
    driver.find_element_by_link_text(u"类目管理").click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','cate_del_xpath_by'),cfg.get('exam','cate_del_xpath')).click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','cate_oknew_button_by'),cfg.get('exam','cate_oknew_button')).click()
    time.sleep(3)


def create_exam_point(cfg,driver, base_url,org_name,point_name,point_detail,other_groom):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(2) 
    driver.find_element_by_link_text(u"考点库").click()
    driver.find_element(cfg.get('exam','point_addnewid_by'),cfg.get('exam','point_addnewid')).click()
    driver.find_element(cfg.get('exam','point_addname_by'),cfg.get('exam','point_addname')).clear()
    driver.find_element(cfg.get('exam','point_addname_by'),cfg.get('exam','point_addname')).send_keys(point_name)
    driver.find_element(cfg.get('exam','point_desname_by'),cfg.get('exam','point_desname')).clear()
    driver.find_element(cfg.get('exam','point_desname_by'),cfg.get('exam','point_desname')).send_keys(point_detail)
    time.sleep(2)
    driver.find_element_by_link_text("+").click()
    #driver.find_element_by_css_selector(cfg.get('exam','point_lesson_css')).click()
    driver.find_element(cfg.get('exam','point_address_xpath1_by'),cfg.get('exam','point_address_xpath1')).click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_address_xpath2_by'),cfg.get('exam','point_address_xpath2')).click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_ok_lessbotton_by'),cfg.get('exam','point_ok_lessbotton')).click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_othergroom_by'),cfg.get('exam','point_othergroom')).clear()
    driver.find_element(cfg.get('exam','point_othergroom_by'),cfg.get('exam','point_othergroom')).send_keys(other_groom)
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_okbotton_by'),cfg.get('exam','point_okbotton')).click()
    time.sleep(2)

def auto_create_exam_point(cfg,driver, base_url,org_name,point_num):
    
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    point_info = []
    for i in range(point_num):
        point_name = org_name[0] +"point_" +prefix+str(i)
        point_detail = org_name[0] +"point_" +prefix+str(i)
        other_groom = org_name[0] +"point_" +prefix+str(i)
        create_exam_point(cfg,driver, base_url,org_name,point_name,point_detail,other_groom)
        point_info.append(point_name)
    return point_info


def modify_exam_point(cfg,driver, base_url, org_name):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(2) 
    driver.find_element_by_link_text(u"考点库").click()
    point_name = 'bianjikaodian'
    point_detail = 'kaodianmiaoshu'
    point_other = 'qitatuijian'
    driver.find_element(cfg.get('exam','point_edit_by'),cfg.get('exam','point_edit')).click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_addname_by'),cfg.get('exam','point_addname')).clear()
    driver.find_element(cfg.get('exam','point_addname_by'),cfg.get('exam','point_addname')).send_keys(point_name)
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_desname_by'),cfg.get('exam','point_desname')).clear()
    driver.find_element(cfg.get('exam','point_desname_by'),cfg.get('exam','point_desname')).send_keys(point_detail)
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_lesdel_botton_by'),cfg.get('exam','point_lesdel_botton')).click()
    time.sleep(1)

    driver.find_element_by_link_text("+").click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_address_xpath1_by'),cfg.get('exam','point_address_xpath1')).click()
    driver.find_element(cfg.get('exam','point_address_xpath2_by'),cfg.get('exam','point_address_xpath2')).click()
    driver.find_element(cfg.get('exam','point_ok_lessbotton_by'),cfg.get('exam','point_ok_lessbotton')).click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_othergroom_by'),cfg.get('exam','point_othergroom')).click()
    driver.find_element(cfg.get('exam','point_othergroom_by'),cfg.get('exam','point_othergroom')).clear()
    driver.find_element(cfg.get('exam','point_othergroom_by'),cfg.get('exam','point_othergroom')).send_keys(point_other)
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_okbotton_by'),cfg.get('exam','point_okbotton')).click()
    time.sleep(2)


def delete_exam_point(cfg,driver, base_url, org_name):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(2) 
    driver.find_element_by_link_text(u"考点库").click()
    time.sleep(1)
    driver.find_element(cfg.get('exam','point_delete_xpath_by'),cfg.get('exam','point_delete_xpath')).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam','point_delokbot_xpath_by'),cfg.get('exam','point_delokbot_xpath')).click()
    time.sleep(1)
    
    
    
    
    
    