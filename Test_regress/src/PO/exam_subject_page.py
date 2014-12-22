# -*- coding: UTF-8 -*-
import time

from selenium.webdriver.support.wait import WebDriverWait

import base
from myoffice_page import MyOfficePage

class SubjectListPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self):
		self.dr.get("%sexam/" %(self.base_url))

	#试卷库
	def click_exampaper(self):
		self.dr.find_element_by_link_text(u"试卷库").click()

	#试题库
	def click_examquestion(self):
		pass

	#学员管理
	def click_stu_manage(self):
		self.dr.find_element(self.cfg.get('exam', 'stu_manage_by'), \
			self.cfg.get('exam', 'stu_manage')).click()
