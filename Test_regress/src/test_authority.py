# -*- coding: UTF-8 -*-
from selenium import webdriver

def course(driver, base_url):
	driver.get("%smyOffice.do" %(base_url))
	course_func = [u'课程类目', u'课程管理', u'课程存储空间', u'视频外链管理', u'播放高级设置']
	try:
		driver.find_element_by_link_text(u"教学教务").click()
		for item in course_func:
			try:
				driver.find_element_by_link_text(item).click()
			except Exception:
				error_info = u"没有%s权限"%item
				print error_info
	except Exception:
		print u"没有教学教务相关权限"
		return


def admin_athority_check():
	base_url = "http://www.gamma.ablesky.com"
	chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    admin_athority_check()
