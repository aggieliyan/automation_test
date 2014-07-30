'''
Created on Oct 23, 2012

@author: yilulu
'''
import student_management,login,ConfigParser
from selenium import webdriver
import os
import admin_management

def test_create_student():
    
    test_enviroment = "beta"        
    cfg_file = 'config.ini'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file)  

    base_url = "http://www."+test_enviroment+".ablesky.com/"
    #driver = webdriver.Firefox()
    #driver.implicitly_wait(30)
    user_name = "zhongyan"
    user_psw = "1234"
    org_name = user_name
    for i in range(1):
        print 'wwwwwwwwwwwwwwwwwwwwwww'
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver =  webdriver.Chrome(chromedriver)
        stu_num = 2
        login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
        #admin_management.auto_create_admin(cfg,driver, base_url, org_name="zhongyan", adm_num=2)
        admin_management.modify_admin(cfg,driver, base_url, org_name)
        admin_management.delete_admin(cfg,driver, base_url, org_name, admin_num=1)
        time.sleep(10)
        #login.auto_register(cfg, driver, base_url, 2, 1)
        #student_management.auto_create_student(cfg, driver, base_url, user_name, stu_num)
        driver.quit()
    
if __name__ == "__main__":
 
    test_create_student()