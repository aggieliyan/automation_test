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

	def open(self, driver, cfg):
		self.dr.get("%sexam/" %(base_url))

	#试卷库
	def click_exampaper(self):
		self.dr.find_element_by_link_text(u"试卷库").click()

	#创建科目
    def click_create_sub(self):
        self.dr.driver.find_element(cfg.get('exam', 'new_subject_by'), \
        cfg.get('exam', 'new_subject_id')).click()
        driver.implicitly_wait(10)

    #类目管理
    def click_create_cate(self):
        self.dr.driver.find_element_by_link_text(u"类目管理").click()
        self.dr.driver.implicitly_wait(10)

    #考点库
    def click_point_page(self):
        self.dr.driver.find_element_by_link_text(u"考点库").click()
    


	#试题库
	def click_examquestion(self):
		pass

	#学员管理
	def click_stu_manage(self):
		pass