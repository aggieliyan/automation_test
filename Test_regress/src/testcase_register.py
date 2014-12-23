# -*- coding: UTF-8 -*-
'''
Created on Dec 19, 2014

@author: liwen
'''
import unittest,  ConfigParser, os, time

from selenium import webdriver
from PO.base import Base
import login 

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

        if self.browser == 'ie':
            self.driver = webdriver.Ie()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser == 'Chrome':
            chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(chromedriver)
        elif self.browser == "Html":
            self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
        else:
            self.driver = webdriver.Ie()

        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
            
#    @unittest.skip("test")    
    def test_register(self):
        ba = Base(self.driver)
        user_name = ""
        user_name = login.auto_register(self.cfg, self.driver, self.base_url, 2, 1)
        if user_name:
            self.cfg.set("env_para", "import_name", user_name)
            self.cfg.write(open(self.cfg_file, "w"))    
        filename = ba.save_screenshot()
        print "image:"+filename
    
    def tearDown(self):
        self.driver.quit()
        
        