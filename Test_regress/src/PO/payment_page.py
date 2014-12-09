# -*- coding: UTF-8 -*-
'''
Created on Dec. 09, 2014

@author: yilulu
'''
import re
import time

import base

class PaymentPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self, course_url):
		course_id = re.search(r'\d{1,10}', course_url).group(0)
		host = self.base_url.replace("http://","")
		self.dr.get("%spaymentRedirect.do?action=paymentDomainRedirect&\
			host=%s&grouponid=&type=course&id=%s"\
			%(self.base_url, host, str(course_id)))

	def choose_use_rmb(self):
		self.dr.find_element(self.cfg.get('org_index','use_rmb_by'), \
			self.cfg.get('org_index','use_rmb')).click()

	def click_pay(self):
		self.dr.find_element(self.cfg.get('org_index', 'pay_ok_by'), \
			self.cfg.get('org_index', 'pay_ok')).click()
		time.sleep(2)