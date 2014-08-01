# -*- coding: UTF-8 -*-
'''
Created on May 28, 2012

@author: yilulu
'''

import time, random

def create_admin(cfg, driver, base_url, admin_name, admin_username, admin_psw, admin_email):
    
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"系统设置").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"网校管理员").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(cfg.get('org_manage', 'add_admin_xpath')).click()#添加管理员
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_manage','ad_name_by'),cfg.get('org_manage','ad_name_id')).send_keys(admin_name)
    driver.find_element(cfg.get('org_manage','ad_username_by'),cfg.get('org_manage','ad_username_id')).send_keys(admin_username)
    driver.find_element(cfg.get('org_manage','ad_psw_by'),cfg.get('org_manage','ad_psw_id')).send_keys(admin_psw)
    driver.find_element(cfg.get('org_manage','ad_repsw_by'),cfg.get('org_manage','ad_repsw_id')).send_keys(admin_psw)
    driver.find_element(cfg.get('org_manage','ad_email_by'),cfg.get('org_manage','ad_email_id')).send_keys(admin_email)
    driver.find_element(cfg.get('org_manage','ad_reemail_by'),cfg.get('org_manage','ad_reemail_id')).send_keys(admin_email)
    driver.find_element(cfg.get('org_manage','per_menber_by'),cfg.get('org_manage','per_menber_id')).click()
    driver.find_element(cfg.get('org_manage','per_student_by'),cfg.get('org_manage','per_student_id')).click()
    driver.find_element(cfg.get('org_manage','per_account_by'),cfg.get('org_manage','per_account_id')).click()
    driver.find_element(cfg.get('org_manage','per_admin_by'),cfg.get('org_manage','per_admin_id')).click()
    driver.implicitly_wait(10)
    driver.execute_script("$('.x-btn-text').eq(0).click()")
    driver.implicitly_wait(10)

def auto_create_admin(cfg, driver, base_url, org_name, adm_num):
    
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    admin_info = []  
    for i in range(adm_num):
        
        admin_name = org_name[0] +"adm_" +prefix+str(i)
        admin_username = admin_name
        admin_psw ='123456aa'
        admin_email = admin_name+"@ablesky.com"
        create_admin(cfg,driver, base_url,admin_name,admin_username,admin_psw,admin_email)
        admin_info.append(admin_name)
        
    return admin_info
    
def delete_admin(cfg, driver, base_url, admin_num=1):
        
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"系统设置").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"网校管理员").click()
    driver.implicitly_wait(10)
    if admin_num == 1:
        driver.find_element_by_link_text(u"删除管理员").click()
    else:
        driver.find_element_by_xpath("//div["+str(2+admin_num)+"]/div/div/div[2]/div[3]/a").click()
    time.sleep(1) 
    driver.find_element(cfg.get('org_manage','delete_ad_ok_xpath_by'),cfg.get('org_manage','delete_ad_ok_xpath')).click()
    time.sleep(3)
    
    
def modify_admin(cfg, driver, base_url):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"系统设置").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"网校管理员").click()
    driver.implicitly_wait(10)
    
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    admin_name = "adm_" +prefix
    #driver.find_element(cfg.get('org_index','org_manage_xpath_by'),cfg.get('org_index','org_manage_xpath')).click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"编辑管理员").click()   
    driver.find_element(cfg.get('org_manage','ad_name_by'),cfg.get('org_manage','ad_name_id')).clear()
    driver.find_element(cfg.get('org_manage','ad_name_by'),cfg.get('org_manage','ad_name_id')).send_keys(admin_name)
    driver.implicitly_wait(10)
    #driver.find_element(cfg.get('org_manage','admin_modify_xpath_by'),cfg.get('org_manage','admin_modify_xpath')).click()
    driver.execute_script("$(\"#editButton button\").eq(0).click()")
    time.sleep(1)
    return admin_name
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        