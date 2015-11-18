# -*- coding: UTF-8 -*-
'''
Created on Dec 19, 2014

@author: liwen
'''
import unittest,  ConfigParser, os, time

from selenium import webdriver
from PO.base import Base
import login
import HTMLTestRunner

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.browser = "Chrome"
        self.cfg_file = 'config.ini'
        self.cfg = ConfigParser.RawConfigParser()
        self.cfg.read(self.cfg_file)
        self.verificationErrors = []
        self.org_name = self.cfg.get("env_para", "org_name")
        self.org_password = self.cfg.get("env_para", "org_password")
        self.user_name = self.cfg.get("env_para", "user_name")
        self.user_password = self.cfg.get("env_para", "user_password")
        self.base_url = self.cfg.get("env_para", "base_url")
        self.independent_url = self.cfg.get("env_para","independent_url")

        if self.browser == 'ie':
            self.driver = webdriver.Ie()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser == 'Chrome':
#            chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#            os.environ["webdriver.chrome.driver"] = chromedriver
#            self.driver = webdriver.Chrome(chromedriver)
            self.driver = webdriver.Chrome()
        elif self.browser == "Html":
            self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
        else:
            self.driver = webdriver.Ie()

        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
            
##    @unittest.skip("test")    
#    def test_register(self):
#        ba = Base(self.driver)
#        user_name = ""
#        user_name = login.auto_register(self.cfg, self.driver, self.base_url, 2, 1)
#        if user_name:
#            self.cfg.set("env_para", "import_name", user_name)
#            self.cfg.write(open(self.cfg_file, "w"))    
#        filename = ba.save_screenshot()
#        print "image:"+filename
    
#    @unittest.skip("test")    
    def test_register_domain(self):
        ba = Base(self.driver)
        user_name = ""
        user_name = login.auto_register(self.cfg, self.driver, self.independent_url, 1, 3)
     
        filename = ba.save_screenshot()
        print "image:"+filename
        
##    @unittest.skip("test")    
#    def test_logandout_domain(self):
#        ba = Base(self.driver)
#        login.login_by_independent_domian(self.cfg, self.driver, self.independent_url, self.user_name, self.user_password)
#        login.logout_by_independent_domian(self.driver, self.independent_url)
#   
#        filename = ba.save_screenshot()
#        print "image:"+filename

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":

    suite_register = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)
    allsuites = []
    allsuites.append(suite_register)
    alltests = unittest.TestSuite(allsuites)

    fp = file("myreport.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )
    runner.run(alltests)

    cfg_file = 'config.ini'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file)
    cfg.set("env_para", "cookie1", "no")
    cfg.set("env_para", "cookie_stu", "no")
    cfg.write(open(cfg_file, "w"))
        