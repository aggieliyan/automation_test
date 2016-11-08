# -*- coding: UTF-8 -*-
'''
Created on May 31, 2012

@author: yilulu
'''
import time
import re
from selenium.common.exceptions import NoSuchElementException

from PO.myoffice_page import MyOfficePage
from PO.payment_page import PaymentPage
from PO.orgindex_page import OrgIndexPage, FootPage
from PO.announcement_page import AnnouncementListPage, AnnouncementInputPage
from PO.banner_page import BannerPage
from PO.course_page import CourseManageListPage

#个人人民币买课
def buy_course(cfg, driver, base_url, course_url):

    pay = PaymentPage(driver, cfg)
    pay.open(course_url)
    bm = pay.choose_registerNow()
    pay.save_screenshot()
    if bm == 0:
        pay.choose_balance_pay()
        pay.choose_use_rmb()
        pay.click_pay()
        pay.click_look_Coursedetail()
    else:
        pass
   
#个人充值卡买课
def buy_course_usecard(cfg, driver, base_url, course_url):

    pay = PaymentPage(driver, cfg)
    pay.open(course_url)
    cm = pay.choose_registerNow()
    pay.save_screenshot()
    if cm == 0:
        pay.choose_balance_pay()
        pay.click_pay()
    else:
        pass          
    
#个人修改头像
def change_headpic(cfg, base_url, driver, \
    headpic = "C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg"):
    
    driver.get("%smyOffice.do" %(base_url))
    time.sleep(1)
    driver.find_element_by_link_text(u"编辑头像").click()
    time.sleep(3)
    driver.find_element_by_id(cfg.get('office', 'headpic_file_id')).send_keys(headpic)
    driver.find_element_by_xpath(cfg.get('office', 'headpic_upload_xpath')).click()
    time.sleep(2)

#机构发公告  
def release_announcement(cfg,driver, base_url, org_name, title,  an_content=u'announcement'):
    
    index = OrgIndexPage(driver, cfg)
    index.open(org_name)
    index.save_screenshot()
    index.click_announcement()
    al = AnnouncementListPage(driver, cfg)
    al.save_screenshot()
    al.click_list()
    al.click_manage()
    al.click_add_announcement()
    ai = AnnouncementInputPage(driver, cfg)
    ai.click_dropdown()
    ai.choice_column()
    ai.input_title(title)
    ai.input_content(an_content)
    ai.save_screenshot()
    ai.click_save()


#获取视频外链发公告    
def release_href_announcement(cfg, driver, base_url, org_name, title = u'href_announcement'):
    
    cp = CourseManageListPage(driver, cfg)
    cp.open()
    cp.save_screenshot()
    cp.click_manage()
    an_content = cp.click_get_link()
    cp.save_screenshot()
    if not an_content:
        an_content = "content-test"
    release_announcement(cfg,driver, base_url, org_name, title, an_content)

#机构修改头像
def org_chang_headpic(cfg, driver, base_url, org_name, \
    head_pic = r"\\data.ablesky.com\workspace\Testing\Testing Files\Automation_test\headpic.jpg"):

    org_office =  MyOfficePage(driver, cfg)
    org_office.open()
    org_office.input_org_pic(head_pic)

#机构首页logo   
def change_homelogo(cfg, driver, base_url, org_name, \
    logo_pic = r"\\data.ablesky.com\workspace\Testing\Testing Files\Automation_test\headpic.jpg"):

    lop = BannerPage(driver, cfg)
    if not lop.open():
        return
    lop.save_screenshot()
    lop.change_logo(logo_pic)

#修改页脚
def modify_pagefoot(cfg, driver, base_url, org_name, \
    foot_name=u"footname", foot_url=u"http://www.ablesky.com"):
   
    fp = FootPage(driver, cfg)
    fp.open(org_name)
    fp.save_screenshot()
    fp.input_footname(foot_name)
    fp.input_link(foot_url)
    fp.click_save()



    
    