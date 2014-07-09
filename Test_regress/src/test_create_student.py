'''
Created on Oct 23, 2012

@author: yilulu
'''
import student_management,login,ConfigParser
from selenium import webdriver

def test_create_student():
    
    test_enviroment = "omega"        
    cfg_file = 'config.ini'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file)  

    base_url = "http://www."+test_enviroment+".ablesky.com/"
    driver = webdriver.Firefox()
    #driver.implicitly_wait(30)
    user_name = "zhongyan"
    user_psw = "1234"
    for i in range(5):
        driver = webdriver.Firefox()
        stu_num = 200
        login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
        student_management.auto_create_student(cfg, driver, base_url, user_name, stu_num)
        driver.quit()
    
if __name__ == "__main__":
 
    test_create_student()