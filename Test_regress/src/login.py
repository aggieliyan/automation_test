# -*- coding: UTF-8 -*-
'''
Created on Jun 15, 2012

@author: yilulu
'''
import time, random
from PO.base import Base
from PO.login_page import LoginPage, IndexPage, SearchPage, IndependentDomianLoginPage, ClickLoginText
from PO.register_page import ClickRegisterText, EmailRegisterPage, PhoneRegisterPage, IndependentAegisterPage 
#从网站首页登录
#参数：drivere对象，用户名和密码
def login_by_as(cfg, driver, base_url, user_name, user_psw):
    indexpage = IndexPage(driver,cfg)    
    indexpage.open()
    
    click = ClickLoginText(driver,cfg)
    click.click_login()
    
    loginpage = LoginPage(driver,cfg)
    loginpage.input_username(user_name)
    loginpage.input_pwd(user_psw)
    loginpage.click_login_btn()
    time.sleep(2)
#从搜索页面登陆
def login_by_search(cfg, driver, test_enviroment, user_name, user_psw):
    driver.get("http://s." + test_enviroment + ".ablesky.com/s.do?aft=Course")
    time.sleep(2)
    click = ClickLoginText(driver,cfg)
    click.click_login()
    
    loginpage = LoginPage(driver,cfg)
    loginpage.input_username(user_name)
    loginpage.input_pwd(user_psw)
    loginpage.click_login_btn()
    time.sleep(2)
#从独立域名登录
#参数：driverenium对象，独立域名地址、用户名和密码
def login_by_independent_domian(cfg, driver, independent_url, user_name, user_psw):
    
    indompage = IndependentDomianLoginPage(driver,cfg)
    indompage.open()
        
    click = ClickLoginText(driver,cfg)
    click.click_login()
    
    loginpage = LoginPage(driver,cfg)
    loginpage.input_username(user_name)
    loginpage.input_pwd(user_psw)
    loginpage.click_login_btn()
    time.sleep(2)
    
def login_by_logindo(cfg, driver, base_url, user_name, user_psw):
    loginpage = LoginPage(driver,cfg)    
    loginpage.open_logindo()
    loginpage.save_screenshot()
    
    loginpage.input_username(user_name)
    loginpage.input_pwd(user_psw)
    loginpage.click_login_btn()
    loginpage.save_screenshot()
    time.sleep(2)
    
def login_by_know(cfg, driver):
    time.sleep(1)
    driver.find_element_by_css_selector("#J_continueGuid > span.greenbtn30_text").click()
    time.sleep(1)
    
#从独立域名退出
#参数：driverenium对象，独立域名地址、用户名和密码
def logout_by_independent_domian(driver,independent_url):
    time.sleep(3)
    driver.find_element_by_link_text(u"退出").click()
    time.sleep(2)
       
def logout(driver, base_url):
    driver.get(base_url)
    time.sleep(1)
    driver.find_element_by_link_text(u"退出").click()
    time.sleep(1)
    
def is_element_present(driver, how, what):
    try: driver.find_element(by=how, value=what)
    except Exception, e: return False
    return True
#email注册
def register_by_email_index(cfg, driver, base_url, r_username, r_email, r_psw):
    clickregister = ClickRegisterText(driver,cfg)
    clickregister.click_register()
    clickregister.save_screenshot()

    registerpage = EmailRegisterPage(driver,cfg)
    em = registerpage.click_emalimod()
    if em == 0:
        registerpage.input_username(r_username)
        registerpage.input_email(r_email)
        registerpage.input_psw(r_psw)
        time.sleep(2)
        registerpage.verification_code()
        time.sleep(8)
        registerpage.save_screenshot()       
#    code = driver.find_element_by_id("J_iCode")
#    code.click()
#    time.sleep(2)
#    put = raw_input(u"请输入验证码:")
#    code.send_keys(put)
#    time.sleep(8)
#    driver.find_element(cfg.get('as_index', 'register_email_submit_by'), \
#                        cfg.get('as_index', 'register_email_submit')).click()
#    time.sleep(6)
        registerpage.register_submit_btn()
        registerpage.save_screenshot()
    else:
        pass

    try:
        logout(driver, base_url)
    except:
        print 'pass'

