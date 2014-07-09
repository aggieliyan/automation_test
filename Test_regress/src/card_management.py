# -*- coding: UTF-8 -*-
'''
Created on Jun 1, 2012

@author: yilulu
'''
import time

#使用充值卡和充课卡
def use_prepaid_card(cfg, driver, base_url, card_num, card_psw):
        
    driver.get(base_url+"useCard.do?action=toStudyCard")
    time.sleep(1)
    driver.find_element_by_id(cfg.get('use_card','card_num_id')).send_keys(card_num)
    driver.find_element_by_id(cfg.get('use_card','card_psw_id')).send_keys(card_psw)
    driver.find_element_by_css_selector(cfg.get('use_card','card_ok_css')).click()
    time.sleep(2)
    driver.find_element_by_css_selector(cfg.get('use_card','prepaid_ok_css')).click()
    time.sleep(2)
    
#使用补课卡
def use_course_card(cfg,driver, base_url, card_num, card_psw):
    
    driver.get(base_url+"useCard.do?action=toStudyCard")
    time.sleep(1)
    driver.find_element_by_id(cfg.get('use_card','card_num_id')).send_keys(card_num)
    driver.find_element_by_id(cfg.get('use_card','card_psw_id')).send_keys(card_psw)
    driver.find_element_by_css_selector(cfg.get('use_card','card_ok_css')).click()
    time.sleep(2)
    driver.find_element_by_name(cfg.get('use_card','course_check_1_name')).click()
    driver.find_element_by_xpath(cfg.get('use_card','course_check_2_xpath')).click()
    time.sleep(2)
    driver.find_element_by_css_selector(cfg.get('use_card','add_ok_css')).click()
    time.sleep(2)
    driver.find_element_by_css_selector(cfg.get('use_card','course_ok_css')).click()
    time.sleep(2)
  
#添加卡组-充值卡  
def add_prepaid_cardgroup(cfg, driver, base_url, org_name, group_name = u'prepaidcard100', group_price = 100):

    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"管理卡组").click()
    time.sleep(2)
    driver.find_element_by_link_text(u"添加卡组").click()
    time.sleep(2)
    driver.find_element_by_id(cfg.get('org_manage','grouptitle_id')).send_keys(group_name)
    driver.find_element_by_id(cfg.get('org_manage','prepaid_price_id')).send_keys(group_price)
    driver.execute_script("$(\".x-btn-text\").eq(2).click()")
    time.sleep(2)

#添加卡组-充课卡
def add_course_cardgroup(cfg,driver, base_url, org_name , group_name = u'coursecard'):
    
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"管理卡组").click()
    time.sleep(2)
    driver.find_element_by_link_text(u"添加卡组").click()
    time.sleep(2)
    driver.find_element_by_xpath(cfg.get('org_manage','course_card_xpath')).click()#选择充课卡
    driver.find_element_by_id(cfg.get('org_manage','grouptitle_id')).send_keys(group_name)
    time.sleep(3)
    driver.find_element_by_xpath(cfg.get('org_manage','course_cate_xpath')).click()#选择整个类目，类目下的课被选中
    time.sleep(1)
    #driver.find_element_by_xpath(cfg.get('org_manage','course_ok_xpath')).click()
    driver.execute_script("$(\".x-btn-text\").eq(0).click()")
    time.sleep(3)
    driver.execute_script("$(\".x-btn-text\").eq(2).click()")

#添加卡组-补课卡 
def add_cate_cardgroup(cfg,driver, base_url, org_name,group_name = u'catecard-200', group_price = 200):
    
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"管理卡组").click()
    time.sleep(2)
    driver.find_element_by_link_text(u"添加卡组").click()
    time.sleep(2)
    driver.find_element_by_id(cfg.get('org_manage','grouptitle_id')).send_keys(group_name)
    driver.find_element_by_xpath(cfg.get('org_manage','cate_card_xpath')).click()
    time.sleep(3)
    driver.find_element_by_name(cfg.get('org_manage','cate_name')).click()
    driver.find_element_by_id(cfg.get('org_manage','cate_price_id')).send_keys(group_price)
    driver.execute_script("$(\".x-btn-text\").eq(2).click()")
    time.sleep(2)
      

#添加卡
def add_card(cfg, driver, base_url, org_name, cgroup_num = 1,card_prifix='auto',card_num = 50):
     
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"管理卡组").click()
    time.sleep(2)
    
    if cgroup_num == 1:
        driver.find_element_by_link_text(u"添加卡").click()
    else:  
        driver.find_element_by_xpath("//div["+str(cgroup_num)+"]/table/tbody/tr/td[6]/div/div/a").click()
    
    time.sleep(2)
    driver.find_element_by_id(cfg.get('org_manage','card_prefix_id')).send_keys(card_prifix)
    time.sleep(3)
    driver.find_element_by_id(cfg.get('org_manage','card_count_id')).send_keys(card_num)
    time.sleep(3)
    driver.find_element_by_css_selector(cfg.get('org_manage','add_card_ok_css')).click()
    time.sleep(2)


