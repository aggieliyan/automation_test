# -*- coding: UTF-8 -*-
'''
Created on Jun 2, 2012

@author: yilulu
'''
import time
#添加一级类目
def add_cate(cfg, driver, base_url, org_name, cate_name=u'计算机'):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"教学教务").click()    
    driver.implicitly_wait(10)
    #driver.find_element_by_link_text(u"课程类目").click()
    #time.sleep(2)
    driver.find_element(cfg.get('org_manage', 'add_topcate_by'), \
        cfg.get('org_manage', 'add_topcate')).click()#新建一级类目
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_manage', 'cate_addname_by'), \
        cfg.get('org_manage', 'cate_addname')).send_keys(cate_name)
    time.sleep(2)
    driver.find_element(cfg.get('org_manage', 'add_cate_ok_by'), \
        cfg.get('org_manage', 'add_cate_ok')).click()
    driver.implicitly_wait(10)
#删除类目   
def delete_cate(cfg, driver, base_url, org_name):  
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"教学教务").click() 
    time.sleep(2)   
    before_delete = driver.execute_script("return $(\".categTitle:last\").text()")#取最后一个类目的名称
    driver.implicitly_wait(10) 
    driver.execute_script("$(\".delete:last\").click()")
    driver.implicitly_wait(10) 
    driver.find_element(cfg.get('org_manage', 'delete_cate_ok_by'), \
        cfg.get('org_manage', 'delete_cate_ok')).click()
    driver.implicitly_wait(10) 
    return before_delete #返回被删除的类目名 
#向类目中加入课程  
def add_courese_to_cate(cfg, driver, base_url, org_name, cate_num=0):
    driver.implicitly_wait(10)
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"教学教务").click()  
    time.sleep(2)
    url_add = driver.execute_script("return $('#categoryList .manageCategCourse:eq("+str(cate_num)+")').attr('href')")
    driver.implicitly_wait(10)
    driver.get(base_url + url_add)
    time.sleep(2)
    driver.find_element_by_link_text(u"向类目添加知识资料").click()
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_manage', 'course_add_1_by'), \
        cfg.get('org_manage', 'course_add_1')).click()
    driver.implicitly_wait(10)
    add_course_name = driver.execute_script("return $(\"input[name='win_groupCheck']:eq(0)\").parent().parent().next().children().text()")
    driver.implicitly_wait(10)
    add_course_name = add_course_name.strip()
    #add_course_name = add_course_name.encode('UTF-8','ignore')
    driver.find_element(cfg.get('org_manage', 'course_add_ok_by'), \
        cfg.get('org_manage', 'course_add_ok')).click()
    time.sleep(1) 
    return add_course_name
    