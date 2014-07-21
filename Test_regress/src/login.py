# -*- coding: UTF-8 -*-
'''
Created on Jun 15, 2012

@author: yilulu
'''
import time,random
from selenium.webdriver.common.by import By
#从网站首页登录
#参数：drivere对象，用户名和密码
def login_by_as(cfg, driver, base_url, user_name, user_psw):
    
    driver.get(base_url + "index.do")
    driver.find_element_by_link_text('登录').click()
    time.sleep(2)
    driver.find_element_by_id('J_loginUsername').send_keys(user_name)
    #driver.find_element_by_id(cfg.get('as_index','login_username_id')).send_keys(user_name)
    driver.find_element_by_id(cfg.get('as_index','login_psw_id')).send_keys(user_psw)
    driver.find_element_by_css_selector(cfg.get('as_index','login_btn_xpath')).click()
    time.sleep(2)   
    
#从搜索页面登陆
def login_by_search(cfg, driver,test_enviroment,user_name, user_psw):
    
    driver.get("http://s." + test_enviroment + ".ablesky.com/s.do?aft=Course")
    time.sleep(2)
    driver.find_element_by_link_text("登录").click()
    time.sleep(2)
    driver.find_element_by_name(cfg.get('search','login_username_name')).send_keys(user_name)
    driver.find_element_by_name(cfg.get('search','login_psw_name')).send_keys(user_psw)
    driver.find_element_by_css_selector(cfg.get('search','login_btn_css')).click()
    time.sleep(2) 
    
#从独立域名登录
#参数：driverenium对象，独立域名地址、用户名和密码
def login_by_independent_domian(cfg,driver,independent_url,user_name,user_psw):
    
    driver.get(independent_url)
    driver.find_element_by_id(cfg.get('org_index','login_popup_id')).click()
    driver.find_element_by_id(cfg.get('org_index','login_username_id')).send_keys(user_name)
    driver.find_element_by_id(cfg.get('org_index','login_psw_id')).send_keys(user_psw)
    driver.find_element_by_xpath(cfg.get('org_index','login_btn_xpath')).click()
    time.sleep(2)

def login_by_logindo(cfg,driver, base_url,user_name, user_psw):
    
    driver.get(base_url + "login.do")
    driver.find_element_by_id(cfg.get('login','login_username_id')).send_keys(user_name)
    driver.find_element_by_id(cfg.get('login','login_psw_id')).send_keys(user_psw)
    driver.find_element_by_id(cfg.get('login','login_btn_id')).click()
    time.sleep(2)
        
#从独立域名退出
#参数：driverenium对象，独立域名地址、用户名和密码    
def logout_by_independent_domian(driver,independent_url):
    
    driver.get(independent_url)
    time.sleep(2)
    driver.find_element_by_link_text("退出").click()
    time.sleep(1)
    
def logout(driver,base_url):
    
    driver.get(base_url)
    driver.find_element_by_link_text(u"[退出]").click()
    time.sleep(1)
    
def is_element_present(driver,how, what):
    try: driver.find_element(by=how, value=what)
    except Exception, e: return False
    return True 


#email注册   
def register_by_email_index(cfg,driver, base_url,r_username, r_email, r_psw):
    
    driver.get(base_url + "/index.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"注册").click()
    #driver.find_element_by_id(cfg.get('as_index','register_email_type_id')).click()
    driver.find_element_by_id(cfg.get('as_index','register_email_uid')).clear()
    driver.find_element_by_id(cfg.get('as_index','register_email_uid')).send_keys(r_username)
    driver.find_element_by_id(cfg.get('as_index','register_email_id')).clear()
    driver.find_element_by_id(cfg.get('as_index','register_email_id')).send_keys(r_email)
    driver.find_element_by_id(cfg.get('as_index','register_email_psw_id')).clear()
    driver.find_element_by_id(cfg.get('as_index','register_email_psw_id')).send_keys(r_psw)
    driver.find_element_by_id(cfg.get('as_index','register_email_confirm_psw_id')).clear()
    driver.find_element_by_id(cfg.get('as_index','register_email_confirm_psw_id')).send_keys(r_psw)
    driver.find_element_by_id("J_iCode").send_keys("aaaa")
    time.sleep(3)
    driver.find_element_by_css_selector(cfg.get('as_index','register_email_submit_css')).click()
    time.sleep(6)
    try:
        logout(driver,base_url,r_username)
    except:
        print 'pass'
        
#手机注册        
def register_by_mobile_index(cfg,driver, base_url,r_username, r_mobile, r_psw):
    
    driver.get(base_url + "/index.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"注册").click()
    driver.find_element_by_id(cfg.get('as_index','register_mobile_type_id')).click()
    driver.find_element_by_id(cfg.get('as_index','register_mobile_uid')).clear()
    driver.find_element_by_id(cfg.get('as_index','register_mobile_uid')).send_keys(r_username)
    driver.find_element_by_id(cfg.get('as_index','register_mobile_number_id')).clear()
    driver.find_element_by_id(cfg.get('as_index','register_mobile_number_id')).send_keys(r_mobile)
    driver.find_element_by_id(cfg.get('as_index','register_mobile_psw_id')).clear()
    driver.find_element_by_id(cfg.get('as_index','register_mobile_psw_id')).send_keys(r_psw)
    driver.find_element_by_id(cfg.get('as_index','register_mobile_confirm_psw_id')).clear()
    driver.find_element_by_id(cfg.get('as_index','register_mobile_confirm_psw_id')).send_keys(r_psw)
    driver.find_element_by_css_selector(cfg.get('as_index','register_mobile_getverify_css')).click()
    driver.find_element_by_id("J_imessageCode").send_keys("aaaa")    
    time.sleep(3) 
    driver.find_element_by_xpath(cfg.get('as_index','register_mobile_submit_xpath')).click()
    time.sleep(6)
    try:
        logout(driver,base_url,r_username)
    except:
        print 'pass'

#自动注册 
def auto_register(cfg,driver, base_url,r_num):
    
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    user_file = open(r"D:/register_user_list.txt",'w')
    for i in range(r_num):
        r_username = 'testlogin_' + prefix + str(i) 
        r_email = r_username+"@sohu.com"
        r_mobile = '15858565555'
        r_psw = '1234aa'
      
        #register_by_mobile_index(cfg,driver, base_url,r_username, r_mobile, r_psw)
        register_by_email_index(cfg,driver, base_url,r_username, r_email, r_psw)
        
        #except Exception,info:
            #print info
        if i== 0:
            user_name = r_username
        else:
            user_file.writelines(r_username+"\n") 
        
    user_file.close()  
    return user_name

#独立域名注册


