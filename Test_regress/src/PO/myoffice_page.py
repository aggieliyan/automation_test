# -*- coding: UTF-8 -*-

import time
import ConfigParser

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

	#点击网校管理员
	def click_org_admin(self):
		self.dr.find_element_by_link_text(u"网校管理员").click()

	#点击教学教务
	def click_teaching(self):
		self.dr.find_element_by_link_text(u"教学教务").click()

	def class_manage(self):
		self.dr.find_element_by_link_text(u"报班管理").click()


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