#手机注册
def register_by_mobile_index(cfg, driver, base_url, r_username, r_mobile, r_psw):

    clickregister = ClickRegisterText(driver,cfg)
    clickregister.click_register()

    registerpage = PhoneRegisterPage(driver,cfg)
    registerpage.input_username(r_username)
    registerpage.input_mobile(r_mobile)
    registerpage.input_psw(r_psw)
    registerpage.get_verification()    
#    registerpage.verification_code()
#    driver.find_element_by_id("J_imessageCode").send_keys(raw_input(u'请输入验证码：')) 
    registerpage.register_submit_btn()
    registerpage.save_screenshot()

    try:
        logout(driver, base_url)
    except:
        print 'pass'
        
#院校注册
def register_college_by_email(cfg, driver, base_url, r_username, r_email, r_mobile, r_psw, reg_type):
    driver.get(base_url + "/")
    time.sleep(2)
    driver.find_element_by_link_text(u"[注册]").click()
    driver.find_element_by_link_text(u"高校用户").click()
    if reg_type == 5:
        driver.find_element(cfg.get('as_index', 'register_college_type_by'), \
                        cfg.get('as_index', 'register_college_type')).click()        
    driver.find_element(cfg.get('as_index', 'register_college_email_username_by'), \
                        cfg.get('as_index', 'register_college_email_username')).click()
    driver.find_element(cfg.get('as_index', 'register_college_email_username_by'), \
                        cfg.get('as_index', 'register_college_email_username')).send_keys(r_username)
    driver.find_element(cfg.get('as_index', 'register_college_email_realname_by'), \
                        cfg.get('as_index', 'register_college_email_realname')).click()
    driver.find_element(cfg.get('as_index', 'register_college_email_realname_by'), \
                        cfg.get('as_index', 'register_college_email_realname')).send_keys("Realname")
    if reg_type == 4:
        driver.find_element(cfg.get('as_index', 'register_college_email_by'), \
                            cfg.get('as_index', 'register_college_email')).click()
        driver.find_element(cfg.get('as_index', 'register_college_email_by'), \
                            cfg.get('as_index', 'register_college_email')).send_keys(r_email)
    else:
        driver.find_element(cfg.get('as_index', 'register_college_mobile_by'), \
                            cfg.get('as_index', 'register_college_mobile')).click()
        driver.find_element(cfg.get('as_index', 'register_college_mobile_by'), \
                            cfg.get('as_index', 'register_college_mobile')).send_keys(r_mobile)        
    driver.find_element(cfg.get('as_index', 'register_college_email_pwd_by'), \
                        cfg.get('as_index', 'register_college_email_pwd')).click()
    driver.find_element(cfg.get('as_index', 'register_college_email_pwd_by'), \
                        cfg.get('as_index', 'register_college_email_pwd')).send_keys(r_psw)
    driver.find_element(cfg.get('as_index', 'register_college_by'), \
                        cfg.get('as_index', 'register_college')).click()
    driver.find_element(cfg.get('as_index', 'register_college_form_by'), \
                        cfg.get('as_index', 'register_college_form')).click()
    time.sleep(2)
    driver.find_element(cfg.get('as_index', 'register_college_selected_by'), \
                        cfg.get('as_index', 'register_college_selected')).click()
    time.sleep(1)
    driver.find_element(cfg.get('as_index', 'register_college_faculty_by'), \
                        cfg.get('as_index', 'register_college_faculty')).click()
    time.sleep(2)
    driver.find_element(cfg.get('as_index', 'register_college_faculty_selected_by'), \
                        cfg.get('as_index', 'register_college_faculty_selected')).click()
    time.sleep(2)                    
    driver.find_element(cfg.get('as_index', 'register_college_specialty_by'), \
                        cfg.get('as_index', 'register_college_specialty')).click()
    driver.find_element(cfg.get('as_index', 'register_college_specialty_selected_by'), \
                        cfg.get('as_index', 'register_college_specialty_selected')).click()
    driver.find_element(cfg.get('as_index', 'register_college_year_by'), \
                        cfg.get('as_index', 'register_college_year')).click()
    driver.find_element(cfg.get('as_index', 'register_college_year_selected_by'), \
                        cfg.get('as_index', 'register_college_year_selected')).click()
    driver.find_element(cfg.get('as_index', 'register_college_edu_by'), \
                        cfg.get('as_index', 'register_college_edu')).click()
    driver.find_element(cfg.get('as_index', 'register_college_edu_selected_by'), \
                        cfg.get('as_index', 'register_college_edu_selected')).click()
    driver.find_element(cfg.get('as_index', 'register_college_num_by'), \
                        cfg.get('as_index', 'register_college_num')).click()
    driver.find_element(cfg.get('as_index', 'register_college_num_by'), \
                        cfg.get('as_index', 'register_college_num')).send_keys("M06000109")
    if reg_type == 4:
        driver.find_element_by_id("J_collegeVerifycode").click()
        driver.find_element_by_id("J_collegeVerifycode").send_keys(raw_input(u'请输入验证码：'))
        time.sleep(8)
    else:
        driver.find_element_by_css_selector("span.show-state.lightgray30_text").click()
        driver.find_element_by_id("J_imessageCode").click()
        driver.find_element_by_id("J_imessageCode").send_keys(raw_input(u'请输入验证码：'))
        time.sleep(8)        
    driver.find_element(cfg.get('as_index', 'register_email_submit_by'), \
                        cfg.get('as_index', 'register_email_submit')).click()
    time.sleep(6)
    try:
        logout(driver, base_url)
    except:
        print 'pass'    
    
