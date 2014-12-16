# -*- coding: UTF-8 -*-
'''
Created on Dec. 15, 2014

@author: yilulu
'''
import time

import base

class AnnouncementListPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def click_edit_announcement(self):
		pass

	def click_add_announcement(self):
		self.dr.find_element("link text", u"新增公告").click()

class AnnouncementInputPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def input_title(self, title):
		self.dr.find_element(self.cfg.get('org_index', 'act_title_by'), \
			self.cfg.get('org_index', 'act_title')).send_keys(title)

	def input_content(self, an_content):
		an_content = an_content.replace("\"","\\\"").replace("\'","\\\'")
		time.sleep(1)
		self.dr.execute_script("var element=window.document.getElementById('editNotice_ifr');\
			idocument=element.contentDocument;\
			element=idocument.getElementById('tinymce');\
			element.innerHTML='" + an_content + "'")
		time.sleep(1)

	def click_save(self):
		self.dr.find_element(self.cfg.get('org_index', 'act_ok_by'), \
			self.cfg.get('org_index', 'act_ok')).click()
		time.sleep(1)