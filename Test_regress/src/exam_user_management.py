# -*- coding: UTF-8 -*-
'''
Created on Jul 24, 2014

@author: yilulu
'''
import user_management
import time

def buy_paper(cfg, driver, base_url, paper_url):
	#paper_url = "http://www.gamma.ablesky.com/examRedirect.do?action=viewExamPaperInfo&examPaperId=6129"
	driver.get(paper_url)
	time.sleep(1)
	driver.find_element("id", "examBtn").click()
	h = driver.window_handles
	driver.switch_to_window(h[-1])
	driver.find_element_by_css_selector(cfg.get('org_index','pay_ok_css')).click()
	time.sleep(5)