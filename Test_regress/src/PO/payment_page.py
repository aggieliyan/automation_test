# -*- coding: UTF-8 -*-
'''
Created on Dec. 09, 2014

@author: yilulu
'''
import re
import time
from selenium.common.exceptions import NoSuchElementException

import base

class PaymentPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self, course_url, ptype="course"):
		"""
		ptype 是购买东西的类型，course 为课程
		                       exampaper 为试卷

		"""
		try:
			self.dr.get(course_url)
			time.sleep(3)
		except:
			self.dr.refresh()
			time.sleep(3)
#		course_id = re.search(r'\d{1,10}', course_url).group(0)
#		host = self.base_url.replace("http://","")
#		self.dr.get("%spaymentRedirect.do?action=paymentDomainRedirect&\
#			host=%s&grouponid=&type=%s&id=%s"\
#			%(self.base_url, host, ptype, str(course_id)))

	#刷新页面
#	def self_dr_refresh(self):
#		self.dr.refresh()
#		time.sleep(3)

	#点击立即报名
	def choose_registerNow(self):
		time.sleep(2)
		bm = 0
		try:
			bh = self.dr.window_handles
			self.dr.find_element_by_link_text(u"立即报名").click()
			self.switch_window(bh)
		except NoSuchElementException, e:
			print u"已购买该课程或课程为免费课程"
			bm = 1
		return bm
	
	#点击立即购买
	def choose_buyNow(self):
		time.sleep(2)
		exm = 0
		try:
			bh = self.dr.window_handles
			self.dr.find_element_by_link_text(u"立即购买").click()
			self.switch_window(bh)
		except NoSuchElementException, e:
			print u"已购买该试卷或试卷为免费试卷"
			exm = 1
		return exm
	
	#付款确认信息页面
	def confirm_pay(self):
		time.sleep(2)
		self.dr.find_element_by_class_name("button").click()

    #选择账户余额支付
	def choose_balance_pay(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_index','balance_by'), \
			self.cfg.get('org_index','balance')).click()
			
	def choose_use_rmb(self):
		time.sleep(2)
        try:
            self.dr.find_element(self.cfg.get('org_index','use_rmb_by'), \
                self.cfg.get('org_index','use_rmb')).click()
        except:
            pass

	def click_pay(self):
		time.sleep(3)
		self.dr.find_element(self.cfg.get('org_index', 'pay_ok_by'), \
			self.cfg.get('org_index', 'pay_ok')).click()
		
	def click_look_Coursedetail(self):
		time.sleep(5)
		self.dr.find_element_by_link_text(u"查看课程详情").click()
		time.sleep(3)
		
	def click_look_Examdetail(self):
		time.sleep(5)
		self.dr.find_element_by_link_text(u"查看试卷详情").click()
		time.sleep(3)
		