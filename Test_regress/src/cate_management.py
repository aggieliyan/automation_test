# -*- coding: UTF-8 -*-
'''
Created on Jun 2, 2012

@author: yilulu
'''
import time
from PO.org_cate_page import OrgCateListPage, OrgcatecoursePge

#添加一级类目
def add_cate(cfg, driver, base_url, cate_name=u'cate_name'):
    ogcate = OrgCateListPage(driver, cfg)
    ogcate.open()
    ogcate.click_create_FirstCate()
    ogcate.input_catename(cate_name)
    ogcate.click_ensure()
        
#删除类目   
def delete_cate(cfg, driver, base_url):  
    ogcate = OrgCateListPage(driver, cfg)
    ogcate.open()
    before_delete = ogcate.get_lastcatename()
    ogcate.click_delete()
    ogcate.click_delete_ok()
    return before_delete #返回被删除的类目名 

#向类目中加入课程  
def add_courese_to_cate(cfg, driver, base_url, cate_num=0):
    ogcate = OrgCateListPage(driver, cfg)
    ogcate.open()    
    ogcatecourse = OrgcatecoursePge(driver, cfg)
    ogcatecourse.inter_catecourse(cate_num)
    ogcatecourse.click_addcourse_tocate()
    ogcatecourse.select_first()
    add_course_name = ogcatecourse.get_firstcoursename()
    ogcatecourse.click_add()
    return add_course_name


##添加一级类目
#def add_cate(cfg, driver, base_url, cate_name=u'cate_name'):
#    time.sleep(2)
#    driver.get(base_url + "myOffice.do")
#    driver.implicitly_wait(10)
#    driver.find_element_by_link_text(u"教学教务").click()    
#    time.sleep(3)
#    driver.find_element(cfg.get('org_manage', 'add_topcate_by'), \
#        cfg.get('org_manage', 'add_topcate')).click()#新建一级类目
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'cate_addname_by'), \
#        cfg.get('org_manage', 'cate_addname')).send_keys(cate_name)
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'add_cate_ok_by'), \
#        cfg.get('org_manage', 'add_cate_ok')).click()
#    driver.implicitly_wait(10)
##删除类目   
#def delete_cate(cfg, driver, base_url):  
#    time.sleep(2)
#    driver.get(base_url + "myOffice.do")
#    driver.implicitly_wait(10)
#    driver.find_element_by_link_text(u"教学教务").click() 
#    time.sleep(5)   
#    before_delete = driver.execute_script("return $(\".categTitle:last\").text()")#取最后一个类目的名称
#    time.sleep(2)
#    driver.execute_script("$(\".delete:last\").click()")
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'delete_cate_ok_by'), \
#        cfg.get('org_manage', 'delete_cate_ok')).click()
#    driver.implicitly_wait(10) 
#    return before_delete #返回被删除的类目名 
##向类目中加入课程  
#def add_courese_to_cate(cfg, driver, base_url, cate_num=0):
#    time.sleep(2)
#    driver.get(base_url + "myOffice.do")
#    driver.implicitly_wait(10)
#    driver.find_element_by_link_text(u"教学教务").click()  
#    time.sleep(3)
#    url_add = driver.execute_script("return $('#categoryList .manageCategCourse:eq("+str(cate_num)+")').attr('href')")
#    time.sleep(2)
#    driver.get(base_url + str(url_add))
#    time.sleep(3)
#    driver.find_element_by_link_text(u"向类目添加知识资料").click()
#    time.sleep(3)
#    driver.find_element(cfg.get('org_manage', 'course_add_1_by'), \
#        cfg.get('org_manage', 'course_add_1')).click()
#    driver.implicitly_wait(10)
#    add_course_name = driver.execute_script("return $(\"input[name='win_groupCheck']:eq(0)\").parent().parent().next().children().text()")
#    driver.implicitly_wait(10)
#    add_course_name = add_course_name.strip()
#    time.sleep(2)
#    #add_course_name = add_course_name.encode('UTF-8','ignore')
#    driver.find_element(cfg.get('org_manage', 'course_add_ok_by'), \
#        cfg.get('org_manage', 'course_add_ok')).click()
#    time.sleep(2) 
#    return add_course_name
    