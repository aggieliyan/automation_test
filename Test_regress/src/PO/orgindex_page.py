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
		time.sleep(1)
		try:
			self.dr.find_element("id", "J_continueGuid").click()
			time.sleep(1)
			print "okkkk"
		except:
			pass

	def get_orgid(self, org_name):
		self.open(org_name)
		orgid = 0
		ahref = self.dr.execute_script("return $('.text').eq(1).attr('href')")
		orgid = re.search(r'\d{1,10}.\d', ahref).group(0)
		print orgid
		return orgid

	#网校公告
	def click_announcement(self):
		try:
			self.dr.find_element_by_link_text(u"网校公告").click()
		except NoSuchElementException, e:
			print u'网校公告导航不存在'
		# except WebDriverException, e:
		# 	self.dr.find_element("id", "J_continueGuid").click()
		# 	time.sleep(1)
		# 	self.dr.find_element_by_link_text(u"网校公告").click()


class FootPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self, org_name):
		op = OrgIndexPage(self.dr, self.cfg)
		orgid = op.get_orgid(org_name)
		self.dr.get("%sorgHomePageRedirect.do?action=toEditPageFoot\
			&organizationId=%s"%(self.base_url, str(orgid)))

	def input_footname(self, footname):
		ainput = self.dr.find_element(self.cfg.get('org_index', 'pf_name_by'), \
			self.cfg.get('org_index', 'pf_name'))
		ainput.clear()
		ainput.send_keys(footname)

	def input_link(self, link):
		ainput = self.dr.find_element(self.cfg.get('org_index', 'pf_link_by'), \
			self.cfg.get('org_index', 'pf_link'))
		ainput.clear()
		ainput.send_keys(link)

	def click_save(self):
		self.dr.find_element(self.cfg.get('org_index', 'pf_save_by'), \
			self.cfg.get('org_index', 'pf_save')).click()
		self.save_screenshot()
		time.sleep(1)
