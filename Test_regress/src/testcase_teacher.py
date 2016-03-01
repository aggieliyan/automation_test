# -*- coding: UTF-8 -*-
'''
Created on Dec. 13, 2015

@author: gaoyue
'''

import unittest, ConfigParser, random, time, os, logging
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestRunner

from PO.base import Base
import login, teacher_management

class TeacherTest(unittest.TestCase):
      
    def setUp(self):
        
        self.i = 0
        self.cfg_file = 'config.ini'
        self.cfg = ConfigParser.RawConfigParser()
        self.cfg.read(self.cfg_file)
        self.browser = self.cfg.get("env_para", "browser")
        self.org_name = self.cfg.get("env_para", "org_name")
        self.org_password = self.cfg.get("env_para", "org_password")
        self.user_name = self.cfg.get("env_para", "user_name")
        self.user_password = self.cfg.get("env_para", "user_password")
        self.base_url = self.cfg.get("env_para", "base_url")
        self.dbhost = self.cfg.get("env_para", "dbhost")

        if os.path.exists("C:\\test_rs_pic") != True:
                os.system("mkdir C:\\test_rs_pic")

        if self.browser == 'ie':
            self.driver = webdriver.Ie()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif self.browser == "Html":
            self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
        else:
            self.driver = webdriver.Ie()

        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(self.base_url)

        cookie1 = self.cfg.get('env_para', 'cookie1')
        if(cookie1 == 'no'):
            login.login_by_logindo(self.cfg, self.driver, self.base_url, self.org_name, self.org_password)
            self.cfg.set("env_para", "cookie1", str(self.driver.get_cookie('ASUSS')['value']))
            self.cfg.write(open(self.cfg_file, "w"))
           
            #本来还有一个叫RM的cookie，但是值都是rm不变所以不取了
            # path=/; domain=.ablesky.com
        else:
            self.driver.add_cookie({'name':'ASUSS', 'value':cookie1, 'path':'/', 'domain':'.ablesky.com'})
            self.driver.add_cookie({'name':'RM', 'value':'rm'})
            
    # @unittest.skip("test")
    def test_create_teacher(self):      
        ba = Base(self.driver)
        name = u"teacher" + ba.rand_name()
        try:
           teacher_management.create_teacher(self.cfg, self.driver, tea_name=name)
           time.sleep(2)
        except:   
            while self.i < 2:
                self.i = self.i + 1
                self.test_create_teacher()
           
        get_name = ba.is_element_present("link text", name)
        rs = False
        if get_name:
            rs = True
        else:
            while self.i < 2:
                self.i = self.i + 1
                self.test_create_teacher()
              
        self.assertEqual(True, rs)
        filename = ba.save_screenshot()
        print "image:"+filename
         
    # @unittest.skip("test")
    def test_edit_teacher(self):      
        ba = Base(self.driver)
        time.sleep(2)
        try:
            get_name = self.driver.execute_script("return $('.odd .text-center').eq(1).text()")#取第一个老师
            name = u"teacher" + ba.rand_name()
            teacher_management.edit_teacher(self.cfg, self.driver, tea_name=name)
            time.sleep(1)
            get_name1 = self.driver.execute_script("return $('.odd .text-center').eq(1).text()")#取第一个老师   
        except:      
            while self.i < 2:
                self.i = self.i + 1
                self.test_edit_teacher()
                return
            
        self.assertNotEqual(get_name, get_name1)
        filename = ba.save_screenshot()
        print "image:"+filename
        
    # @unittest.skip("test")
    def test_delete_teacher(self):      
        ba = Base(self.driver)
        time.sleep(2)
        get_name = self.driver.execute_script("return $('.odd .text-center').eq(1).text()")#取第一个老师
        teacher_management.delete_teacher(self.cfg, self.driver)

        get_newname = self.driver.execute_script("return $('.odd .text-center').eq(1).text()")#取第一个老师
        self.assertNotEqual(get_name, get_newname)
        filename = ba.save_screenshot()
        print "image:"+filename

    def tearDown(self): #在每个测试方法执行后调用，这个地方做所有清理工作
        self.driver.quit()

if __name__ == "__main__":

    suite_teacher = unittest.TestLoader().loadTestsFromTestCase(TeacherTest)

    allsuites = []
    allsuites.append(suite_teacher)

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