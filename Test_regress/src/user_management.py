# -*- coding: UTF-8 -*-
'''
Created on May 31, 2012

@author: yilulu
'''
import time
from selenium.common.exceptions import NoSuchElementException

#个人人民币买课
def buy_course(cfg, driver, course_url):
    
    driver.get(course_url)
    driver.find_element_by_id(cfg.get('org_index','buy_course_id')).click()
    time.sleep(1)
    h = driver.window_handles
    #ch = driver.current_window_handle
    driver.switch_to_window(h[-1])

    driver.find_element_by_id(cfg.get('org_index','use_rmb_id')).click()
    driver.find_element(cfg.get('org_index','pay_ok_by'), cfg.get('org_index','pay_ok')).click()
    time.sleep(5)

#个人充值卡买课
def buy_course_usecard(cfg, driver, course_url):
    
    driver.get(course_url)
    driver.find_element_by_id(cfg.get('org_index','buy_course_id')).click()
    time.sleep(1)
    h = driver.window_handles
    #ch = driver.current_window_handle
    driver.switch_to_window(h[-1])
            
    driver.find_element(cfg.get('org_index','pay_ok_by'), cfg.get('org_index','pay_ok')).click()
    time.sleep(5)

#个人发照片 数量最大10
def add_photo(cfg, driver, base_url, username,pic="C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg",pic_num = 1):
    
    driver.get(base_url + "community.do?action=toProfileSpace&username="+username)
    try:
        driver.find_element_by_link_text(u"编辑").click()
        time.sleep(2)
        driver.find_element_by_id(cfg.get('office','add_Galleries_id')).click()
    except NoSuchElementException:
        driver.execute_script("$('#albumMain .center').click()")
        time.sleep(1)
        driver.find_element_by_id("albumName").send_keys("sss")
        driver.find_element_by_id("albumDescription").send_keys("dddd")
        driver.find_element_by_xpath("//button").click()
        
    
    time.sleep(3)
    
    for i in range(1,pic_num + 1):       
        if i > 5 and i < 11:
            driver.find_element_by_id(cfg.get('office','add_photo_id')).click()
        driver.find_element_by_id("gallery"+str(i)).send_keys(pic)
        
    driver.find_element_by_xpath(cfg.get('office','add_submit_xpath')).click()
    
    if pic_num > 5:
        time.sleep(15)
    else:
        time.sleep(6)
    
    driver.find_element_by_xpath(cfg.get('office','save_photo_xpath')).click()
    time.sleep(2)

def auto_add_photo(cfg,driver, base_url, username,pic="C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg",pic_num = 50):
    
    count = 0
    last_count = 0
    count = pic_num/10
    last_count = pic_num%10
    if last_count != 0:
        count = count + 1
    
    pic_num = 10
    for i in range(count):  
        if i == count - 1:
            pic_num = last_count
        add_photo(cfg,driver, base_url, username,pic,pic_num)
           
    
#个人修改头像
def change_headpic(cfg,base_url,driver,headpic = "C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg" ):
    
    driver.get(base_url+"myOffice.do")
    time.sleep(1)
    driver.find_element_by_link_text(u"编辑头像").click()
    time.sleep(3)
    driver.find_element_by_id(cfg.get('office','headpic_file_id')).send_keys(headpic)
    driver.find_element_by_xpath(cfg.get('office','headpic_upload_xpath')).click()
    time.sleep(2)

#机构发公告  
def release_announcement(cfg,driver, base_url, org_name, an_title = u"自动化测试公告", an_content=u'这是公告内容公告内容'):
    
    driver.get(base_url+org_name)
    time.sleep(2)
    driver.find_element_by_link_text(u"发布机构公告").click()
    time.sleep(2)
    driver.find_element_by_xpath(cfg.get('org_index','ann_title_xpath')).send_keys(an_title)
    driver.find_element_by_css_selector("span.mceIcon.mce_expandEdit").click()
    time.sleep(2)
    driver.find_element_by_css_selector("span.mceIcon.mce_code").click()
    an_content = an_content.replace("\"","\\\"").replace("\'","\\\'")
    #print an_content
    driver.execute_script("var element=window.document.getElementById('mce_9_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('htmlSource');element.value =\'"+an_content+"\';idocument.getElementById('insert').click();")
    time.sleep(5)

    driver.find_element_by_xpath(cfg.get('org_index','ann_ok_xpath')).click()
    time.sleep(2)
    return an_title

#机构修改头像
def org_chang_headpic(cfg,driver, base_url,org_name,head_pic = r"W:\Testing\Testing Files\Automation_test\headpic.jpg" ):
 
    driver.get(base_url + "myOffice.do")
    time.sleep(5)
    #driver.find_element_by_name("photo").click()
    #driver.execute_script("$(\"#J_oaiUploadTrigger input\").attr('style','display:opacity:1;display:block;')")
    driver.find_element_by_name("photo").send_keys(head_pic)
    time.sleep(10)
    #driver.find_element_by_xpath(cfg.get('org_index','org_manage_xpath')).click()
    #time.sleep(2)
    #driver.find_element_by_css_selector(cfg.get('org_manage','change_headpic_css')).click()
    #time.sleep(1)
    #driver.find_element_by_id(cfg.get('org_manage','headpic_upload_id')).send_keys(head_pic)
    #driver.find_element_by_xpath(cfg.get('org_manage','headpic_ok_xpath')).click()
    #time.sleep(2)
    
def change_banner(cfg,driver, base_url, org_name):
  
    driver.get(base_url + org_name)
    driver.find_element_by_css_selector(cfg.get('org_index','change_banner_css')).click()
    driver.find_element_by_xpath(cfg.get('org_index','as_banner_xpath')).click()
    driver.find_element_by_xpath(cfg.get('org_index','select_banner_xpath')).click()
    driver.find_element_by_xpath(cfg.get('org_index','banner_ok_xpath')).click()  
    time.sleep(1)

def modify_pagefoot(cfg,driver, independent_url, foot_info = u"新公司信息",foot_icp = u"1100110"):
   
    driver.get(independent_url)
    driver.find_element_by_link_text(u"编辑页脚信息").click()
    driver.find_element_by_xpath(cfg.get('org_index','foot_info_xpath')).clear()
    driver.find_element_by_xpath(cfg.get('org_index','foot_info_xpath')).send_keys(foot_info)
    driver.find_element_by_xpath(cfg.get('org_index','foot_icp_xpath')).clear()
    driver.find_element_by_xpath(cfg.get('org_index','foot_icp_xpath')).send_keys(foot_icp)
    driver.find_element_by_xpath(cfg.get('org_index','foot_ok_xpath')).click() 
    
    