# -*- coding: UTF-8 -*-
'''
Created on Sep. 24, 2012

@author: yilulu
'''
import unittest, ConfigParser, random, time, os, logging, MySQLdb
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestRunner

from PO.base import Base
from testcase_student import StudentTest
from testcase_register import RegisterTest
from testcase_exam import ExamTest
from testcase_exam_student import ExamStudentTest
import login, new_course_management, course_management, student_management
import card_management, cate_management, admin_management, user_management
import exam_paper, exam_questions, exam_cate_management
import exam_user_management

class Test(unittest.TestCase):
    

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
        self.total = 0


        #一些使用卡相关变量，前置条件：管理员先创建卡，给变量赋值，用户才可获取卡号登录使用卡号
        #充值卡-卡号、密码
        self.p_card_num = 0
        self.p_card_pwd = 0
        #充课卡-卡号、密码
        self.c_card_num = 0
        self.c_card_pwd = 0
        #补课卡-卡号、密码
        self.ca_card_num = 0
        self.ca_card_pwd = 0
        #试听卡-考号、密码
        self.l_card_num = 0
        self.l_card_pwd = 0
        #考试卡-卡号
        self.examcard_num = 0

        #注册的时候会把第一个值赋给它
        self.import_name = ""

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
 
    # @unittest.skip("test")
    def test_release_normal_course(self):      
        ba = Base(self.driver)
        title = "course" + ba.rand_name()
        new_course_management.course_redirect(self.cfg, self.driver, self.base_url, course_title=title, course_price=10)
        
        rs = ba.is_element_present("link text", u"查看课程")
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

     

        # self.normal_course = title#待用-在数据库中查是否转换失败

          
        #取链接待后面购买
        # course_href = self.driver.execute_script("return $(\"a:contains(\'"+title+"\')\").attr('href')")
        # time.sleep(1)
        # if course_href:
        #     self.course_href = self.base_url + course_href
        # else:
        #     self.course_href = ""

    # @unittest.skip("test")
    def test_release_three_video(self):
        ba = Base(self.driver)
        title = "coursethree" + ba.rand_name()
        new_course_management.course_redirect(self.cfg, self.driver, self.base_url, course_title=title)
        
        rs = ba.is_element_present("link text", u"查看课程")
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

    # @unittest.skip("test")
    def test_release_two_video(self):
        ba = Base(self.driver)
        title = "two_video" + ba.rand_name()
        new_course_management.course_redirect(self.cfg, self.driver, self.base_url, course_title=title, course_price=10)
        
        rs = ba.is_element_present("link text", u"查看课程")
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

    # @unittest.skip("test")
    def test_presaleclass(self):
        ba = Base(self.driver)
        title = "presaleclass" + ba.rand_name()
        new_course_management.class_redirect(self.cfg, self.driver, self.base_url, ctype=2, classname=title)

        course = self.driver.find_element("link text", title)
        #若发课成功了取出课程链接存入文件中供后面的购买流程用
        rs = False
        if course:
            rs = True
            self.cfg.set("env_para", "course_href1", course.get_attribute("href"))
            self.cfg.write(open(self.cfg_file, "w"))
        
        filename = ba.save_screenshot()
        print "image:"+filename

        self.assertEqual(True, rs)

    # @unittest.skip("test")
    def test_onlineclass(self):
        ba = Base(self.driver)
        title = "onlineclass" + ba.rand_name()
        new_course_management.class_redirect(self.cfg, self.driver, self.base_url, classname=title)

        # rs = ba.is_element_present("link text", title)
        course = self.driver.find_element("link text", title)
        #若发课成功了取出课程链接存入文件中供后面的购买流程用
        rs = False
        if course:
            rs = True
            self.cfg.set("env_para", "course_href2", course.get_attribute("href"))
            self.cfg.write(open(self.cfg_file, "w"))

        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

    # @unittest.skip("test")
    def test_agency_course(self):
        ba = Base(self.driver)
        title = "agency" + ba.rand_name()
        new_course_management.release_agency_course(self.cfg, self.driver, self.base_url, course_title=title)

        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

    # @unittest.skip("test")
    def test_create_admin(self):
        ba = Base(self.driver)
        aname = admin_management.auto_create_admin(self.cfg, self.driver, adm_num=1)
        lastadmin = self.driver.execute_script("return $('.floatleft').eq(-10).text()")
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(aname, lastadmin)
        
    def test_add_cate(self):
        ba = Base(self.driver)
        cate_name = u"cate" + ba.rand_name()
        cate_management.add_cate(self.cfg, self.driver, self.base_url, cate_name=cate_name)
        
        time.sleep(2)          
        actul = self.driver.execute_script("return $(\".categTitleFalse :last\").text()")#取最后一个类目的名称
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(actul, cate_name)

    def test_delete_cate(self):
        ba = Base(self.driver)
        before_delete = cate_management.delete_cate(self.cfg, self.driver, self.base_url)
        #print before_delete
        time.sleep(1)         
        after_delete = self.driver.execute_script("return $(\".categTitle:last\").text()")#取最后一个类目的名称
        #print after_delete
        rs = (before_delete==after_delete )
        #若删除前后最后一个类目名类不同则证明删除类目成功
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

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
        
    #充值卡 
    def test_prepaid_cardgroup(self):#充值卡
        ba = Base(self.driver)
        title = u"prepaid" + ba.rand_name()
        price = 100
        #建卡组
        card_management.add_prepaid_cardgroup(self.cfg, self.driver, self.base_url, self.org_name, group_name=title, group_price=price)
         
        self.driver.implicitly_wait(10)
        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename        
        self.assertEqual(True, rs)
        #建卡,取考号密码
        if rs == True:
            card_info = self.add_and_get_card()
            self.p_card_num = card_info[0]
            self.p_card_pwd = card_info[1]
            self.cfg.set("env_para", "p_card_num", self.p_card_num)
            self.cfg.set("env_para", "p_card_pwd", self.p_card_pwd)
            self.cfg.write(open(self.cfg_file, "w"))

    #添加卡组-充课卡   
    def test_course_cardgroup(self):
        ba = Base(self.driver)
        title = u"course" + ba.rand_name()
        card_management.add_course_cardgroup(self.cfg, self.driver, self.base_url, self.org_name, group_name=title)

        self.driver.implicitly_wait(10)
        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)
        #建卡,取考号密码
        if rs == True:
            card_info = self.add_and_get_card(1)#充课卡需要传参数
            self.c_card_num = card_info[0]
            self.c_card_pwd = card_info[1]
            self.cfg.set("env_para", "c_card_num", self.c_card_num)
            self.cfg.set("env_para", "c_card_pwd", self.c_card_pwd)
            self.cfg.write(open(self.cfg_file, "w"))
        
     #添加卡组-补课卡         
    def test_cate_cardgroup(self):
        ba = Base(self.driver)
        title = u"cate" + ba.rand_name()
        card_management.add_cate_cardgroup(self.cfg, self.driver, self.base_url, self.org_name, title)

        self.driver.implicitly_wait(10)
        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)
        #建卡,取考号密码
        if rs == True:
            card_info = self.add_and_get_card()
            self.ca_card_num = card_info[0]
            self.ca_card_pwd = card_info[1]
            self.cfg.set("env_para", "ca_card_num", self.ca_card_num)
            self.cfg.set("env_para", "ca_card_pwd", self.ca_card_pwd)
            self.cfg.write(open(self.cfg_file, "w"))
        
    #购买试听卡
    def test_buy_listen_card(self):
        ba = Base(self.driver)
        card_management.buy_listen_card(self.cfg, self.driver, self.base_url)
        
        time.sleep(2)
        payok = self.driver.execute_script("return $('.page-headline').text()").strip()
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual("付款成功！", payok)
        
    #添加试听卡组
    def test_listen_cardgroup(self):
        ba = Base(self.driver)
        title = u"listen" + ba.rand_name()
        card_management.add_listen_cardgroup(self.cfg, self.driver, self.base_url, self.org_name, group_name=title)

        self.driver.implicitly_wait(10)
        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)
        #建卡,取考号密码
        if rs == True:
            card_info = self.add_and_get_card()
            self.l_card_num = card_info[0]
            self.l_card_pwd = card_info[1]
            self.cfg.set("env_para", "l_card_num", self.l_card_num)
            self.cfg.set("env_para", "l_card_pwd", self.l_card_pwd)
            self.cfg.write(open(self.cfg_file, "w"))
        

    def add_and_get_card(self, card_type=0):#添加卡并返回第一个卡号和密码
        ba = Base(self.driver)
        card_prifix = "c" + ba.rand_name()
        card_management.add_card(self.cfg, self.driver, self.base_url, self.org_name, card_prifix)
        if card_type == 0:
            time.sleep(3)
            self.driver.find_element_by_link_text(u"浏览卡").click()
            time.sleep(2)
            card_num = self.driver.execute_script("return $(\"input[name='groupCheck']:eq(0)\").parent().next().text()")
            time.sleep(2)
            card_pwd = self.driver.execute_script("return $(\".textaligncenter\:eq(4)\").text()")
            time.sleep(2) 
        else:
            time.sleep(3)                
            self.driver.find_element_by_css_selector("span.greenbtn35_text").click()
            time.sleep(2)
            card_num = self.driver.execute_script("return $(\"input[type='checkbox']:eq(1)\").parent().text()")
            time.sleep(2)
             #print 'card_num:',card_num
            card_pwd = self.driver.execute_script("return $(\"input[type='checkbox']:eq(1)\").parent().parent().next().children().text()") 
            time.sleep(2)
   
        return card_num, card_pwd

    @unittest.skip("test") 
    #添加考试卡并返回第一个卡号
    def test_add_exam_card(self):
        ba = Base(self.driver)
        count = 5
        academy = "qqhru"
        self.examcard_num = card_management.add_exam_card(self.cfg, self.driver, self.base_url, count, academy)
        self.cfg.set("env_para", "examcard_num", self.examcard_num)
        self.cfg.write(open(self.cfg_file, "w"))
        if self.examcard_num == None:
           rs = False
        else:
           rs = True  
        filename = ba.save_screenshot()
        print "image:"+filename       
        self.assertEqual(True, rs)

    @unittest.skip("test")
    #导入一个学员
    def test_import_one_student(self):
        ba = Base(self.driver)
        stu_name = "exam3996"#还是固定的学员，以后改成注册那生成的学员
        student_management.import_one_student(self.cfg, self.driver, self.base_url, stu_name)
        filename = ba.save_screenshot()
        print "image:"+filename
        #验证
        self.driver.refresh()
        time.sleep(5)
        ts = ba.is_element_present(By.XPATH, "//span[@title=\'"+stu_name+"\']")
        if ts == False:
            rs = False
        else:
            rs = True
        self.assertEqual(True, rs)

    @unittest.skip("test")
    #导入多个学员
    def test_import_multi_student(self):
        ba = Base(self.driver)
        student_management.import_multi_student(self.cfg, self.driver, self.base_url, r"C:\register_user_list.txt")
        filename = ba.save_screenshot()
        print "image:"+filename

    @unittest.skip("test")
    #创建学员
    def test_auto_create_student(self):
        ba = Base(self.driver)
        stu_num = 1
        student_management.auto_create_student(self.cfg, self.driver, self.base_url, stu_num)
        filename = ba.save_screenshot()
        print "image:"+filename

    @unittest.skip("test")
    #给一个学员开通课程
    def test_open_course_for_one(self):
        ba = Base(self.driver)
        student_management.open_course_for_one(self.cfg, self.driver, self.base_url)
        filename = ba.save_screenshot()
        print "image:"+filename

    @unittest.skip("test")
    #给多个学员开通课程
    def test_open_course_for_multi(self):
        ba = Base(self.driver)
        student_management.open_course_for_multi(self.cfg, self.driver, self.base_url)
        filename = ba.save_screenshot()
        print "image:"+filename

    @unittest.skip("test")
    #管理学员播放授权数
    def test_manage_course_num(self):
        ba = Base(self.driver)
        student_management.manage_course_num(self.cfg, self.driver, self.base_url, self.user_name)
        filename = ba.save_screenshot()
        print "image:"+filename

    @unittest.skip("test")
    #购买授权
    def test_buy_open_num(self):
        ba = Base(self.driver)
        student_management.buy_open_num(self.cfg, self.driver, self.base_url)
        filename = ba.save_screenshot()
        print "image:"+filename

    # @unittest.skip("test")
    def test_add_announcement(self):
        ba = Base(self.driver)

        title = ba.rand_name()
        user_management.release_announcement(self.cfg, self.driver, self.base_url, self.org_name, title)

        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

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
    #import sys;sys.argv = ['', 'Test.testName']
    # unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(Test("test_release_normal_course"))
    # testsuite.addTest(Test("test_create_admin"))
    # testsuite = unittest.TestLoader().loadTestsFromTestCase(Test)
    suite_register = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(StudentTest)
    suite_exam = unittest.TestLoader().loadTestsFromTestCase(ExamTest)
    suite_exam_student = unittest.TestLoader().loadTestsFromTestCase(ExamStudentTest)
    allsuites = []
    allsuites.append(suite_register)
    allsuites.append(suite1)
    allsuites.append(suite2)
    allsuites.append(suite_exam)
    allsuites.append(suite_exam_student)    

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
    

        

    


    


    

