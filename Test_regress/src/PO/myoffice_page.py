# -*- coding: UTF-8 -*-
'''
Created on Nov. 17, 2014

@author: yilulu
'''
import time
import ConfigParser

from selenium.common.exceptions import NoSuchElementException

import base

class MyOfficePage(base.Base):
	#
	def __init__(self, driver, cfg):
		
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver
	
	#打开机构后台页面
	def open(self):
		self.dr.get("%smyOffice.do" %(self.base_url))
		self.dr.maximize_window()

	#点击系统设置导航
	def click_system_settings(self):
		self.dr.find_element_by_link_text(u"系统设置").click()

	def click_logo_settings(self):
		try:
			self.dr.find_element_by_link_text(u"logo/联系方式设置").click()
		except NoSuchElementException, e:
			print u"该导航不存在"
			return 0
		return 1

	#点击网校管理员
	def click_org_admin(self):
		self.dr.find_element_by_link_text(u"网校管理员").click()

	#点击教学教务
	def click_teaching(self):
		self.dr.find_element_by_link_text(u"教学教务").click()

	def click_course_manage(self):
		self.dr.find_element_by_link_text(u"课程管理").click()	

	def class_manage(self):
		self.dr.find_element_by_link_text(u"报班管理").click()

	#点击管理我申请的代理
	def click_myapplyagency(self):
		self.dr.find_element_by_link_text(u"管理我申请的代理").click()


	#为机构头像换图片
	def input_org_pic(self, picfile):
		self.dr.execute_script("$('.oai-org-logo-upload').attr('style','display:block;');\
			$('#J_oaiUploadTrigger').attr('style','display:block;'); \
			$('.fileinput-button input').eq(0).attr('style',\
				'height:300px;opacity:1;display:block;position:static;\
				transform:translate(-2px,-50px) scale(1)')")
		time.sleep(1)
		self.dr.find_element(self.cfg.get('org_index','headpic_by'), \
			self.cfg.get('org_index','headpic')).send_keys(picfile)

	#点击学员/员工导航
	def click_student(self):
		self.dr.find_element_by_link_text(u"学员/员工").click()

	#点击学员管理
	def click_student_management(self):
		self.dr.find_element_by_link_text(u"学员管理").click()


	# #点击在线购买授权
	# def click_buy_opennum(self):
	# 	self.dr.find_element_by_link_text(u"授权购买记录").click()
	# 	self.dr.find_element_by_link_text(u"购买授权").click()
	# 	h = self.dr.window_handles
	# 	self.dr.switch_to_window(h[-1])
	# 	time.sleep(2)
		
	#点击教学教务导航
	def click_org_teach(self):
		time.sleep(2)
		self.dr.find_element_by_link_text(u"教学教务").click()

	#点击课程类目
	def click_org_cate(self):
		self.dr.find_element_by_link_text(u"课程类目").click()
		
	#点击首页导航
	def click_org_firstpage(self):
		self.dr.find_element_by_link_text(u"后台首页").click()

	#点击管理/卡组
	def click_org_mancardgroup(self):
		self.dr.find_element_by_link_text(u"管理卡组").click()

	#去在线购买授权页面
	def click_num_record(self):
		time.sleep(2)
		self.dr.find_element_by_link_text(u"授权购买记录").click()
		h = self.dr.window_handles
		self.dr.switch_to_window(h[-1])
		self.dr.find_element_by_link_text(u"购买授权").click()	



