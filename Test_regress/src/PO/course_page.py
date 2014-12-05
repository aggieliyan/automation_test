# -*- coding: UTF-8 -*-
'''
Created on Dec. 03, 2014

@author: yilulu
'''
import time

import base

class CourseStepOnePage(base.Base):

	def __init__(self, driver, cfg):

		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver


	def open(self):
		url = "%s/coursePostRedirect.do?action=courseStepOne"%(self.base_url)
		self.dr.get(url)

	def choose_three_video(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'threevideo_by'), \
			self.cfg.get('courseRedirect', 'threevideo')).click()	

	def click_upload(self, i):
		self.dr.find_elements(self.cfg.get('courseRedirect', 'upload_btn_by'), \
			self.cfg.get('courseRedirect', 'upload_btn'))[i].click()
		time.sleep(1)

	def choose_flv(self):
		self.dr.execute_script("$(\"[filetype='flv']\").eq(0).click()")#选一个视频课件
		time.sleep(1)

	def choose_pdf(self):
		self.dr.execute_script("$(\"[filetype='pdf']\").eq(0).click()")#选一个pdf课件
		time.sleep(1)

	def click_choose_ok(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'select_ok_by'), \
			self.cfg.get('courseRedirect', 'select_ok')).click()

	def click_next_step(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'next_btn_by'), \
			self.cfg.get('courseRedirect', 'next_btn')).click()

class CourseInfoPage(base.Base):

	def __init__(self, driver, cfg):
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver

	def input_course_title(self, ctitle):
		c_input = self.dr.find_element(self.cfg.get('courseRedirect', 'ctitle_by'), \
			self.cfg.get('courseRedirect', 'ctitle'))
		c_input.clear()
		c_input.send_keys(ctitle)

	def click_charge(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'chanrge_by'), \
			self.cfg.get('courseRedirect', 'chanrge')).click()

	def input_price(self, cprice):
		self.dr.find_element(self.cfg.get('courseRedirect', 'price_by'), \
			self.cfg.get('courseRedirect', 'price')).send_keys(cprice)

	def input_description(self, cdescription ):
		self.dr.execute_script("var element=\
			window.document.getElementById('courseDesc-editor_ifr');\
			idocument=element.contentDocument;\
			element=idocument.getElementById('tinymce');\
			element.innerHTML =\'"+cdescription+"\';")
		time.sleep(1)

	def click_service_cate(self):
		self.dr.execute_script("$(\'li.level2\').click()")
		self.dr.execute_script("$(\'li.level3.selected\').click()")
		time.sleep(1)

	def input_tag(self, course_tags):
		self.dr.find_element(self.cfg.get('courseRedirect', 'tags_by'), \
			self.cfg.get('courseRedirect', 'tags')).send_keys(course_tags)

	def click_save(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'done_btn_by'), \
			self.cfg.get('courseRedirect', 'done_btn')).click()

