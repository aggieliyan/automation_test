# -*- coding: UTF-8 -*-
'''
Created on Apr 29, 2014

@author: yilulu
'''
import unittest
import random
import os
import ConfigParser
import login
import traceback
import new_course_management
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException

class Test(unittest.TestCase):


    def setUp(self):
        self.browser = "Chrome"
        self.test_enviroment = "beta" 
        self.org_name = "sadm001"
        self.org_password = "1234"
        self.base_url = "http://www."+self.test_enviroment+".ablesky.com/"
        
        #记录页面元素的文件
        cfg_file = 'config.ini'
        self.cfg = ConfigParser.RawConfigParser()
        self.cfg.read(cfg_file)
        
        #浏览器
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver =  webdriver.Chrome(chromedriver)


    def tearDown(self):
        self.driver.quit()


    def testName(self):
        
        #登录
        login.login_by_logindo(self.cfg, self.driver, self.base_url, self.org_name, self.org_password)
        
    
        for i in range(1000):
            try:
                rand_name = str(random.randint(1000,9999))
                title =u"course"+rand_name  
                # 发单视频        
                new_course_management.course_redirect(self.cfg, self.driver, self.base_url, course_title=title)
                #三分屏
                title =u"threecourse"+rand_name
                new_course_management.course_redirect(self.cfg, self.driver, self.base_url, isthree=1, course_title=title)
            except UnexpectedAlertPresentException:
                self.driver.switch_to_alert().accept()
                traceback.print_exc()
                print i
                continue
            except Exception:
                traceback.print_exc()
                print i
                continue
            
                
           

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()