# -*- coding: UTF-8 -*-
'''
Created on Dec. 24, 2014
@author:liuhongjiao
'''


import unittest, ConfigParser, random, time, os, logging, MySQLdb
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestRunner

from PO.base import Base
import login, student_management

class StudentMangeTest(unittest.TestCase):
    
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
             
    #导入一个学员
    def test_import_one_student(self):
        ba = Base(self.driver)
        #导入的学员为注册生成的学员
        #stu_name = self.cfg.get("env_para", "import_name")
        stu_name = student_management.import_one_student(self.cfg, self.driver, self.base_url)
        filename = ba.save_screenshot()
        print "image:"+filename
        #验证
        self.driver.refresh()
        #获取第一个学员的用户名
        time.sleep(3)
        self.driver.execute_script("$('li.alt-info-link').eq(0).click()")
        time.sleep(3)
        stuname_one = self.driver.execute_script("return $('.field-title').eq(1).text()")
        if stuname_one != stu_name:        
            rs = False
        else:
            rs = True
        self.assertEqual(True, rs)

    # 注：以后机构不能批量导入学员了，只有超管可以
    # 导入多个学员
    # def test_import_multi_student(self):
    #     ba = Base(self.driver)
    #     student_management.import_multi_student(self.cfg, self.driver, self.base_url, r"C:\register_user_list.txt")
    #     filename = ba.save_screenshot()
    #     print "image:"+filename

    #创建学员
    def test_auto_create_student(self):
        ba = Base(self.driver)
        stu_num = 1
        student_management.auto_create_student(self.cfg, self.driver, self.base_url, stu_num)
        filename = ba.save_screenshot()
        print "image:"+filename

    #给一个学员开通课程
    def test_open_course_for_one(self):
        ba = Base(self.driver)
        student_management.open_course_for_one(self.cfg, self.driver, self.base_url)
        filename = ba.save_screenshot()
        print "image:"+filename

    #给多个学员开通课程
    def test_open_course_for_multi(self):
        ba = Base(self.driver)
        student_management.open_course_for_multi(self.cfg, self.driver, self.base_url)
        filename = ba.save_screenshot()
        print "image:"+filename

    #管理学员播放授权数
    def test_manage_course_num(self):
        ba = Base(self.driver)
        student_management.manage_course_num(self.cfg, self.driver, self.base_url, self.user_name)
        filename = ba.save_screenshot()
        print "image:"+filename

    #购买授权(线上不走购买授权)
    def test_buy_open_num(self):
        ba = Base(self.driver)
        if self.base_url == "http://www.ablesky.com/":
            return
        else:
            student_management.buy_open_num(self.cfg, self.driver, self.base_url)
            filename = ba.save_screenshot()
            print "image:"+filename

    def tearDown(self): #在每个测试方法执行后调用，这个地方做所有清理工作
        self.driver.quit()

if __name__ == "__main__":
    suite_stumanage = unittest.TestLoader().loadTestsFromTestCase(StudentMangeTest) 
    allsuites = []
    allsuites.append(suite_stumanage)
    alltests = unittest.TestSuite(suite_stumanage)

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