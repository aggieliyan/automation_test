# -*- coding: UTF-8 -*-

import time

from selenium.webdriver.support.wait import WebDriverWait

import base
from PO.exam_subject_page import SubjectListPage


class ExamStudentListPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self):
		sp = SubjectListPage(self.dr, self.cfg)
		sp.open()
		sp.click_stu_manage()

	def search_student(self, username):
		self.dr.find_element(self.cfg.get('exam', 'user_search_by'), \
			self.cfg.get('exam', 'user_search')).clear()
		#得一个字母一个字母的输入，否则因为输入太快得到的搜索结果不准确
		for letter in username:
			self.dr.find_element(self.cfg.get('exam', 'user_search_by'), \
				self.cfg.get('exam', 'user_search')).send_keys(letter)
			time.sleep(0.1)
		self.dr.find_element(self.cfg.get('exam', 'click_search_by'), \
			self.cfg.get('exam', 'click_search')).send_keys(letter)	

	def click_send_paper(self):
		time.sleep(2)
		self.dr.find_element_by_link_text(u"分发试卷").click()

	def click_close_paper(self):
		self.dr.find_element_by_link_text(u"关闭试卷").click()

	def choose_all_paper(self):
		time.sleep(0.5)
		self.dr.find_element(self.cfg.get('exam', 'open_paper_by'), \
			self.cfg.get('exam', 'open_paper')).click()

	def choose_one_paper(self):
		time.sleep(0.5)
		self.dr.find_elements(self.cfg.get('exam', 'select_one_p_by'), \
			self.cfg.get('exam', 'select_one_p'))[-1].click()

	def click_save(self):
		self.dr.find_element(self.cfg.get('exam', 'open_paper_ok_by'), \
			self.cfg.get('exam', 'open_paper_ok')).click()
		time.sleep(0.1)