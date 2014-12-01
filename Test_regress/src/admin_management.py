# -*- coding: UTF-8 -*-
'''
Created on May 28, 2012

@author: yilulu
'''

import time, random

from PO.org_admin_page import OrgAdminListPage, OrgAdminInputPage

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
    
def auto_create_admin(cfg, driver, adm_num):

    prefix = chr(random.randint(97,122)) + chr(random.randint(97,122)) + chr(random.randint(97,122))
    admin_info = []  
    for i in range(adm_num):

        admin_name = "adm_" + prefix + str(i)
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
    
    return admin_name
