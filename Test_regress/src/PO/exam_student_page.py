# -*- coding: UTF-8 -*-

import time

from selenium.webdriver.support.wait import WebDriverWait

import base
from PO.exam_subject_page import SubjectListPage
from myoffice_page import MyOfficePage


class ExamStudentListPage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
	
	#进入后台页面
	def open(self):
		op = MyOfficePage(self.dr, self.cfg)
		op.open()
		#self.dr.get("http://www.ablesky.com/myOffice.do ")
		#time.sleep(2)
		#self.dr.find_element_by_class_name("close-btn").click()
		#time.sleep(1)
		
	#点击后台人员
	def click_org_personnel(self):
		self.dr.find_element_by_link_text(u"人员").click()
        time.sleep(2)
        
    #点击后台学员
	def click_org_student(self):
		self.dr.find_element_by_link_text(u"学员").click()
        time.sleep(2)

	#筛选学员user_name
	def click_select_stu(self):
		time.sleep(6)
		self.dr.find_elements(self.cfg.get('manage_course_num', "stu_select_by"), \
							self.cfg.get('manage_course_num', "stu_select"))[0].click()
	def click_selectuser_stu(self):#改xpath
		time.sleep(3)
		self.dr.execute_script("$('ul.cc-itemList li:eq(1)').click()")
#		self.dr.find_elements(self.cfg.get('manage_course_num', "stu_selectuser_by"), \
#							self.cfg.get('manage_course_num', "stu_selectuser")).click()				
	def click_selectinput_stu(self, user_name):
		time.sleep(1)
		self.dr.find_element(self.cfg.get('manage_course_num', 'stu_selectinput_by'), \
							self.cfg.get('manage_course_num', 'stu_selectinput')).send_keys(user_name)
	def click_selectsearch_stu(self):
		self.dr.find_element(self.cfg.get('manage_course_num', "stu_selectsearch_by"), \
							self.cfg.get('manage_course_num', "stu_selectsearch")).click()
		time.sleep(5)
	#点击开通试卷题库
	def click_test_paper(self):
		bh = self.dr.window_handles
		self.dr.find_element_by_link_text(u"开通试卷题库").click()		
		time.sleep(3)

	def click_send_paper(self):
		time.sleep(1)
		self.dr.find_elements(self.cfg.get('exam', 'send_paper_by'), \
			self.cfg.get('exam', 'send_paper'))[0].click()

	def click_close_paper(self):
		time.sleep(1)
		self.dr.find_elements(self.cfg.get('exam', 'close_paper_by'), \
			self.cfg.get('exam', 'close_paper'))[1].click()

	def choose_all_paper(self):
		time.sleep(0.5)
		self.dr.find_element(self.cfg.get('exam', 'open_paper_by'), \
			self.cfg.get('exam', 'open_paper')).click()

	def choose_one_paper(self):
		time.sleep(0.5)
		self.dr.find_elements(self.cfg.get('exam', 'select_one_p_by'), \
			self.cfg.get('exam', 'select_one_p'))[1].click()
			
	def click_close(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam', 'open_paper_close_by'), \
			self.cfg.get('exam', 'open_paper_close')).click()	
		time.sleep(2)	

	def click_save(self):
		time.sleep(0.5)
		self.dr.find_element(self.cfg.get('exam', 'open_paper_ok_by'), \
			self.cfg.get('exam', 'open_paper_ok')).click()
		time.sleep(1)
		#首次开通扣授权弹框确认
		try:
			self.dr.find_element(self.cfg.get('exam','pay_authorization_ok_by'),\
								 self.cfg.get('exam','pay_authorization_ok')).click()
		except:
			pass
		time.sleep(0.1)