#独立域名注册
def register_by_independent_domian(cfg, driver, base_url, r_username, r_email, r_psw):
    indompage = IndependentDomianLoginPage(driver,cfg)
    indompage.open()

    clickregister = ClickLoginText(driver,cfg)
    clickregister.click_register()

    registerpage = EmailRegisterPage(driver,cfg)
    dem = registerpage.click_emailmod_domain()
    if dem == 0:
        registerpage.input_username(r_username)
        registerpage.input_email(r_email)
        registerpage.input_psw(r_psw)
        registerpage.verification_code()
        time.sleep(10)
        registerpage.save_screenshot()
#    #下一步(设置没有下一步填写项)
#    independentreg = IndependentDomianLoginPage(driver,cfg)
#    independentreg.click_next()
#    independentreg.input_realname()
#    # ...
#    # ...
        registerpage.register_submit_btn()
        registerpage.save_screenshot()
    else:
        pass
    time.sleep(2)
    try:
        logout(driver, base_url)
    except:
        print 'pass'

#自动注册 
def auto_register(cfg, driver, base_url, r_num, reg_type):
    """
    reg_type 代表注册方式 1 邮箱注册
                        2 手机注册
                        3 独立域名下注册
                        4 院校邮箱注册
                        5 院校手机注册
    """
    ba = Base(driver)
    prefix = ba.rand_name()
    user_file = open(r"C:/register_user_list.txt", 'w')
    for i in range(r_num):
        r_username = 'testlogin_' + prefix + str(i) 
        r_email = r_username+"@sohu.com"
        r_mobile = '15858565'+ str(random.randint(100, 999))
        r_psw = '1234aa'
        if reg_type == 1:
            register_by_email_index(cfg, driver, base_url, r_username, r_email, r_psw)
        elif reg_type == 2:
            register_by_mobile_index(cfg, driver, base_url, r_username, r_mobile, r_psw)
        elif reg_type == 3:
            register_by_independent_domian(cfg, driver, base_url, r_username, r_email, r_psw)
        else:
            register_college_by_email(cfg, driver, base_url, r_username, r_email, r_mobile, r_psw, reg_type)
            #except Exception,info:
            #print info
        if i == 0:
            user_name = r_username
        else:
            user_file.writelines(r_username+"\n")
    user_file.close()
    return user_name