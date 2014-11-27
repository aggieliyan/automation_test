# -*- coding: UTF-8 -*-
'''
Created on May 28, 2012

@author: yilulu
'''

import time, random

from org_admin_page import OrgAdminListPage, OrgAdminInputPage

def create_admin(cfg, driver, admin_name, admin_username, admin_psw, admin_email):
    
    adpage = OrgAdminListPage(driver, cfg)
    adpage.open()
    adpage.click_create()

    editpage = OrgAdminInputPage(driver, cfg)
    editpage.input_name(admin_name)
    editpage.input_username(admin_username)
    editpage.input_password(admin_psw)
    editpage.input_psd_again(admin_psw)
    editpage.input_email(admin_email)
    editpage.input_eml_again(admin_email)
    editpage.click_add_save()
    time.sleep(1)

    # driver.get(base_url + "myOffice.do")
    # driver.implicitly_wait(30)
    # driver.find_element_by_link_text(u"系统设置").click()
    # driver.implicitly_wait(30)
    # driver.find_element_by_link_text(u"网校管理员").click()
    # driver.implicitly_wait(30)
    # driver.find_element_by_xpath(cfg.get('org_manage', 'add_admin_xpath')).click()#添加管理员
    # driver.implicitly_wait(30)

    # driver.find_element(cfg.get('org_manage', 'ad_name_by'), \
    #     cfg.get('org_manage', 'ad_name_id')).send_keys(admin_name)
    # driver.find_element(cfg.get('org_manage', 'ad_username_by'), \
    #     cfg.get('org_manage', 'ad_username_id')).send_keys(admin_username)
    # driver.find_element(cfg.get('org_manage', 'ad_psw_by'), \
    #     cfg.get('org_manage', 'ad_psw')).send_keys(admin_psw)
    # driver.find_element(cfg.get('org_manage', 'ad_repsw_by'), \
    #     cfg.get('org_manage', 'ad_repsw_id')).send_keys(admin_psw)
    # driver.find_element(cfg.get('org_manage', 'ad_email_by'), \
    #     cfg.get('org_manage', 'ad_email')).send_keys(admin_email)
    # driver.find_element(cfg.get('org_manage', 'ad_reemail_by'), \
    #     cfg.get('org_manage', 'ad_reemail')).send_keys(admin_email)
    # driver.find_element(cfg.get('org_manage', 'per_menber_by'), \
    #     cfg.get('org_manage', 'per_menber_id')).click()
    # driver.find_element(cfg.get('org_manage', 'per_student_by'), \
    #     cfg.get('org_manage', 'per_student_id')).click()
    # driver.find_element(cfg.get('org_manage', 'per_account_by'), \
    #     cfg.get('org_manage', 'per_account_id')).click()
    # driver.find_element(cfg.get('org_manage', 'per_admin_by'), \
    #     cfg.get('org_manage', 'per_admin_id')).click()
    # driver.implicitly_wait(10)
    # driver.execute_script("$('.x-btn-text').eq(0).click()")
    # time.sleep(1)


    
def auto_create_admin(cfg, driver, base_url, org_name, adm_num):

    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    admin_info = []  
    for i in range(adm_num):

        admin_name = org_name[0] +"adm_" + prefix + str(i)
        admin_username = admin_name
        admin_psw ='123456aa'
        admin_email = admin_name + "@ablesky.com"
        create_admin(cfg, driver, admin_name, admin_username, admin_psw, admin_email)
        admin_info.append(admin_name)

    return admin_info

def delete_admin(cfg, driver, base_url, admin_num=1):
    
    adpage = OrgAdminListPage(driver, cfg)
    adpage.open()
    bdelete = adpage.count_admin()
    print bdelete
    adpage.click_delete()
    adpage.click_delete_ok()
    time.sleep(1)
    adelete = adpage.count_admin()
    print adelete

    # driver.get(base_url + "myOffice.do")
    # driver.implicitly_wait(30)
    # driver.find_element_by_link_text(u"系统设置").click()
    # driver.implicitly_wait(30)
    # driver.find_element_by_link_text(u"网校管理员").click()
    # driver.implicitly_wait(30)
    # alist = driver.find_elements_by_link_text(u"删除管理员")
    # alist[-1].click()
    # time.sleep(1) 
    # driver.find_element(cfg.get('org_manage', 'delete_ad_ok_by'), \
    #                     cfg.get('org_manage', 'delete_ad_ok')).click()
    # time.sleep(5)
    # blist = driver.find_elements_by_link_text(u"删除管理员")
    if bdelete == adelete:
        return False
    else:
        return True



def modify_admin(cfg, driver, base_url):

    adpage = OrgAdminListPage(driver, cfg)
    adpage.open()
    adpage.click_edit()

    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    admin_name = "adm_" + prefix
    editpage = OrgAdminInputPage(driver, cfg)
    editpage.input_name(admin_name)
    editpage.click_edit_save()
    driver.back()
    time.sleep(1)

    # driver.get(base_url + "myOffice.do")
    # driver.implicitly_wait(30)
    # driver.find_element_by_link_text(u"系统设置").click()
    # driver.implicitly_wait(30)
    # driver.find_element_by_link_text(u"网校管理员").click()
    # driver.implicitly_wait(30) 
    # prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    # admin_name = "adm_" + prefix
    # #driver.find_element(cfg.get('org_index','org_manage_xpath_by'),cfg.get('org_index','org_manage_xpath')).click()
    # driver.implicitly_wait(10)
    # driver.find_element_by_link_text(u"编辑管理员").click()   

    # driver.find_element(cfg.get('org_manage', 'ad_name_by'), \
    #     cfg.get('org_manage', 'ad_name_id')).clear()
    # driver.find_element(cfg.get('org_manage', 'ad_name_by'), \
    #     cfg.get('org_manage', 'ad_name_id')).send_keys(admin_name)
    # driver.implicitly_wait(10)
    # #driver.find_element(cfg.get('org_manage','admin_modify_xpath_by'),cfg.get('org_manage','admin_modify_xpath')).click()
    # driver.execute_script("$(\"#editButton button\").eq(0).click()")
    # driver.implicitly_wait(30)
    # time.sleep(1)
    
    return admin_name
