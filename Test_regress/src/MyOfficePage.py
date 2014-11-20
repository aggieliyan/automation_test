# -*- coding: UTF-8 -*-

import time
import ConfigParser

class MyOfficePage():
	#
	def __init__(self, driver):
		
		tdata = ConfigParser.RawConfigParser()
		tdata.read('testdata.ini')
		self.cfg = ConfigParser.RawConfigParser()
		self.cfg.read('config.ini')
		self.base_url = tdata.get('env_para', 'base_url')
		self.dr = driver
	
	def open(self):
		self.dr.get("%smyOffice.do" %(self.base_url))
		self.dr.maximize_window()

	def click_system_settings(self):
		self.dr.find_element_by_link_text(u"系统设置")


	def input_org_pic(self, picfile):
		self.dr.execute_script("$('.oai-org-logo-upload').attr('style','display:block;');\
			$('#J_oaiUploadTrigger').attr('style','display:block;'); \
			$('.fileinput-button input').eq(0).attr('style',\
				'height:300px;opacity:1;display:block;position:static;\
				transform:translate(-2px,-50px) scale(1)')")
		time.sleep(1)
		self.dr.find_element(self.cfg.get('org_index','headpic_by'), \
			self.cfg.get('org_index','headpic')).send_keys(picfile)



