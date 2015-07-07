# -*- coding: UTF-8 -*-
'''
Created on Sep. 24, 2012

@author: yilulu
'''

import unittest,  ConfigParser, os, time

from selenium import webdriver

import login, user_management, card_management, exam_user_management
from PO.base import Base

class StudentTest(unittest.TestCase):

    def setUp(self):

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
        
    #充值卡
    def test_use_prepaidcard(self):
        p_card_num = self.cfg.get("env_para", "p_card_num")
        p_card_pwd = self.cfg.get("env_para", "p_card_pwd")
        if p_card_num != 0 and p_card_pwd != 0:
            confirm_num = card_management.use_prepaidorcate_card(self.cfg, self.driver, self.base_url, p_card_num, p_card_pwd)
        else:
            print u"没有获取到卡充值卡号或者密码"
           
        ba = Base(self.driver)
        filename = ba.save_screenshot()
        print "image:"+filename       
        self.assertEqual(p_card_num, confirm_num)
   
    #充课卡    
    def test_use_coursecard(self):
        c_card_num = self.cfg.get("env_para", "c_card_num")
        c_card_pwd = self.cfg.get("env_para", "c_card_pwd")
        if c_card_num != 0 and c_card_pwd != 0:
            confirm_num = card_management.use_prepaidorcate_card(self.cfg, self.driver, self.base_url, c_card_num, c_card_pwd)
        else:
            print u"没有获取到充课卡号或者密码"
           
        ba = Base(self.driver) 
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(c_card_num, confirm_num)

    #补课卡
    def test_use_catecard(self):
        ca_card_num = self.cfg.get("env_para", "ca_card_num")
        ca_card_pwd = self.cfg.get("env_para", "ca_card_pwd")
        if ca_card_num != 0 and ca_card_pwd != 0:
            course_num = card_management.use_course_card(self.cfg, self.driver, self.base_url, ca_card_num, ca_card_pwd)
        else:
            print u"没有获取到补课卡号或者密码"

        ba = Base(self.driver)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(ca_card_num, course_num)       

    #试听卡
    def test_use_listencard(self):
       l_card_num = self.cfg.get("env_para", "l_card_num")
       l_card_pwd = self.cfg.get("env_para", "l_card_pwd")
       if l_card_num != 0 and l_card_pwd != 0:
           login.login_by_logindo(self.cfg, self.driver, self.base_url, l_card_num, l_card_pwd)
       else:
           print u"没有获取到试听卡号或者密码"
           
       time.sleep(2)     
       confirm_ok = self.driver.execute_script("return $('.mode-selected').text()")
       ba = Base(self.driver)
       filename = ba.save_screenshot()
       print "image:"+filename
       self.assertEqual(u"绑定手机", confirm_ok)

    #使用考试卡  
    def test_use_exam_card(self):
        examcard_num = self.cfg.get("env_para", "examcard_num")
        if examcard_num != 0:
            academy_catename = card_management.user_usexamcard(self.cfg, self.driver, self.base_url, examcard_num)
        else:
            print u"没有获取到考试卡号"

        ba = Base(self.driver)            
        time.sleep(5)         
        academy_catename_ok = self.driver.execute_script("return $('.exampaper-title:eq(1)').text()")#获取已考完的第一个试卷名称
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(academy_catename_ok, academy_catename)

    def tearDown(self):
        self.driver.quit()