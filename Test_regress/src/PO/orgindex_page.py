
# -*- coding: UTF-8 -*-
'''
Created on Dec. 09, 2014

@author: yilulu
'''
import re
import time

from selenium.common.exceptions import NoSuchElementException, WebDriverException

import base

class OrgIndexPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self, org_name):
		self.dr.get("%s%s"%(self.base_url, org_name))

	#网校公告
	def click_announcement(self):
		try:
			self.dr.find_element_by_link_text(u"网校公告").click()
		# except NoSuchElementException, e:
		# 	print u'网校公告导航不存在'
		except WebDriverException, e:
			self.dr.find_element("id", "J_continueGuid").click()
			time.sleep(1)
			self.dr.find_element_by_link_text(u"网校公告").click()