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

	def click_list(self):
	    time.sleep(3)
	    self.dr.find_element(self.cfg.get('org_index', 'noticelist_by'), \
			self.cfg.get('org_index', 'noticelist')).click()
	    time.sleep(1)
	    try:	
	        self.dr.find_element(self.cfg.get('org_index', 'sure_by'), \
			    self.cfg.get('org_index', 'sure')).click()
	    except:
	    	None
    
	def click_manage(self):
		time.sleep(1)
		self.dr.find_elements(self.cfg.get('org_index', 'manage_by'), \
			self.cfg.get('org_index', 'manage'))[0].click()
			
	def click_add_announcement(self):
		bh = self.dr.window_handles
		self.dr.find_elements(self.cfg.get('org_index', 'addannoun_by'), \
			self.cfg.get('org_index', 'addannoun'))[0].click()
		self.switch_window(bh)
		
class AnnouncementInputPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		
	def click_dropdown(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_index', 'dropdown_by'), \
			self.cfg.get('org_index', 'dropdown')).click()
			
	def choice_column(self):
		self.dr.find_element(self.cfg.get('org_index', 'column_by'), \
			self.cfg.get('org_index', 'column')).click()

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