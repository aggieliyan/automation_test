# -*- coding: UTF-8 -*-
import time

import base
from myoffice_page import MyOfficePage


class OnLineClassListPage(base.Base):

	
	def __init__(self, driver, cfg):

		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver

	def open(self):
		m = MyOfficePage(self.dr, self.cfg)
		m.open()
		m.click_teaching()
		m.class_manage()

	def click_create(self):
		self.dr.implicitly_wait(10)
		self.dr.find_element(self.cfg.get('classRedirect', 'redirect_btn_by'), \
			self.cfg.get('classRedirect', 'redirect_btn')).click()

	def click_classface(self):
		time.sleep(1)
		self.dr.find_element(self.cfg.get('classRedirect', 'classface_by'), \
			self.cfg.get('classRedirect', 'classface')).click()

class ClassInfoPage(base.Base):


	def __init__(self, driver, cfg):
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver

	def click_presell(self):
		self.dr.find_element_by_link_text(u"课程预售").click()

	def chooes_course(self):
		time.sleep(30)
		self.dr.find_elements(self.cfg.get('classRedirect', 'select_course_by'), \
			self.cfg.get('classRedirect', 'select_course'))[0].click()

	def choose_cate(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('classRedirect', 'select_cate_by'), \
			self.cfg.get('classRedirect', 'select_cate')).click()

	def input_classname(self, classname):
		ninput = self.dr.find_element(self.cfg.get('classRedirect', 'classname_by'), \
			self.cfg.get('classRedirect', 'classname'))
		ninput.clear()
		ninput.send_keys(classname)
	
	def input_current_price(self, price):
		time.sleep(3)
		current = self.dr.find_element(self.cfg.get('classRedirect', 'current_price_by'), \
			self.cfg.get('classRedirect', 'current_price'))
		current.clear()
		current.send_keys(price)
    	
	def input_price(self, price):
		pinput = self.dr.find_element(self.cfg.get('classRedirect', 'presell_price_by'), \
			self.cfg.get('classRedirect', 'presell_price'))
		pinput.clear()
		pinput.send_keys(price)

	def input_description(self, course_describe):
		self.dr.execute_script("var element=\
			window.document.getElementById('courseDescribe-editor_ifr');\
			idocument=element.contentDocument;\
			element=idocument.getElementById('tinymce');\
			element.innerHTML =\'"+course_describe+"\';")

	def input_tag(self, class_tags):
		self.dr.find_element(self.cfg.get('courseRedirect', 'tags_by'), \
			self.cfg.get('courseRedirect', 'tags')).send_keys(class_tags)

	def click_service_cate(self):
		self.dr.execute_script("$('li.level2').eq(1).click()")
		self.dr.execute_script("$('li.level3').eq(1).click()")
		time.sleep(1)

	def click_save(self):
		self.dr.find_element(self.cfg.get('classRedirect', 'save_btn_by'), \
			self.cfg.get('classRedirect', 'save_btn')).click()
		time.sleep(1)
        
	def input_classadress(self, address):
		self.dr.find_element(self.cfg.get('classRedirect', 'address_by'), \
			self.cfg.get('classRedirect', 'address')).send_keys(address)

	def input_classnum(self, number):
		self.dr.find_element(self.cfg.get('classRedirect', 'number_by'), \
			self.cfg.get('classRedirect', 'number')).send_keys(number)  
