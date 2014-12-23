# -*- coding: UTF-8 -*-
'''
Created on Nov. 17, 2014

@author: yilulu
'''
import time
import ConfigParser

import base
from myoffice_page import MyOfficePage

class BannerPage(base.Base):


	def __init__(self, driver, cfg):
		
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.dr = driver

	def open(self):
		op = MyOfficePage(self.dr, self.cfg)
		op.open()
		op.click_system_settings()
		op.click_logo_settings()

	def change_logo(self, logo_pic):
		# self.dr.execute_script("$('#J_uploadLogoIndex').attr('style','display:block;');\
		# 	$('#J_uploadLogo').attr('style','display:block;');\
		# 	$('#J_uploadLogo input').eq(0).attr('style','height:300px;opacity:1;\
		# 		display:block;position:static;transform:translate(0px, 0px) scale(1)')")
		ainput = self.dr.find_element(self.cfg.get('org_index', 'home_logoname_by'), \
			self.cfg.get('org_index', 'home_logoname'))
		# print ainput
		# for a in ainput:
		# print ainput.is_displayed()
		self.dr.execute_script("\
			$('#J_uploadLogoIndex').attr('style','display:block;');\
			$('#J_uploadLogo').attr('style','display:block;');\
			$('.reload-text').eq(0);\
			$('#J_uploadLogo input').attr('style','height:300px;opacity:1;\
				display:block;transform:translate(0px, 0px) scale(1)')")
		time.sleep(1)
		# for a in ainput:
		# print ainput.is_displayed()

		self.dr.find_element(self.cfg.get('org_index', 'home_logoname_by'), \
			self.cfg.get('org_index', 'home_logoname')).send_keys(logo_pic)
		time.sleep(1)