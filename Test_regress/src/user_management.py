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
    driver.find_element_by_id(cfg.get('','buy_course_id')).click()
    time.sleep(1)
    h = driver.window_handles
    #ch = driver.current_window_handle
    driver.switch_to_window(h[-1])

    driver.find_element_by_id(cfg.get('','use_rmb_id')).click()
    driver.find_element(cfg.get('','pay_ok_by'), cfg.get('','pay_ok')).click()
    time.sleep(5)

#个人充值卡买课
def buy_course_usecard(cfg, driver, course_url):
    
    driver.get(course_url)
    driver.find_element_by_id(cfg.get('','buy_course_id')).click()
    time.sleep(1)
    h = driver.window_handles
    #ch = driver.current_window_handle
    driver.switch_to_window(h[-1])
            
    driver.find_element(cfg.get('','pay_ok_by'), cfg.get('','pay_ok')).click()
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
def release_announcement(cfg,driver, base_url, org_name, title, an_content=u'这是公告内容公告内容'):
    
    driver.get(base_url+org_name)
    time.sleep(2)
    driver.find_element_by_link_text(u"网校公告").click()
    time.sleep(5)
    driver.find_element(cfg.get('org_index','ann_notice_xpath_by'),cfg.get('org_index','ann_notice_xpath')).click()
    time.sleep(2)
    #driver.find_element(cfg.get('org_index','ann_title_css_by'),cfg.get('org_index','ann_title_css')).send_keys(title) 
    #driver.find_element_by_css_selector("input.input360.titleName").send_keys(u"公告")
    driver.find_element(cfg.get('org_index','ann_select_css_by'),cfg.get('org_index','ann_select_css')).send_keys(u"公告")
    #driver.find_element_by_css_selector("span.mceIcon.mce_expandEdit").click()
    #time.sleep(2)
    #driver.find_element_by_css_selector("span.mceIcon.mce_code").click()
    an_content = an_content.replace("\"","\\\"").replace("\'","\\\'")
    #print an_content
    time.sleep(2)
    driver.execute_script("var element=window.document.getElementById('editNotice_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');element.innerHTML='" +an_content+ "'")
    time.sleep(5)
    driver.find_element(cfg.get('org_index','ann_ok_xpath_by'),cfg.get('org_index','ann_ok_xpath')).click()
    time.sleep(3)
    return title

#机构修改头像
def org_chang_headpic(cfg, driver, base_url, org_name, head_pic = r"W:\Testing\Testing Files\Automation_test\headpic.jpg"):
    
    #driver.get(base_url + org_name)
    #time.sleep(2)
    #driver.find_element_by_xpath(cfg.get('org_index','org_manage_xpath')).click()
    driver.get(base_url + "myOffice.do")
    time.sleep(5)
    #driver.execute_script("$('.fileinput-button input').eq(0).attr('style','height:300px;opacity:1;display:block;position:static;')")
    #driver.find_element_by_name("photo").click()
    #driver.execute_script("$(\"#J_oaiUploadTrigger input\").attr('style','display:opacity:1;display:block;')")
    #driver.execute_script("$('#J_oaiUploadTrigger input').click()")
    #driver.find_element_by_css_selector(cfg.get('org_manage','change_headpic_css')).click()
    #driver.find_element_by_link_text(u"修改头像").click()
    
    #driver.execute_script("$('.fileinput-button input').eq(0).attr('style','height:300px;opacity:1;display:block;position:static;transform:translate(-300px, 0px) scale(4)')") 
    #driver.find_element_by_name("photo").is_displayed()
    driver.find_element(cfg.get('org_index','head_picname_name_by'),cfg.get('org_index','head_picname_name')).send_keys(head_pic)
    #driver.find_element_by_name("photo").send_keys(head_pic)
    #driver.find_element_by_id(cfg.get('org_manage','headpic_upload_id')).send_keys(head_pic)
    #time.sleep(2)
    #driver.find_element_by_name('photo').is_displayed()   
    #driver.find_element_by_name('photo').send_keys(head_pic)
    #driver.findElement(By.xpath("//html/body/div/div/div[2]/div[3]/div[17]/div/div[2]/div/div/div/input")).is_displayed()
    #driver.findElement(By.xpath("//html/body/div/div/div[2]/div[3]/div[17]/div/div[2]/div/div/div/input")).send_keys(head_pic)
    #driver.find_element_by_xpath(cfg.get('org_manage','headpic_ok_xpath')).click()
    time.sleep(8)
    
def change_homelogo(cfg, driver, base_url, org_name, logo_pic = r"W:\Testing\Testing Files\Automation_test\headpic.jpg"):
  
    driver.get(base_url + org_name)
    time.sleep(2)
    #driver.find_element_by_name("files").send_keys(logo_pic)
    driver.find_element(cfg.get('org_index','home_logoname_name_by'),cfg.get('org_index','home_logoname_name')).send_keys(logo_pic)
    time.sleep(8)

