# -*- coding: UTF-8 -*-
'''
Created on May 31, 2012

@author: yilulu
'''
import time
from selenium.common.exceptions import NoSuchElementException

#个人人民币买课
def buy_course(cfg, driver, base_url, org_name):
    
    driver.get(base_url+org_name)
    time.sleep(8)
    driver.find_element_by_link_text(u"课程中心").click()
    time.sleep(10)
    driver.find_element_by_xpath('//html/body/div[2]/div[3]/div/div[2]/div[1]/div/p/a').click()
    time.sleep(8)
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    time.sleep(8)
    driver.find_element_by_link_text(u"立即购买").click()
    time.sleep(10)
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    driver.find_element(cfg.get('org_index','buy_coursei_by'),cfg.get('org_index','buy_coursei')).click()
    time.sleep(12)
    driver.find_element(cfg.get('org_index','buy_coursec2_by'),cfg.get('org_index','buy_coursec2')).click()
    time.sleep(8)
    driver.find_element(cfg.get('org_index','buy_coursec2_by'),cfg.get('org_index','buy_coursec2')).click()
    time.sleep(3)
    driver.find_element(cfg.get('org_index','buy_coursec2_by'),cfg.get('org_index','buy_coursec2')).click()
    time.sleep(3)    
    
#个人充值卡买课
def buy_course_usecard(cfg, driver, base_url, org_name):
    
    driver.get(base_url+org_name)
    time.sleep(8)
    driver.find_element_by_link_text(u"课程中心").click()
    time.sleep(10)
    driver.find_element_by_xpath('//html/body/div[2]/div[3]/div/div[2]/div[1]/div/p/a').click()
    time.sleep(8)
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    time.sleep(8)
    driver.find_element_by_link_text(u"立即购买").click()
    time.sleep(12)
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    driver.find_element_by_xpath('//html/body/div[3]/div[1]/div[2]/div/div[5]/div[4]/a').click()
    #driver.find_element(cfg.get('org_index','buy_coursec2_by'),cfg.get('org_index','buy_coursec2')).click()
    time.sleep(10)
    
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
def release_announcement(cfg,driver, base_url, org_name, title, an_content=u'这是公告内容公告内容'):
    
    driver.get(base_url+org_name)
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"网校公告").click()
    driver.implicitly_wait(5)
    driver.find_element(cfg.get('org_index','release_announcementx_by'),cfg.get('org_index','release_announcementx')).click()
    driver.find_element(cfg.get('org_index','release_announcementc_by'),cfg.get('org_index','release_announcementc')).send_keys(title)
    an_content = an_content.replace("\"","\\\"").replace("\'","\\\'")
    driver.implicitly_wait(2)
    driver.execute_script("var element=window.document.getElementById('editNotice_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');element.innerHTML='" +an_content+ "'")
    time.sleep(2)
    driver.find_element(cfg.get('org_index','release_announcementx2_by'),cfg.get('org_index','release_announcementx2')).click()
    time.sleep(1)
    return title

#获取视频外链发公告    
def release_href_course(cfg, driver, base_url, org_name):
    
    driver.get(base_url+org_name)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(u"(//a[contains(text(),'课程中心')])[2]").click()
    time.sleep(2)
    chref = driver.execute_script("return $(\".coursecenter-details-pic a\").eq(0).attr('href')")
    time.sleep(1)
    print chref
    driver.get("%s%s"%(base_url, chref)) 
    time.sleep(1)
    driver.find_element(cfg.get('org_index','release_hrefi_by'),cfg.get('org_index','release_hrefi')).click() 
    time.sleep(2)
    an_content = driver.execute_script("return $('textarea:eq(2)').text()")
    time.sleep(1)
    title = u'外链的哦'
    release_announcement(cfg,driver, base_url, org_name, title, an_content)
    time.sleep(2)
#机构修改头像
def org_chang_headpic(cfg, driver, base_url, org_name, head_pic = r"W:\Testing\Testing Files\Automation_test\headpic.jpg"):
    
    driver.get(base_url + "myOffice.do")
    time.sleep(5)
    driver.find_element(cfg.get('org_index','head_picname_by'),cfg.get('org_index','head_picname')).send_keys(head_pic)
    time.sleep(8)
#机构首页logo   
def change_homelogo(cfg, driver, base_url, org_name, logo_pic = r"W:\Testing\Testing Files\Automation_test\headpic.jpg"):
  
    driver.get(base_url + org_name)
    time.sleep(2)
    driver.execute_script("$('.edit-logo').attr('style','display:block;');$('.edit-logo-btn ').attr('style','display:block;'); \
    $('.fileinput-button input').eq(0).attr('style','height:300px;opacity:0;display:block;position:static;transform:translate(-300px, 0px) scale(4)')")
    time.sleep(1)
    driver.find_element(cfg.get('org_index','home_logoname_by'),cfg.get('org_index','home_logoname')).send_keys(logo_pic)
    time.sleep(2)

#修改页脚
def modify_pagefoot(cfg, driver, base_url, org_name):
   
    driver.get(base_url + org_name)
    time.sleep(4)
    driver.find_element_by_link_text(u"编辑页脚").click()
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    driver.find_element(cfg.get('org_index','pf_modx_by'),cfg.get('org_index','pf_modx')).click()
    time.sleep(5)
    driver.find_element(cfg.get('org_index','pf_modx2_by'),cfg.get('org_index','pf_modx2')).clear()
    time.sleep(5)
    driver.find_element(cfg.get('org_index','pf_modx3_by'),cfg.get('org_index','pf_modx3')).send_keys("0")
    time.sleep(2)
    driver.find_element(cfg.get('org_index','pf_modx4_by'),cfg.get('org_index','pf_modx4')).send_keys("sdfsdf")
    time.sleep(2)
    driver.find_element(cfg.get('org_index','pf_modc5_by'),cfg.get('org_index','pf_modc5')).click()
    time.sleep(4)


    
    