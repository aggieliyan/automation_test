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
from PO.orgindex_page import OrgIndexPage
from PO.announcement_page import AnnouncementListPage, AnnouncementInputPage

#个人人民币买课
def buy_course(cfg, driver, base_url, course_url):

    pay = PaymentPage(driver, cfg)
    pay.open(course_url)
    pay.save_screenshot()
    pay.choose_use_rmb()
    pay.click_pay()
    pay.save_screenshot()
    
#个人充值卡买课
def buy_course_usecard(cfg, driver, base_url, course_url):

    pay = PaymentPage(driver, cfg)
    pay.open(course_url)
    pay.save_screenshot()
    pay.click_pay()
    pay.save_screenshot()
           
    
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
def release_announcement(cfg,driver, base_url, org_name, title, an_content=u'announcement'):
    
    index = OrgIndexPage(driver, cfg)
    index.open(org_name)
    index.click_announcement()
    al = AnnouncementListPage(driver, cfg)
    al.click_add_announcement()
    ai = AnnouncementInputPage(driver, cfg)
    ai.input_title(title)
    ai.input_content(an_content)
    ai.click_save()



    # driver.get("%s%s"%(base_url, org_name))
    # driver.implicitly_wait(10)
    # driver.find_element_by_link_text(u"网校公告").click()
    # driver.implicitly_wait(10)
    # driver.find_element(cfg.get('org_index', 'release_announcementx_by'), \
    #     cfg.get('org_index', 'release_announcementx')).click()
    # driver.find_element(cfg.get('org_index', 'release_announcementc_by'), \
    #     cfg.get('org_index', 'release_announcementc')).send_keys(title)
    # an_content = an_content.replace("\"","\\\"").replace("\'","\\\'")
    # driver.implicitly_wait(10)
    # driver.execute_script("var element=window.document.getElementById('editNotice_ifr');\
    # idocument=element.contentDocument;\
    # element=idocument.getElementById('tinymce');\
    # element.innerHTML='" + an_content + "'")
    # time.sleep(2)
    # driver.find_element(cfg.get('org_index', 'act_ok_by'), \
    #     cfg.get('org_index', 'act_ok')).click()
    # time.sleep(1)

#获取视频外链发公告    
def release_href_announcement(cfg, driver, base_url, org_name, title = u'href_announcement'):
    
    driver.get("%smyOffice.do" %(base_url))
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"教学教务").click()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"课程管理").click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"获取视频链接").click()
    time.sleep(2)
    an_content = driver.execute_script("return $('textarea:eq(1)').text()")
    time.sleep(1)  
    release_announcement(cfg,driver, base_url, org_name, title, an_content)
    time.sleep(2)

#机构修改头像
def org_chang_headpic(cfg, driver, base_url, org_name, \
    head_pic = r"\\data.ablesky.com\workspace\Testing\Testing Files\Automation_test\headpic.jpg"):

    org_office =  MyOfficePage(driver)
    org_office.open()
    org_office.input_org_pic(head_pic)

#机构首页logo   
def change_homelogo(cfg, driver, base_url, org_name, \
    logo_pic = r"\\data.ablesky.com\workspace\Testing\Testing Files\Automation_test\headpic.jpg"):
  
    driver.get("%s%s"%(base_url, org_name))
    time.sleep(2)
    driver.execute_script("$('.edit-logo').attr('style','display:block;');\
        $('.edit-logo-btn ').attr('style','display:block;');\
        $('.fileinput-button input').eq(0).attr('style','height:300px;opacity:1;\
            display:block;position:static;transform:translate(0px, 0px) scale(1)')")
    time.sleep(1)
    driver.find_element(cfg.get('org_index', 'home_logoname_by'), \
        cfg.get('org_index', 'home_logoname')).send_keys(logo_pic)
    time.sleep(1)

#修改页脚
def modify_pagefoot(cfg, driver, base_url, org_name, \
    foot_name=u"footname", foot_url=u"http://www.ablesky.com"):
   
    driver.get("%s%s"%(base_url, org_name))
    driver.implicitly_wait(10)
    foot_href = driver.execute_script("return $('#J_dressNav_warp a').eq(6).attr('href')")
    time.sleep(1)
    driver.get("%s%s"%(base_url, foot_href))
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_index', 'pf_modx2_by'), \
        cfg.get('org_index', 'pf_modx2')).clear()
    driver.find_element(cfg.get('org_index', 'pf_modx3_by'), \
        cfg.get('org_index', 'pf_modx3')).send_keys(foot_name)
    driver.find_element(cfg.get('org_index', 'pf_modx4_by'), \
        cfg.get('org_index', 'pf_modx4')).clear()
    driver.find_element(cfg.get('org_index', 'pf_modx4_by'), \
        cfg.get('org_index', 'pf_modx4')).send_keys(foot_url)
    driver.find_element(cfg.get('org_index', 'pf_modc5_by'), \
        cfg.get('org_index', 'pf_modc5')).click()
    time.sleep(1)


    
    