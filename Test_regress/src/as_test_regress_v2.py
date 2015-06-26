# -*- coding: UTF-8 -*-
'''
Created on Sep. 24, 2012

@author: yilulu
'''
import unittest, ConfigParser, random, time, os, logging, MySQLdb
import traceback
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestRunner

from PO.base import Base
from testcase_student import StudentTest
from testcase_register import RegisterTest
from testcase_exam import ExamTest
from testcase_exam_student import ExamStudentTest
from testcase_exam_result import ExamResultTest
from testcase_course import CourseTest
from testcase_card import StudyCardTest
from testcase_stu_manage import StudentMangeTest
import login, new_course_management, course_management, student_management
import card_management, cate_management, admin_management, user_management
import exam_paper, exam_questions, exam_cate_management
import exam_user_management

class Test(unittest.TestCase):
    

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

        #注册的时候会把第一个值赋给它
        self.import_name = ""

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

    # @unittest.skip("test")
    def test_create_admin(self):
        ba = Base(self.driver)
        aname = admin_management.auto_create_admin(self.cfg, self.driver, adm_num=1)
        # lastadmin = self.driver.execute_script("return $('.floatleft').eq(-10).text()")
        filename = ba.save_screenshot()
        print "image:"+filename
        # self.assertEqual(aname, lastadmin)

    # @unittest.skip("test")
    def test_modify_admin(self):
        ba = Base(self.driver)
        admin_name = admin_management.modify_admin(self.cfg, self.driver, self.base_url)
        filename = ba.save_screenshot()
        print "image:"+filename

    # @unittest.skip("test")
    def test_delete_admin(self):
        ba = Base(self.driver)
        rs = admin_management.delete_admin(self.cfg, self.driver, self.base_url)
        self.assertEqual(True, rs) 
        filename = ba.save_screenshot()
        print "image:"+filename

    # @unittest.skip("test")
    def test_add_cate(self):
        ba = Base(self.driver)
        cate_name = u"cate" + ba.rand_name()
        cate_management.add_cate(self.cfg, self.driver, self.base_url, cate_name=cate_name)
        
        time.sleep(3)          
        actul = self.driver.execute_script("return $(\".categTitleFalse :last\").text()")#取最后一个类目的名称
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(actul, cate_name)

    # @unittest.skip("test")
    def test_delete_cate(self):
        ba = Base(self.driver)
        before_delete = cate_management.delete_cate(self.cfg, self.driver, self.base_url)
        #print before_delete
        time.sleep(1)         
        after_delete = self.driver.execute_script("return $(\".categTitle:last\").text()")#取最后一个类目的名称
        #print after_delete
        rs = (before_delete==after_delete)
        #若删除前后最后一个类目名类不同则证明删除类目成功
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

    # @unittest.skip("test")
    def test_add_course_to_cate(self):
        ba = Base(self.driver)
        course_name = ""
        actual_name = "0"
        course_name = cate_management.add_courese_to_cate(self.cfg, self.driver, self.base_url)

        time.sleep(2)
        actual_name = self.driver.execute_script("return $(\"input[name='course_ckeckbox']:eq(0)\").next().text()")
        actual_name = actual_name.strip()   
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(course_name, actual_name)

    def test_href_announcement(self):
        ba = Base(self.driver)
        title = ba.rand_name()
        user_management.release_href_announcement(self.cfg, self.driver, self.base_url, self.org_name, title)

        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

    # @unittest.skip("test")
    def test_change_homelogo(self):
        ba = Base(self.driver)
        user_management.change_homelogo(self.cfg, self.driver, self.base_url, self.org_name)
        filename = ba.save_screenshot()
        print "image:"+filename
    
    # @unittest.skip("test")
    def test_change_headpic(self):
        ba = Base(self.driver)
        user_management.org_chang_headpic(self.cfg, self.driver, self.base_url, self.org_name)
        filename = ba.save_screenshot()
        print "image:"+filename

    # @unittest.skip("test")
    def test_modify_pagefoot(self):
        ba = Base(self.driver)
        user_management.modify_pagefoot(self.cfg, self.driver, self.base_url, self.org_name)
        filename = ba.save_screenshot()
        print "image:"+filename

        

    def tearDown(self): #在每个测试方法执行后调用，这个地方做所有清理工作
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)
        # fail_num = len(self.verificationErrors)
        # print "total case:%s, %s failures.detail:%s"%(self.total, fail_num, self.verificationErrors)



if __name__ == "__main__":

    suite_register = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test)
    suite_course = unittest.TestLoader().loadTestsFromTestCase(CourseTest)
    suite_card = unittest.TestLoader().loadTestsFromTestCase(StudyCardTest)
    suite_stumanage = unittest.TestLoader().loadTestsFromTestCase(StudentMangeTest)    
    suite2 = unittest.TestLoader().loadTestsFromTestCase(StudentTest)

    #考试部分
    suite_exam = unittest.TestLoader().loadTestsFromTestCase(ExamTest)
    suite_exam_student = unittest.TestLoader().loadTestsFromTestCase(ExamStudentTest)
    suite_exam_result = unittest.TestLoader().loadTestsFromTestCase(ExamResultTest)
    
    allsuites = []
    allsuites.append(suite_register)
    allsuites.append(suite_course)
    allsuites.append(suite_card)
    allsuites.append(suite_stumanage)
    allsuites.append(suite1)
    allsuites.append(suite2)

    #考试部分
    # allsuites.append(suite_exam)
    # allsuites.append(suite_exam_student)
    # allsuites.append(suite_exam_result)

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
    

        

    


    


    

