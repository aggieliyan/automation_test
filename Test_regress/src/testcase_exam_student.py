# -*- coding: UTF-8 -*-
'''
Created on Sep. 24, 2012

@author: yilulu
'''

import unittest,  ConfigParser, os, time

from selenium import webdriver

import login, user_management, card_management, exam_user_management
from PO.base import Base

class ExamStudentTest(unittest.TestCase):

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

        if os.path.exists("C:\\test_rs_pic") != True:
                os.system("mkdir C:\\test_rs_pic")

        if self.browser == 'ie':
            self.driver = webdriver.Ie()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser == 'Chrome':
            # chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
            # os.environ["webdriver.chrome.driver"] = chromedriver
            # self.driver = webdriver.Chrome(chromedriver)
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

    def test_buy_paper(self):
        ba = Base(self.driver)
        paper_url = self.cfg.get("env_para", "paper_url")
        exam_user_management.buy_paper(self.cfg, self.driver, paper_url)
        filename = ba.save_screenshot()
        print "image:"+filename

    #学员参加考试
    def test_exam_user(self):
        ba = Base(self.driver)
        # operation = '0' 自动提交  operation = '1' 继续答题
        operation = '1'
        question_answer ='123'
        # blank_pager=1是交白卷 ；blank_pager=0 是做了一个题
        blank_pager = 0
#        paper_name = self.paper_name
        paper_name = self.cfg.get("env_para", "paper_name")
        exam_user_management.exam_user(self.cfg, self.driver, self.base_url, operation, blank_pager, question_answer, paper_name)

        time.sleep(2)
        paper_name_ok = self.driver.execute_script("return $('.exampaper-title:eq(0)').text()")#获取已考完的第一个试卷名称
        filename = ba.save_screenshot()
        print "image:"+filename 
        self.assertEqual(paper_name, paper_name_ok)



    def tearDown(self):
        self.driver.quit()