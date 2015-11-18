# -*- coding: UTF-8 -*-
'''
Created on Dec. 03, 2014

@author: yilulu
'''
import time

from selenium.webdriver.support.wait import WebDriverWait

import base
from myoffice_page import MyOfficePage

class CourseStepOnePage(base.Base):


	def __init__(self, driver, cfg):

		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver

	def open(self):
		url = "%s/course/manage/create"%(self.base_url)
		self.dr.get(url)

	def input_course_title(self, ctitle):
		c_input = self.dr.find_element(self.cfg.get('courseRedirect', 'ctitle_by'), \
			self.cfg.get('courseRedirect', 'ctitle'))
		c_input.clear()
		c_input.send_keys(ctitle)

	def click_service_cate(self):
		self.dr.execute_script("$(\'li.level2\').click()")
		self.dr.execute_script("$(\'li.level3.selected\').click()")
		time.sleep(0.1)

	#点创建进入下一步
	def click_next_step(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'next_btn_by'), \
			self.cfg.get('courseRedirect', 'next_btn')).click()

class CuorsefilePage(base.Base):
	def __init__(self, driver, cfg):
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver

	def click_know(self):
		time.sleep(1)
		self.dr.find_element("id", "J_know").click()

	def click_add_classhour(self, cnum):
		self.dr.find_elements_by_link_text(u"课时")[cnum].click()
		time.sleep(0.5)

	def click_add_chapter(self):
		self.dr.find_element_by_link_text(u"章").click()

	def click_add_section(self):
		self.dr.find_element_by_link_text(u"节").click()
		time.sleep(1)

	def click_singlevideo(self):#点击弹出上传框
		self.dr.find_element_by_link_text(u"单视频").click()
		time.sleep(1)

	def choose_three_video(self):
		# self.dr.find_elements("class name", "tvql")[0].click()
		self.dr.find_elements(self.cfg.get('courseRedirect', 'choose_three_by'), \
			self.cfg.get('courseRedirect', 'choose_three'))[0].click()		

	def input_cname(self, cnum=0):
		# self.dr.find_element("class name", "saveTitle").send_keys("threecoursehour")
		self.dr.find_elements(self.cfg.get('courseRedirect', 'cname_by'), \
			self.cfg.get('courseRedirect', 'cname'))[cnum].send_keys("threecoursehour")
		time.sleep(0.5)

	def click_add(self, cno):
		time.sleep(2)
		self.dr.find_elements_by_link_text(u"添加")[cno].click()

	def choose_flv(self):
		time.sleep(2)
		self.dr.execute_script("$(\"[filetype='flv']\").eq(0).click()")#选一个视频课件
		time.sleep(0.1)

	def choose_pdf(self):
		time.sleep(2)
		self.dr.execute_script("$(\"[filetype='pdf']\").eq(0).click()")#选一个pdf课件
		time.sleep(0.1)

	def click_choose_ok(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'select_ok_by'), \
			self.cfg.get('courseRedirect', 'select_ok')).click()
		time.sleep(1)

	def click_save(self):
		time.sleep(1)
		self.dr.find_element_by_link_text(u"保存").click()
		time.sleep(0.5)

	def click_info(self):
		time.sleep(2)
		self.dr.find_element_by_link_text(u"基本信息").click()

class CourseInfoPage(base.Base):


	def __init__(self, driver, cfg):
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver


	def click_charge(self):
		time.sleep(2)
		self.dr.find_element("id", "J_setPriceNav").click()
		time.sleep(4)
		self.dr.find_element(self.cfg.get('courseRedirect', 'chanrge_by'), \
			self.cfg.get('courseRedirect', 'chanrge')).click()

	def input_price(self, cprice):
		pinput = self.dr.find_element(self.cfg.get('courseRedirect', 'price_by'), \
			self.cfg.get('courseRedirect', 'price'))
		pinput.clear()
		pinput.send_keys(cprice)

	def input_description(self, cdescription ):
		time.sleep(3)
		self.dr.execute_script("var element=\
			window.document.getElementById('courseDesc-editor_ifr');\
			idocument=element.contentDocument;\
			element=idocument.getElementById('tinymce');\
			element.innerHTML =\'"+cdescription+"\';")
		time.sleep(0.1)

	def input_tag(self, course_tags):
		self.dr.find_element(self.cfg.get('courseRedirect', 'tags_by'), \
			self.cfg.get('courseRedirect', 'tags')).send_keys(course_tags)
	
	def click_teacher(self):
		time.sleep(1)
		self.dr.execute_script("$('.baseInfoNav li').eq(8).click()")
    	
	def click_choiceteacher(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('courseRedirect', 'teacherbtn_by'), \
			self.cfg.get('courseRedirect', 'teacherbtn')).click()
			
	def choice_firsteacher(self):
		time.sleep(1)
		self.dr.find_elements(self.cfg.get('courseRedirect', 'choiceteacher_by'), \
			self.cfg.get('courseRedirect', 'choiceteacher'))[0].click()
			
	def click_window_sure(self):
		self.dr.find_elements(self.cfg.get('courseRedirect', 'sure_by'), \
			self.cfg.get('courseRedirect', 'sure'))[0].click()	
				
	def click_save(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'done_btn_by'), \
			self.cfg.get('courseRedirect', 'done_btn')).click()

class CourseManageListPage(base.Base):

	def __init__(self, driver, cfg):

		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver

	def open(self):
		op = MyOfficePage(self.dr, self.cfg)
		op.open()
		op.click_teaching()
		op.click_course_manage()

	def click_manage(self):
		self.dr.find_elements("class name", "chapterSelect")[0].click()
		time.sleep(0.5)

	def click_get_link(self):
		time.sleep(3)
		try:
			self.dr.find_element_by_link_text(u"获取视频链接").click()
			time.sleep(1)
			link = self.dr.execute_script("return $('textarea:eq(1)').text()")
		except:
			return ""
		return link
	
	def click_edit(self):
		time.sleep(2)
		self.dr.find_elements(self.cfg.get('courseRedirect', 'editcourse_by'), \
			self.cfg.get('courseRedirect', 'editcourse'))[0].click()
			
	def click_window_ok(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'winok_by'), \
			self.cfg.get('courseRedirect', 'winok')).click()
