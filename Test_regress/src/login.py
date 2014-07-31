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
    driver.find_element(cfg.get('login','login_username_by'),cfg.get('login','login_username')).send_keys(user_name)
    #driver.find_element_by_id(cfg.get('as_index','login_username_id')).send_keys(user_name)
    driver.find_element(cfg.get('login','login_psw_by'),cfg.get('login','login_psw')).send_keys(user_psw)
    driver.find_element(cfg.get('login','login_btn_by'),cfg.get('login','login_btn')).click()
    time.sleep(2)   
    
#从搜索页面登陆
def login_by_search(cfg, driver,test_enviroment,user_name, user_psw):
    
    driver.get("http://s." + test_enviroment + ".ablesky.com/s.do?aft=Course")
    time.sleep(2)
    driver.find_element_by_link_text('登录').click()
    time.sleep(2)
    driver.find_element(cfg.get('search','login_username_by'),cfg.get('search','login_username')).send_keys(user_name)
    driver.find_element(cfg.get('search','login_psw_by'),cfg.get('search','login_psw')).send_keys(user_psw)  
    driver.find_element(cfg.get('search','login_btn_by'),cfg.get('search','login_btn')).click()
    time.sleep(2) 
    
#从独立域名登录
#参数：driverenium对象，独立域名地址、用户名和密码
def login_by_independent_domian(cfg,driver,independent_url,user_name,user_psw):
    
    driver.get(independent_url)
    driver.find_element(cfg.get('org_index','login_popup_by'),cfg.get('org_index','login_popup')).click()
    driver.find_element(cfg.get('org_index','login_username_by'),cfg.get('org_index','login_username')).send_keys(user_name)
    driver.find_element(cfg.get('org_index','login_psw_by'),cfg.get('org_index','login_psw')).send_keys(user_psw)
    driver.find_element(cfg.get('org_index','login_btn_by'),cfg.get('org_index','login_btn')).click()
    time.sleep(2)

def login_by_logindo(cfg,driver, base_url,user_name, user_psw):
    
    driver.get(base_url + "login.do")
    driver.find_element(cfg.get('login','login_username_by'),cfg.get('login','login_username')).send_keys(user_name)
    driver.find_element(cfg.get('login','login_psw_by'),cfg.get('login','login_psw')).send_keys(user_psw)
    driver.find_element(cfg.get('login','login_btn_by'),cfg.get('login','login_btn')).click()
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
    time.sleep(1)
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
    driver.find_element(cfg.get('as_index','register_email_username_by'),cfg.get('as_index','register_email_username')).clear()
    driver.find_element(cfg.get('as_index','register_email_username_by'),cfg.get('as_index','register_email_username')).send_keys(r_username)
    driver.find_element(cfg.get('as_index','register_email_by'),cfg.get('as_index','register_email')).clear()
    driver.find_element(cfg.get('as_index','register_email_by'),cfg.get('as_index','register_email')).send_keys(r_email)
    driver.find_element(cfg.get('as_index','register_email_psw_by'),cfg.get('as_index','register_email_psw')).clear()
    driver.find_element(cfg.get('as_index','register_email_psw_by'),cfg.get('as_index','register_email_psw')).send_keys(r_psw)
    driver.find_element(cfg.get('as_index','register_email_confirm_psw_by'),cfg.get('as_index','register_email_confirm_psw')).clear()
    driver.find_element(cfg.get('as_index','register_email_confirm_psw_by'),cfg.get('as_index','register_email_confirm_psw')).send_keys(r_psw)
    #driver.find_element_by_id("J_iCode").send_keys("aaaa")
    time.sleep(8)
    driver.find_element(cfg.get('as_index','register_email_submit_by'),cfg.get('as_index','register_email_submit')).click()
    time.sleep(6)
    try:
        logout(driver,base_url)
    except:
        print 'pass'
        
