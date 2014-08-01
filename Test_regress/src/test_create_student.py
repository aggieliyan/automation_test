# -*- coding: UTF-8 -*-
'''
Created on Oct 23, 2012

@author: yilulu
'''
import student_management,login,ConfigParser
from selenium import webdriver
import os
import admin_management, exam_user_management, new_course_management
import user_management
import time
import exam_paper

def test_create_student():
    
    test_enviroment = "beta"        
    cfg_file = 'config.ini'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file)  

    base_url = "http://www."+test_enviroment+".ablesky.com/"
    driver = webdriver.Firefox()
    stu_txt = r"C:\register_user_list.txt"
    #driver.implicitly_wait(30)
    user_name = "sadm001"
    user_psw = "1234"
    org_name = user_name
    exam_name = u'未作答（主观+客观，收费）'
    for i in range(1):
        print 'wwwwwwwwwwwwwwwwwwwwwww'
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver =  webdriver.Chrome(chromedriver)
        stu_num = 2
        #login.auto_register(cfg, driver, base_url, 2, 1)
        login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
        #student_management.buy_open_num(cfg,driver, base_url, org_name, bnum=1)
        #student_management.import_one_student(cfg,driver, base_url, org_name, stu_name="sunmin1990")
        time.sleep(5)
        #new_course_management.class_redirect(cfg, driver, base_url)
        #student_management.open_course_for_one(cfg,driver,base_url, org_name,stu_num = 1)
        #student_management.open_course_for_multi(cfg,driver,base_url, org_name)
        #student_management.manage_course_num(cfg, driver, base_url)
        #exam_paper.send_close_paper(cfg, driver, base_url, atype=1)
        #exam_paper.exam_result(cfg, driver, base_url, exam_name, etype=1, username="sun123")
        #exam_paper.exam_result(cfg, driver, base_url, exam_name, etype=2, username="sun125")
        #exam_paper.exam_result(cfg, driver, base_url, exam_name, etype=3, username="sun123")
        #exam_paper.send_close_paper(cfg, driver, base_url, atype=1)
        #exam_paper.send_close_paper(cfg, driver, base_url, atype=2)
        #exam_user_management.buy_paper(cfg, driver)
        #user_management.release_href_course(cfg, driver, base_url, org_name)
        #user_management.release_announcement(cfg,driver, base_url, org_name, title="aaa")
        #user_management.org_chang_headpic(cfg, driver, base_url, org_name)
        #admin_management.auto_create_admin(cfg,driver, base_url, org_name="zhongyan", adm_num=2)
        admin_management.modify_admin(cfg,driver, base_url)
        admin_management.delete_admin(cfg,driver, base_url, admin_num=1)
        #time.sleep(10)
        #student_management.auto_create_student(cfg, driver, base_url, user_name, stu_num)
        #student_management.import_multi_student(cfg,driver, base_url, org_name, stu_txt)
        driver.quit()
    
if __name__ == "__main__":
 
    test_create_student()