def modify_pagefoot(cfg,driver, base_url, org_name):
   
    driver.get(base_url + org_name)
    time.sleep(2)
    driver.find_element_by_link_text(u"编辑页脚").click()
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    #driver.find_element_by_css_selector("span.bluebtn25_text").click()
    #driver.find_element_by_xpath("//html/body/div[3]/div[2]/div/a/span").click()
    driver.find_element(cfg.get('org_index','pf_mod_xpath_by'),cfg.get('org_index','pf_mod_xpath')).click()
    time.sleep(2)
    #driver.find_element_by_xpath("//html/body/div[3]/div[2]/div/ul/li[2]/div/input").clear()
    driver.find_element(cfg.get('org_index','pf_mod2_xpath_by'),cfg.get('org_index','pf_mod2_xpath')).clear()
    time.sleep(2)
    #driver.find_element_by_xpath("//html/body/div[3]/div[2]/div/ul/li[2]/div/input").send_keys("0")
    driver.find_element(cfg.get('org_index','pf_mod3_xpath_by'),cfg.get('org_index','pf_mod3_xpath')).send_keys("0")
    time.sleep(2)
    #driver.find_element_by_xpath("//html/body/div[3]/div[2]/div/ul/li[2]/div[2]/input").send_keys("sdfsd")
    driver.find_element(cfg.get('org_index','pf_mod4_xpath_by'),cfg.get('org_index','pf_mod4_xpath')).send_keys("sdfsdf")
    time.sleep(2)
    #driver.find_element_by_css_selector("button.submit-btn").click()
    driver.find_element(cfg.get('org_index','pf_mod5_css_by'),cfg.get('org_index','pf_mod5_css')).click()
    time.sleep(4)
    #driver.find_element_by_link_text(u"编辑页脚信息").click()
    #driver.find_element_by_xpath(cfg.get('','foot_info_xpath')).clear()
    #driver.find_element_by_xpath(cfg.get('','foot_info_xpath')).send_keys(foot_info)
    #driver.find_element_by_xpath(cfg.get('','foot_icp_xpath')).clear()
    #driver.find_element_by_xpath(cfg.get('','foot_icp_xpath')).send_keys(foot_icp)
    #driver.find_element_by_xpath(cfg.get('','foot_ok_xpath')).click()
    
def wailian_video(cfg, driver, base_url, test_enviroment):
    time.sleep(2)
    driver.get("http://www."+test_enviroment+".ablesky.com/kecheng/detail_251308")
    time.sleep(2)
    #driver.find_element_by_id("J_getVideoLink").click()
    driver.find_element(cfg.get('org_index','wl_ann_id1_by'),cfg.get('org_index','wl_ann_id1')).click()
    time.sleep(2)
    #driver.find_element_by_id("ZeroClipboardMovie_1").click()
    driver.find_element(cfg.get('org_index','wl_ann_id2_by'),cfg.get('org_index','wl_ann_id2')).click()
    time.sleep(2)
    driver.find_element_by_css_selector("button[type=\"button\"]").click()
    #driver.find_element(cfg.get('org_index','wl_ann_css_by'),cfg.get('org_index','wl_ann_css')).click()
    time.sleep(2)
    driver.find_element_by_link_text(u"网校公告").click()
    time.sleep(2)
    driver.find_element_by_link_text(u"新增公告").click()
    time.sleep(2)
    #driver.find_element_by_css_selector("input.input360.titleName").click()
    driver.find_element(cfg.get('org_index','wl_ann_css2_by'),cfg.get('org_index','wl_ann_css2')).click()
    time.sleep(2)
    #driver.find_element_by_css_selector("span.mceIcon.mce_code").click()
    driver.find_element(cfg.get('org_index','wl_ann_css3_by'),cfg.get('org_index','wl_ann_css3')).click()
    time.sleep(2)
    #driver.find_element_by_css_selector("input.input360.titleName").clear()
    driver.find_element(cfg.get('org_index','wl_ann_css2_by'),cfg.get('org_index','wl_ann_css2')).clear()
    time.sleep(5)
    #driver.find_element_by_css_selector("input.input360.titleName").send_keys(u"外链")
    driver.find_element(cfg.get('org_index','wl_ann_css2_by'),cfg.get('org_index','wl_ann_css2')).send_keys(u"外链")
    time.sleep(5)
    #driver.find_element_by_name("mceCodeSource").clear()
    driver.find_element(cfg.get('org_index','wl_ann_name_by'),cfg.get('org_index','wl_ann_name')).clear()
    
    driver.find_element_by_name("mceCodeSource").send_keys("<iframe height=480 width=640 src=\"http://www.gamma.ablesky.com/orgContentUrlAccess.do?action=getContentUrlEmbeddedPage&id=715200&courseId=251308&emKey=42fc457698c41bde60aa786f52a5c1c9\" frameborder=0 allowfullscreen></iframe>")
    time.sleep(2)
    driver.find_element_by_css_selector("div.dialog-button-container > button[type=\"button\"]").click()
    #driver.find_element(cfg.get('org_index','wl_ann_css4_by'),cfg.get('org_index','wl_ann_css4')).click()
    time.sleep(2)
    #driver.find_element_by_css_selector("button.edit-column-sure").click()
    driver.find_element(cfg.get('org_index','wl_ann_css5_by'),cfg.get('org_index','wl_ann_css5')).click()
    time.sleep(2)
    driver.find_element_by_link_text(u"外链").click()
    time.sleep(2)
    #driver.find_element_by_css_selector("div.content-right-noticeDetails").click()
    driver.find_element(cfg.get('org_index','wl_ann_css6_by'),cfg.get('org_index','wl_ann_css6')).click()
    time.sleep(2)
    
    