#手机注册        
def register_by_mobile_index(cfg,driver, base_url,r_username, r_mobile, r_psw):
    
    driver.get(base_url + "/index.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"注册").click()
    driver.find_element(cfg.get('as_index','register_mobile_type_by'),cfg.get('as_index','register_mobile_type')).click()
    driver.find_element(cfg.get('as_index','register_mobile_username_by'),cfg.get('as_index','register_mobile_username')).clear()
    driver.find_element(cfg.get('as_index','register_mobile_username_by'),cfg.get('as_index','register_mobile_username')).send_keys(r_username)
    driver.find_element(cfg.get('as_index','register_mobile_number_by'),cfg.get('as_index','register_mobile_number')).clear()
    driver.find_element(cfg.get('as_index','register_mobile_number_by'),cfg.get('as_index','register_mobile_number')).send_keys(r_mobile)
    driver.find_element(cfg.get('as_index','register_mobile_psw_by'),cfg.get('as_index','register_mobile_psw')).clear()
    driver.find_element(cfg.get('as_index','register_mobile_psw_by'),cfg.get('as_index','register_mobile_psw')).send_keys(r_psw)
    driver.find_element(cfg.get('as_index','register_mobile_confirm_psw_by'),cfg.get('as_index','register_mobile_confirm_psw')).clear()
    driver.find_element(cfg.get('as_index','register_mobile_confirm_psw_by'),cfg.get('as_index','register_mobile_confirm_psw')).send_keys(r_psw)
    driver.find_element(cfg.get('as_index','register_mobile_getverify_by'),cfg.get('as_index','register_mobile_getverify')).click()
    #driver.find_element_by_id("J_imessageCode").send_keys("aaaa")    
    time.sleep(8) 
    driver.find_element(cfg.get('as_index','register_mobile_submit_by'),cfg.get('as_index','register_mobile_submit')).click()
    time.sleep(2)
    try:
        logout(driver,base_url)
    except:
        print 'pass'

#独立域名注册
def register_by_independent_domian(cfg,driver,base_url,r_username, r_email, r_psw):
    driver.get(base_url + "/")
    time.sleep(2)
    driver.find_element_by_link_text(u"[注册]").click()
    driver.find_element(cfg.get('as_index','register_email_username_by'),cfg.get('as_index','register_email_username')).clear()
    driver.find_element(cfg.get('as_index','register_email_username_by'),cfg.get('as_index','register_email_username')).send_keys(r_username)
    driver.find_element(cfg.get('as_index','register_email_by'),cfg.get('as_index','register_email')).clear()
    driver.find_element(cfg.get('as_index','register_email_by'),cfg.get('as_index','register_email')).send_keys(r_email)
    driver.find_element(cfg.get('as_index','register_email_psw_by'),cfg.get('as_index','register_email_psw')).clear()
    driver.find_element(cfg.get('as_index','register_email_psw_by'),cfg.get('as_index','register_email_psw')).send_keys(r_psw)
    driver.find_element(cfg.get('as_index','register_email_confirm_psw_by'),cfg.get('as_index','register_email_confirm_psw')).clear()
    driver.find_element(cfg.get('as_index','register_email_confirm_psw_by'),cfg.get('as_index','register_email_confirm_psw')).send_keys(r_psw)
    #driver.find_element_by_id("J_iCode").send_keys("aaaa")
    time.sleep(10)
    #下一步
    driver.find_element(cfg.get('as_index','register_email_next_by'),cfg.get('as_index','register_email_next')).click()
    time.sleep(3)
    driver.find_element(cfg.get('as_index','register_email_realname_by'),cfg.get('as_index','register_email_realname')).clear()
    driver.find_element(cfg.get('as_index','register_email_realname_by'),cfg.get('as_index','register_email_realname')).send_keys(u"真实姓名")
    driver.find_element(cfg.get('as_index','register_email_mobile_by'),cfg.get('as_index','register_email_mobile')).clear()
    driver.find_element(cfg.get('as_index','register_email_mobile_by'),cfg.get('as_index','register_email_mobile')).send_keys(u"1588881100")
    driver.find_element(cfg.get('as_index','register_email_address_by'),cfg.get('as_index','register_email_address')).clear()
    driver.find_element(cfg.get('as_index','register_email_address_by'),cfg.get('as_index','register_email_address')).send_keys(u"地址啊")
    driver.find_element(cfg.get('as_index','register_email_code_by'),cfg.get('as_index','register_email_code')).clear()
    driver.find_element(cfg.get('as_index','register_email_code_by'),cfg.get('as_index','register_email_code')).send_keys(u"055550")
    driver.find_element_by_css_selector("a.select-btn.ablesky-colortip-right").click()
    time.sleep(2)
    driver.find_element(cfg.get('as_index','register_email_school_by'),cfg.get('as_index','register_email_school')).click()
    driver.find_element_by_xpath("//form[@id='J_nextStopForm']/dl[6]/dd/a").click()
    time.sleep(2)
    driver.find_element(cfg.get('as_index','register_email_age_by'),cfg.get('as_index','register_email_age')).click()
    driver.find_element(cfg.get('as_index','register_email_qq_by'),cfg.get('as_index','register_email_qq')).clear()
    driver.find_element(cfg.get('as_index','register_email_qq_by'),cfg.get('as_index','register_email_qq')).send_keys(u"529111129")
    driver.find_element(cfg.get('as_index','register_email_year_by'),cfg.get('as_index','register_email_year')).clear()
    driver.find_element(cfg.get('as_index','register_email_year_by'),cfg.get('as_index','register_email_year')).send_keys(u"2013")
    driver.find_element(cfg.get('as_index','register_email_submit_by'),cfg.get('as_index','register_email_submit')).click()
    time.sleep(2)
    try:
        logout(driver,base_url)
    except:
        print 'pass'
    
    
#自动注册 
def auto_register(cfg,driver, base_url,r_num, reg_type):
    """
    reg_type 代表注册方式 1 邮箱注册
                        2 手机注册
                        3 独立域名下注册
    """
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    user_file = open(r"C:/register_user_list.txt",'w')
    for i in range(r_num):
        r_username = 'testlogin_' + prefix + str(i) 
        r_email = r_username+"@sohu.com"
        r_mobile = '15858565'+ str(random.randint(100,999))
        r_psw = '1234aa'

        if reg_type == 1:
            register_by_email_index(cfg,driver, base_url,r_username, r_email, r_psw)
        elif reg_type == 2:
            register_by_mobile_index(cfg,driver, base_url,r_username, r_mobile, r_psw)
        elif reg_type == 3:
            register_by_independent_domian(cfg,driver, base_url,r_username, r_email, r_psw)
        
        #except Exception,info:
            #print info
        if i== 0:
            user_name = r_username
        else:
            user_file.writelines(r_username+"\n") 
        
    user_file.close()  
    return user_name