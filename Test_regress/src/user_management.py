# -*- coding: UTF-8 -*-
'''
Created on May 31, 2012

@author: yilulu
'''
import time
from selenium.common.exceptions import NoSuchElementException

#个人人民币买课
def buy_course(cfg, driver, base_url, course_url):
    
    driver.get(course_url)
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_index','buy_course_by'), \
        cfg.get('org_index','buy_course')).click()
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    driver.find_element(cfg.get('org_index','use_rmb_by'), \
        cfg.get('org_index','use_rmb')).click()
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_index', 'pay_ok_by'), \
        cfg.get('org_index', 'pay_ok')).click()
    time.sleep(1)
  
    
#个人充值卡买课
def buy_course_usecard(cfg, driver, base_url, course_url):
    
    driver.get(course_url)
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_index','buy_course_by'), \
        cfg.get('org_index','buy_course')).click()
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_index', 'pay_ok_by'), \
        cfg.get('org_index', 'pay_ok')).click()
    time.sleep(1)
    
#个人发照片 数量最大10
def add_photo(cfg, driver, base_url, username, \
    pic="C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg", pic_num = 1):
    
    driver.get(base_url + "community.do?action=toProfileSpace&username=" + username)
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
            driver.find_element_by_id(cfg.get('office', 'add_photo_id')).click()
        driver.find_element_by_id("gallery"+str(i)).send_keys(pic)
        
    driver.find_element_by_xpath(cfg.get('office', 'add_submit_xpath')).click()
    
    if pic_num > 5:
        time.sleep(15)
    else:
        time.sleep(6)
    
    driver.find_element_by_xpath(cfg.get('office', 'save_photo_xpath')).click()
    time.sleep(2)

def auto_add_photo(cfg,driver, base_url, username, \
    pic="C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg",pic_num = 50):
    
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
        add_photo(cfg,driver, base_url, username, pic, pic_num)
           
    
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
    
    driver.get("%s%s"%(base_url, org_name))
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"网校公告").click()
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_index', 'release_announcementx_by'), \
        cfg.get('org_index', 'release_announcementx')).click()
    driver.find_element(cfg.get('org_index', 'release_announcementc_by'), \
        cfg.get('org_index', 'release_announcementc')).send_keys(title)
    an_content = an_content.replace("\"","\\\"").replace("\'","\\\'")
    driver.implicitly_wait(10)
    driver.execute_script("var element=window.document.getElementById('editNotice_ifr');\
    idocument=element.contentDocument;\
    element=idocument.getElementById('tinymce');\
    element.innerHTML='" + an_content + "'")
    time.sleep(2)
    driver.find_element(cfg.get('org_index', 'release_announcementx2_by'), \
        cfg.get('org_index', 'release_announcementx2')).click()
    time.sleep(1)

#获取视频外链发公告    
def release_href_announcement(cfg, driver, base_url, org_name, title = u'href_announcement'):
    
    driver.get("%s%s"%(base_url, org_name))
    driver.implicitly_wait(10)
    driver.find_element_by_link_text(u"课程中心")
    time.sleep(2)
    chref = driver.execute_script("return $(\".coursecenter-details-pic a\").eq(0).attr('href')")
    time.sleep(1)
    driver.get("%s%s"%(base_url, chref)) 
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_index', 'release_hrefi_by'), \
        cfg.get('org_index', 'release_hrefi')).click() 
    time.sleep(2)
    an_content = driver.execute_script("return $('textarea:eq(2)').text()")
    time.sleep(1)  
    release_announcement(cfg,driver, base_url, org_name, title, an_content)
    time.sleep(2)

#机构修改头像
def org_chang_headpic(cfg, driver, base_url, org_name, \
    head_pic = r"W:\Testing\Testing Files\Automation_test\headpic.jpg"):
    
    driver.get("%smyOffice.do" %(base_url))
    time.sleep(2)
    driver.execute_script("$('.oai-org-logo-upload').attr('style','display:block;');\
        $('#J_oaiUploadTrigger').attr('style','display:block;'); \
        $('.fileinput-button input').eq(0).attr('style',\
            'height:300px;opacity:1;display:block;position:static;\
            transform:translate(-2px,-50px) scale(1)')")
    time.sleep(1)
    driver.find_element(cfg.get('org_index','head_picname_by'), \
        cfg.get('org_index','head_picname')).send_keys(head_pic)
    time.sleep(1)

#机构首页logo   
def change_homelogo(cfg, driver, base_url, org_name, \
    logo_pic = r"W:\Testing\Testing Files\Automation_test\headpic.jpg"):
  
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
    driver.find_element_by_link_text(u"编辑页脚").click()
    h = driver.window_handles
    driver.switch_to_window(h[-1])
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


    
    