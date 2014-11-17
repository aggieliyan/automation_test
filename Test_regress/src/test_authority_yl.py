# -*- coding: UTF-8 -*-
import os
import ConfigParser
import traceback
import time, random
from selenium import webdriver

import login
import new_course_management
import cate_management, student_management, new_course_management, card_management, user_management
    

#系统设置-管理员/客服-网校管理员
def manageorservice_manage():
    time.sleep(1)
    current_url = driver.current_url
    try:
        driver.find_element("class name","colorGray")#找到编辑管理员的置灰span
    except Exception:
        print traceback.format_exc()
        print u"没有管理员的读权限"

    time.sleep(1)
    try:
        driver.find_element_by_link_text(u"添加管理员").click()
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)
        driver.find_element_by_link_text(u"编辑管理员").click()
        time.sleep(1)
        driver.get(current_url)                
    except Exception:
        print traceback.format_exc()
        print u"没有管理员的编辑权限"
        
    time.sleep(1)
    try:
        driver.find_element_by_link_text(u"删除管理员").click()
        time.sleep(1)
        driver.find_element("class name","x-btn-text").click()#删除 
        time.sleep(1)          
    except Exception:
        print traceback.format_exc()
        print u"没有管理员的删除权限"
        
#批量创建读权限管理员
def create_manage_read():
    user_file = open(r"C:/register_admin_user_list_read.txt", 'w')
    i = 1
    pre_name='relog_'
    for item in driver.find_elements("class name","categoryAuthority-look-active"):
        # if i < 22:
        #     i += 1
        #     continue
        admin_username = create_manage_fillmanage(pre_name, i, user_file)
        time.sleep(1)
        if i != 1:
            driver.execute_script("$('.onOff').click()")
            time.sleep(1)
            driver.execute_script("$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none')")
        time.sleep(1)
        driver.find_element_by_link_text(u"保存").click()
        time.sleep(1)
        user_file.writelines(admin_username + "\n")
        i = i + 1
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"添加管理员").click() 
        time.sleep(2)
    print u'读权限管理员个数:' + str(i)
    user_file.close()

#批量创建编辑权限管理员
def create_manage_edit():
    i = 1
    pre_name = 'edlog_'
    user_file = open(r"C:/register_admin_user_list_edit.txt", 'w')
    for item in driver.find_elements("class name", "categoryAuthority-add"):
        # if i < 28:
        #     i += 1
        #     continue
        admin_username = create_manage_fillmanage(pre_name, i, user_file)
        if i != 1:
            driver.execute_script("$('.onOff').click()")
            time.sleep(1)
            driver.execute_script("$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none'); \
                $('.categoryAuthority-add-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-add').eq(" + str(i-1) + ").attr('style','display:none')")

        time.sleep(1)
        driver.find_element_by_link_text(u"保存").click()
        time.sleep(1)
        user_file.writelines(admin_username + "\n")
        i = i + 1
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"添加管理员").click() 
        time.sleep(1)
    print u'编辑权限管理员个数:' + str(i)
    user_file.close()

#批量创建删除权限管理员
def create_manage_delete():
    user_file = open(r"C:/register_admin_user_list_delete.txt", 'w')
    i = 1
    pre_name = 'delog_'
    for item in driver.find_elements("class name", "categoryAuthority-delete"):
        admin_username = create_manage_fillmanage(pre_name, i, user_file)
        if i != 1:
            driver.execute_script("$('.onOff').click()")
            time.sleep(1)
            driver.execute_script("$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none'); \
                $('.categoryAuthority-delete-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-delete').eq(" + str(i-1) + ").attr('style','display:none')")
        time.sleep(1)
        driver.find_element_by_link_text(u"保存").click()
        time.sleep(1)
        user_file.writelines(admin_username + "\n")
        i = i + 1
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"添加管理员").click()
        time.sleep(1)
    print u'删除权限管理员个数' + str(i)
    user_file.close()

#批量创建查看、编辑、删除权限管理员
def create_manage_all():
    user_file = open(r"C:/register_admin_user_list_all.txt", 'w')
    i = 1
    pre_name = 'alllog_'
    for item in driver.find_elements("class name", "categoryAuthorityBox"):
        admin_username = create_manage_fillmanage(pre_name, i, user_file)
        if i == 1:
            time.sleep(1)
            driver.execute_script("$('.categoryAuthority-add-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-add').eq(" + str(i-1) + ").attr('style','display:none'); \
                $('.categoryAuthority-delete-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-delete').eq(" + str(i-1) + ").attr('style','display:none')")
        else:
            driver.execute_script("$('.onOff').click()")
            time.sleep(1)
            driver.execute_script("$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none'); \
                $('.categoryAuthority-add-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-add').eq(" + str(i-1) + ").attr('style','display:none'); \
                $('.categoryAuthority-delete-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
                $('.categoryAuthority-delete').eq(" + str(i-1) + ").attr('style','display:none')")
        time.sleep(1)
        driver.find_element_by_link_text(u"保存").click()
        time.sleep(1)
        user_file.writelines(admin_username + "\n")
        i = i + 1
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"添加管理员").click() 
        time.sleep(1)
    print u'删除权限管理员个数' + str(i)
    user_file.close()

#创建管理员填写信息公用方法
def create_manage_fillmanage(pre_name, i, user_file):
    time.sleep(1)
    prefix = chr(random.randint(97, 122)) + chr(random.randint(97, 122)) + chr(random.randint(97, 122))
    admin_name = pre_name + prefix + str(i)
    admin_username = admin_name 
    admin_email = admin_name + "@sohu.com"
    admin_psw = '1234aa'
    # time.sleep(1)
    driver.find_element("id", "admin_name").send_keys(admin_name)#管理员名称
    # time.sleep(1)
    driver.find_element("id", "admin_username").send_keys(admin_username)#用户名
    # time.sleep(1)
    driver.find_element("id", "admin_password").send_keys(admin_psw)#密码
    # time.sleep(1)
    driver.find_element("id", "admin_repassword").send_keys(admin_psw)#再次输入密码
    # time.sleep(1)
    driver.find_element("id", "admin_email").send_keys(admin_email)#邮箱
    # time.sleep(1)
    driver.find_element("id", "admin_reemail").send_keys(admin_email)#再次确认邮箱
    # time.sleep(1)
    return admin_username

#创建管理员
def create_manage():
    time.sleep(2)
    driver.get("%smyOffice.do" %(base_url))
    time.sleep(2)
    driver.find_element_by_link_text(u"系统设置").click()   
    time.sleep(2)
    driver.find_element_by_link_text(u"网校管理员").click() 
    time.sleep(2)
    driver.find_element_by_link_text(u"添加管理员").click() 
    time.sleep(2)
    create_manage_read()#批量创建读权限管理员
    create_manage_edit()#批量创建编辑权限管理员
    create_manage_delete()#批量创建删除权限管理员
    create_manage_all()#批量创建读、编辑、删除权限管理员
   
def admin_athority_check():
    
    global base_url
    global cfg 
    global driver
    base_url = "http://www.beta.ablesky.com/"
    # base_url = "http://www.ablesky-a.com:8080/"
    cfg_file = 'config.ini'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file)
    # user_name = "v52"
    # user_psw = "1234"    
    user_name = "offcn"
    user_psw = "1234"

    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
    driver.get("%smyOffice.do" %(base_url))
    driver.maximize_window() #窗口最大化

    #后台-先创建管理员    
    create_manage()
    driver.quit()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    admin_athority_check()
    