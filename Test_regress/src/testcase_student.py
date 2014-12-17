# -*- coding: UTF-8 -*-
'''
Created on Sep. 24, 2012

@author: yilulu
'''

import unittest,  ConfigParser, os

from selenium import webdriver

import login, user_management
from PO.base import Base

class StudentTest(unittest.TestCase):
    @unittest.skip("test")
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

        cookie1 = self.cfg.get('env_para', 'cookie_stu')     
        if(cookie1 == 'no'):
            login.login_by_logindo(self.cfg, self.driver, self.base_url, self.user_name, self.user_password)
            self.cfg.set("env_para", "cookie_stu", str(self.driver.get_cookie('ASUSS')['value']))
            self.cfg.write(open(self.cfg_file, "w"))
            
            #本来还有一个叫RM的cookie，但是值都是rm不变所以不取了
            # path=/; domain=.ablesky.com
        else:
            self.driver.add_cookie({'name':'ASUSS', 'value':cookie1, 'path':'/', 'domain':'.ablesky.com'})
            self.driver.add_cookie({'name':'RM', 'value':'rm'})
    @unittest.skip("test")
    def test_buy_course_use_RMB(self):
        course_href = self.cfg.get("env_para", "course_href1")
        if course_href != '0':
            user_management.buy_course(self.cfg, self.driver, self.base_url, course_href)
        else:
            print u"没有购买链接"
        ba = Base(self.driver)

        rs = ba.is_element_present("id", "J_studycenter")
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

        ba.save_screenshot()
    @unittest.skip("test")
    def test_buy_course_use_card(self):
        course_href = self.cfg.get("env_para", "course_href2")
        if course_href != '0':
            user_management.buy_course_usecard(self.cfg, self.driver, self.base_url, course_href)
        else:
            print u"没有购买链接"
        ba = Base(self.driver)

        rs = ba.is_element_present("id", "J_studycenter")
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)
        
        ba.save_screenshot()

    def tearDown(self):
        self.driver.quit()