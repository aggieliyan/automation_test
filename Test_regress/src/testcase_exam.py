# -*- coding: UTF-8 -*-
'''
Created on 2014-12-20
@author: guoyuling
modified on Dec. 24, 2014
@author: liuhongjiao
added: test_import_questions
       test_auto_exam_onequestion
       test_auto_exam_questions
'''

import unittest, ConfigParser, random, time, os, logging, MySQLdb
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestRunner

from PO.base import Base
from PO.exam_subject_page import SubjectListPage 
from PO.exam_cate_page import ExamCateListPage
from PO.exam_point_page import ExamPointListPage
import login, time
import exam_paper, exam_questions, exam_cate_management
import exam_user_management

class ExamTest(unittest.TestCase):

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

        cookie1 = self.cfg.get('env_para', 'cookie1')
        if(cookie1 == 'no'):
            login.login_by_logindo(self.cfg, self.driver, self.base_url, self.org_name, self.org_password)
            self.cfg.set("env_para", "cookie1", \
                str(self.driver.get_cookie('ASUSS')['value']))
            self.cfg.write(open(self.cfg_file, "w"))
           
            #本来还有一个叫RM的cookie，但是值都是rm不变所以不取了
            # path=/; domain=.ablesky.com
        else:
            self.driver.add_cookie({'name':'ASUSS', 'value':cookie1, 'path':'/', 'domain':'.ablesky.com'})
            self.driver.add_cookie({'name':'RM', 'value':'rm'})

    #@unittest.skip("test")
    def test_import_questions(self):
        ba = Base(self.driver)
        self.template = '\\\data.ablesky.com\workspace\Testing\Testing Files\Automation_test\createquestions.xls'
        #建立数据库连接查询当前试题总数并关闭连接,否则下面的查询会有缓存
        db = 'ablesky_examsystem'
        conn = ba.connect_db(self.dbhost, db)
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM e_question_q"
        cursor.execute(sql)
        num1 = cursor.fetchall()[0][0]
        cursor.close()
        #调用导入试题
        exam_questions.import_questions(self.cfg, self.driver, self.template)
        filename = ba.save_screenshot()
        print "image:"+filename
        #重新建立数据库,查询导入试题后的总数,二者差即为导入总数
        conn = ba.connect_db(self.dbhost, db)
        cursor = conn.cursor()
        cursor.execute(sql)
        num2 = cursor.fetchall()[0][0]
        num = num2 - num1
        cursor.execute \
            ("SELECT content_q,content_q FROM e_question_q ORDER BY id_q DESC LIMIT 1")
        title = cursor.fetchall()[0][0]
        msg = u"导入%d道试题,最后一个试题题目为%s"%(num, title)
        print msg
        self.assertEqual(6, num)

    #@unittest.skip("test")#暂时只支持ie
    def test_auto_exam_onequestion(self):
        ba = Base(self.driver)
        title = "exam" + ba.rand_name()
        exam_questions.auto_exam_onequestion(self.cfg, self.driver, self.base_url, question_ansa=title, onetype=7)
        filename = ba.save_screenshot()
        print "image:"+filename

    #@unittest.skip("test")#暂时只支持ie
    def test_auto_exam_questions(self):
        ba = Base(self.driver)
        title = "exam" + ba.rand_name()
        exam_questions.auto_exam_questions(self.cfg, self.driver, self.base_url, question_ansa=title, num=1)
        filename = ba.save_screenshot()
        print "image:"+filename


    #@unittest.skip("test")
    def test_exam_create_subject(self):
        ba = Base(self.driver)
        subject_name = exam_cate_management.auto_create_subject(self.cfg, self.driver, self.base_url, self.org_name, sub_num = 1)
        time.sleep(1)
        lastsubject = self.driver.execute_script("return $('.subject-name').eq(-1).text()")
        self.assertEqual(subject_name, lastsubject)
        filename = ba.save_screenshot()
        print "image:"+filename


    #@unittest.skip("test")
    def test_exam_modify_subject(self):
        ba = Base(self.driver)
        subject_name = exam_cate_management.modify_subject(self.cfg, self.driver, self.base_url, self.org_name)
        time.sleep(1)
        lastsubject = self.driver.execute_script("return $('.subject-name').eq(1).text()")
        self.assertEqual(subject_name, lastsubject)
        filename = ba.save_screenshot()
        print "image:"+filename


    #@unittest.skip("test")
    def test_exam_delete_subject(self):
        ba = Base(self.driver)
        #统计科目总数
        time.sleep(1)
        total_num = exam_cate_management.delete_subject(self.cfg, self.driver, self.base_url, self.org_name)
        time.sleep(1)
        last_num = self.driver.execute_script("return $('.subject-item-con').size()")
        self.assertEqual(total_num - 1, last_num)
        filename = ba.save_screenshot()
        print "image:"+filename
        

    #@unittest.skip("test")
    def test_exam_create_cate(self):
        ba = Base(self.driver)
        cate_name = exam_cate_management.auto_create_exam_cate(self.cfg, self.driver, self.base_url, self.org_name, cate_num = 1)
        time.sleep(1)
        lastcate = self.driver.execute_script("return $('.categTitleFalse').eq(-1).text()")
        self.assertEqual(cate_name, lastcate)
        filename = ba.save_screenshot()
        print "image:"+filename

       
    #@unittest.skip("test")
    def test_exam_modify_cate(self):
        ba = Base(self.driver)
        cate_name = exam_cate_management.modify_exam_cate(self.cfg, self.driver, self.base_url, self.org_name)
        time.sleep(1)
        lastcate = self.driver.execute_script("return $('.categTitleFalse').eq(1).text()")
        self.assertEqual(cate_name, lastcate)
        filename = ba.save_screenshot()
        print "image:"+filename


    #@unittest.skip("test")
    def test_exam_delete_cate(self):
        ba = Base(self.driver)
        time.sleep(1)
        #total_num = self.driver.execute_script("return $('.categTitleFalse').size()")
        total_num = exam_cate_management.delete_exam_cate(self.cfg, self.driver, self.base_url, self.org_name)
        time.sleep(1)
        last_num = self.driver.execute_script("return $('.categTitleFalse').size()")
        self.assertEqual(total_num - 1, last_num)
        filename = ba.save_screenshot()
        print "image:"+filename        



    # @unittest.skip("test")
    def test_exam_create_point(self):
        ba = Base(self.driver)
        point_name = exam_cate_management.auto_create_exam_point(self.cfg, self.driver, self.base_url, self.org_name, point_num = 1)
        time.sleep(1)
        lastpoint = self.driver.execute_script("return $('.categTitleFalse').eq(-1).text()")
        self.assertEqual(point_name, lastpoint)
        filename = ba.save_screenshot()
        print "image:"+filename

    #@unittest.skip("test")
    def test_exam_modify_point(self):
        ba = Base(self.driver)
        point_name = exam_cate_management.modify_exam_point(self.cfg, self.driver, self.base_url, self.org_name)
        time.sleep(2)
        lastpoint = self.driver.execute_script("return $('.categTitleFalse').eq(0).text()")
        time.sleep(2)
        self.assertEqual(point_name, lastpoint)
        filename = ba.save_screenshot()
        print "image:"+filename

    #@unittest.skip("test")
    def test_exam_delete_point(self):
        ba = Base(self.driver)
        total_num = exam_cate_management.delete_exam_point(self.cfg, self.driver, self.base_url, self.org_name)
        time.sleep(1)
        last_num = self.driver.execute_script("return $('.categTitleFalse').size()")
        self.assertEqual(total_num - 1, last_num)
        filename = ba.save_screenshot()
        print "image:"+filename
        
    
   
    #@unittest.skip("test")
    def test_send_paper(self):
        ba = Base(self.driver)
        exam_paper.send_close_paper(self.cfg, self.driver, self.base_url, self.user_name, atype=1)
        filename = ba.save_screenshot()
        print "image:"+filename

    #@unittest.skip("test")
    def test_close_paper(self):
        ba = Base(self.driver)
        exam_paper.send_close_paper(self.cfg, self.driver, self.base_url, self.user_name, atype=2)
        filename = ba.save_screenshot()
        print "image:"+filename 

    #@unittest.skip("test")    
    def test_createpaper(self):
        #免得创建试卷失败后，后面要用到这个变量会失败
        ba = Base(self.driver)
        self.paper_name = ""
        self.paper_name = exam_paper.auto_createpaper(self.cfg, self.driver, self.base_url, 1 , 1, 1, 2, 1, 1)
               
        self.cfg.set("env_para", "paper_name", str(self.paper_name))
        self.cfg.write(open(self.cfg_file, "w"))        
        filename = ba.save_screenshot()
        print "image:"+filename

        
    #@unittest.skip("test")        
    def test_random_paper(self):
        ba = Base(self.driver)
        exam_paper.auto_createpaper(self.cfg, self.driver, self.base_url, 1 , 1, 1, 1, 1, 2) 
        filename = ba.save_screenshot()
        print "image:"+filename

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    # unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(Test("test_release_normal_course"))
    # testsuite.addTest(Test("test_create_admin"))
    # testsuite = unittest.TestLoader().loadTestsFromTestCase(Test)
    #suite1 = unittest.TestLoader().loadTestsFromTestCase(Test)
    #suite2 = unittest.TestLoader().loadTestsFromTestCase(StudentTest)
    suite_exam = unittest.TestLoader().loadTestsFromTestCase(ExamTest)
    allsuites = []
    #allsuites.append(suite1)
    #allsuites.append(suite2)
    allsuites.append(suite_exam)
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
