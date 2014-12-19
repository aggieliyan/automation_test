# -*- coding: UTF-8 -*-
import unittest, ConfigParser, random, time, os, logging, MySQLdb
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestRunner

from PO.base import Base
import login
import exam_paper, exam_questions, exam_cate_management
import exam_user_management

class ExamTest(unittest.TestCase):

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
            self.cfg.set("env_para", "cookie1", str(self.driver.get_cookie('ASUSS')['value']))
            self.cfg.write(open(self.cfg_file, "w"))
           
            #本来还有一个叫RM的cookie，但是值都是rm不变所以不取了
            # path=/; domain=.ablesky.com
        else:
            self.driver.add_cookie({'name':'ASUSS', 'value':cookie1, 'path':'/', 'domain':'.ablesky.com'})
            self.driver.add_cookie({'name':'RM', 'value':'rm'})
    @unittest.skip("test")
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
        try:
            exam_questions.import_questions(self.cfg, self.driver, self.template)
        except Exception, e:
            print traceback.format_exc() 
            self.verificationErrors.append("fail to import questions..")
        finally:
            self.driver.save_screenshot("C:/test_rs_pic/create_paper.png")
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

    @unittest.skip("test")#暂时只支持ie
    def test_auto_exam_onequestion(self):
        ba = Base(self.driver)
        title = "exam" + ba.rand_name()
        exam_questions.auto_exam_onequestion(self.cfg, self.driver, self.base_url, question_ansa=title, onetype=7)
        filename = ba.save_screenshot()
        print "image:"+filename

    @unittest.skip("test")#暂时只支持ie
    def test_auto_exam_questions(self):
        ba = Base(self.driver)
        title = "exam" + ba.rand_name()
        exam_questions.auto_exam_questions(self.cfg, self.driver, self.base_url, question_ansa=title, num=1)
        filename = ba.save_screenshot()
        print "image:"+filename
    @unittest.skip("test")
    def test_exam_create_subject(self):
        subject_name = exam_cate_managementpo.auto_create_subject(self.cfg, self.driver, self.base_url, self.org_name, sub_num = 1)
        lastsubject = self.driver.execute_script("return $('.subject-name').eq(-1).text()")
        self.assertEqual(subject_name, lastsubject)
        ba.save_screenshot()


    @unittest.skip("test")
    def test_exam_modify_subject(self):
        subject_name = exam_cate_managementpo.modify_subject(self.cfg,self.driver, self.base_url, self.org_name)
        lastsubject = self.driver.execute_script("return $('.subject-name').eq(-1).text()")
        self.assertEqual(subject_name, lastsubject)
        ba.save_screenshot()


    @unittest.skip("test")
    def test_exam_delete_subject(self):
        ba = Base(self.driver)
        #统计科目总数
        total_num = self.driver.execute_script("return $('.subject-item-con').size()")
        exam_cate_managementpo.delete_subject(self.cfg, self.driver, self.base_url, self.org_name)
        last_num == self.driver.execute_script("return $('.subject-item-con').size()")
        self.assertEqual(total_num - 1, last_num)
        ba.save_screenshot()
        

    @unittest.skip("test")
    def test_exam_create_cate():
        cate_name = exam_cate_managementpo.auto_create_exam_cate(cfg, driver, base_url, org_name, cate_num = 1)

    @unittest.skip("test")
    def test_exam_create_subject(self):
        subject_name = exam_cate_managementpo.auto_create_subject(self.cfg, self.driver, self.base_url, self.org_name, sub_num = 1)
        lastsubject = self.driver.execute_script("return $('.subject-name').eq(-1).text()")
        self.assertEqual(subject_name, lastsubject)
        ba.save_screenshot()


    @unittest.skip("test")
    def test_exam_modify_subject(self):
        subject_name = exam_cate_managementpo.modify_subject(self.cfg,self.driver, self.base_url, self.org_name)
        lastsubject = self.driver.execute_script("return $('.subject-name').eq(-1).text()")
        self.assertEqual(subject_name, lastsubject)
        ba.save_screenshot()


    @unittest.skip("test")
    def test_exam_delete_subject(self):
        ba = Base(self.driver)
        #统计科目总数
        total_num = self.driver.execute_script("return $('.subject-item-con').size()")
        exam_cate_managementpo.delete_subject(self.cfg, self.driver, self.base_url, self.org_name)
        last_num == self.driver.execute_script("return $('.subject-item-con').size()")
        self.assertEqual(total_num - 1, last_num)
        ba.save_screenshot()        

    @unittest.skip("test")
    def test_exam_create_cate():
        cate_name = exam_cate_managementpo.auto_create_exam_cate(cfg, driver, base_url, org_name, cate_num = 1)
        
    def test_createpaper(self):
        #免得创建试卷失败后，后面要用到这个变量会失败
        self.paper_name = ""
        try:
            self.paper_name = exam_paper.auto_createpaper(self.cfg, self.driver, self.base_url, 1 , 1, 1, 2, 1, 1) 
        except Exception, e:
            print traceback.format_exc() 
            self.verificationErrors.append("fail to create paper")
        finally:
            self.driver.save_screenshot("C:/test_rs_pic/create_paper.png")
            
    def test_random_paper(self):
        try:
            exam_paper.auto_createpaper(self.cfg, self.driver, self.base_url, 1 , 1, 1, 1, 2) 
        except Exception, e:
            print traceback.format_exc() 
            self.verificationErrors.append("fail to create random paper")
        finally:
            self.driver.save_screenshot("C:/test_rs_pic/create_random_paper.png")

    def tearDown(self):
        self.driver.quit()

