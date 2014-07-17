# -*- coding: UTF-8 -*-

import time,re,user_management,random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def is_element_present(driver,how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException, e: 
        return False
    return True
#发布普通资料    
def release_normal_course(cfg,driver,base_url,org_name,course_file =u"D:\\rename-manual.pdf",
                          course_title=u"英语听力训练30天",course_describe='hello world',course_cate ='120101',course_tags='english',course_price=10 ):
        
    driver.get(base_url + org_name)
    driver.find_element_by_link_text(u'发布知识资料').click()
    time.sleep(2)
    driver.find_element_by_id(cfg.get('courseRedirect','local_upload_id')).click() 
    driver.find_element_by_id(cfg.get('courseRedirect','file_input_id')).send_keys(course_file) 
    driver.find_element_by_xpath(cfg.get('courseRedirect','upload_btn_xpath')).click()
    time.sleep(5)
    
    driver.find_element_by_id(cfg.get('courseRedirect','title_id')).send_keys(course_title)      
    driver.execute_script("var element=window.document.getElementById('introduce_field_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');element.innerHTML =\'"+course_describe+"\';")
    driver.execute_script("window.document.getElementById(\'"+cfg.get('courseRedirect','category_id')+"\').value = " + course_cate)
    driver.find_element_by_id(cfg.get('courseRedirect','tags_id')).send_keys(course_tags)
    
    if course_price != 0:
        driver.find_element_by_id(cfg.get('courseRedirect','price_id')).send_keys(course_price)
    
    finish_id = cfg.get('courseRedirect','finish_btn_id')
         
    driver.find_element_by_id(finish_id).click()
    time.sleep(2)

def release_course_from_space(cfg,driver,base_url,org_name,
                          course_title=u"自动化-从空间选文件",course_describe='hello world',course_cate ='120101',course_tags='english',course_price=10):

    driver.get(base_url + org_name)
    driver.find_element_by_link_text(u'发布知识资料').click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@onclick='stepTwo.selFtp();']").click()
    driver.find_element_by_name("selFtpRadio").click()
    driver.find_element_by_xpath("//div[3]/div/div/div/div/div/div/table/tbody/tr/td[2]/em/button").click()
    driver.find_element_by_id(cfg.get('courseRedirect','title_id')).send_keys(course_title)      
    driver.execute_script("var element=window.document.getElementById('introduce_field_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');element.innerHTML =\'"+course_describe+"\';")
    driver.execute_script("window.document.getElementById(\'"+cfg.get('courseRedirect','category_id')+"\').value = " + course_cate)
    driver.find_element_by_id(cfg.get('courseRedirect','tags_id')).send_keys(course_tags)
    
    if course_price != 0:
        driver.find_element_by_id(cfg.get('courseRedirect','price_id')).send_keys(course_price)
    
    driver.find_element_by_id(cfg.get('courseRedirect','finish_btn_id')).click()
    time.sleep(4)    
#发布三分屏
def release_three_video(cfg,driver,base_url,org_name,video_file =u"D:\\yilulu\\测试素材\\shenqi.wmv.asc.flv",pdf_file = u"D:\\yilulu\\测试素材\\构建自己的自动化平台000.pdf",
                          course_title=u"三分屏-英语听力训练30天",course_describe='hello world',course_cate ='120101',course_tags='english',course_price=10 ):
     
    driver.get(base_url + org_name)
    time.sleep(3)
    driver.find_element_by_link_text("发布知识资料").click()
    time.sleep(2)
    driver.find_element_by_css_selector(cfg.get('courseRedirect','three_video_css')).click()
    time.sleep(2)
    driver.find_element_by_id(cfg.get('courseRedirect','local_upload_id')).click()
    time.sleep(2)
    driver.find_element_by_id(cfg.get('courseRedirect','file_input_id')).send_keys(video_file) 
    driver.find_element_by_xpath(cfg.get('courseRedirect','upload_btn_xpath')).click()
    time.sleep(3)
    driver.find_element_by_id(cfg.get('courseRedirect','PDFfile_input_id')).send_keys(pdf_file)
    driver.find_element_by_xpath(cfg.get('courseRedirect','upload_pdf_btn_xpath')).click()
    time.sleep(3)
    driver.find_element_by_id(cfg.get('courseRedirect','title_id')).send_keys(course_title)
    time.sleep(2)
    driver.execute_script("var element=window.document.getElementById('introduce_field_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');element.innerHTML =\'"+course_describe+"\';")
    driver.execute_script("window.document.getElementById(\'"+cfg.get('courseRedirect','category_id')+"\').value = " + course_cate)
    driver.find_element_by_id(cfg.get('courseRedirect','tags_id')).send_keys(course_tags)
    
    if course_price != 0:
        driver.find_element_by_id(cfg.get('courseRedirect','price_id')).send_keys(course_price)
    
    driver.find_element_by_id(cfg.get('courseRedirect','finish_btn_id')).click()
    time.sleep(2)
    
#打包    
def package_course(cfg, driver,base_url,org_name,course_title=u"英语听力训练30天",course_describe='hello world',course_cate ='1001',course_tags='english'):
    
    driver.get(base_url + org_name)
    driver.find_element_by_link_text(u"打包系列资料").click()
    time.sleep(3)
    #选择放入包中的资料
    driver.find_element_by_xpath(cfg.get('courseRedirect','package_content_1_xpath')).click()
    #driver.find_element_by_xpath(cfg.get('courseRedirect','package_content_2_xpath')).click()
        
    driver.find_element_by_xpath(cfg.get('courseRedirect','package_ok_btn_xpath')).click()#确定
    time.sleep(3)
        
    driver.find_element_by_id(cfg.get('courseRedirect','finish_btn_id')).click()#第一步完成
    time.sleep(3)
    driver.find_element_by_id(cfg.get('courseRedirect','title_id')).send_keys(course_title)
    time.sleep(3)
    driver.execute_script("var element=window.document.getElementById('introduce_field_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');element.innerHTML =\'"+course_describe+"\';")
    driver.execute_script("window.document.getElementById(\'"+cfg.get('courseRedirect','category_id')+"\').value = " + course_cate)
    driver.find_element_by_id(cfg.get('courseRedirect','tags_id')).send_keys(course_tags)
    driver.find_element_by_id(cfg.get('courseRedirect','package_next_id')).click()
    time.sleep(2)
  
#预售      
def pre_sale_course(cfg, driver,base_url,org_name,course_title=u"自动化-预售",course_describe=u'预售内容描述',course_cate ='1001',course_tags=u'预售',course_price=40):
        
    driver.get(base_url + org_name)
    driver.find_element_by_link_text("发布预售资料").click()
    time.sleep(2)
    driver.find_element_by_name("cateTreeInput").click()
    driver.find_element_by_id(cfg.get('courseRedirect','title_id')).send_keys(course_title)
    driver.execute_script("var element=window.document.getElementById('introduce_field_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');element.innerHTML =\'"+course_describe+"\';")
    driver.execute_script("window.document.getElementById(\'"+cfg.get('courseRedirect','category_id')+"\').value = " + course_cate)
    driver.find_element_by_id(cfg.get('courseRedirect','tags_id')).send_keys(course_tags)
    if course_price != 0:
        driver.find_element_by_id(cfg.get('courseRedirect','price_id')).send_keys(course_price)
        
    driver.find_element_by_id(cfg.get('courseRedirect','finish_btn_id')).click()
    time.sleep(2)

#发布代理课程    
def release_agency_course(cfg,driver, base_url, org_name,course_title=u'代理课程'):
    
    driver.get(base_url + org_name)
    time.sleep(2)
    driver.find_element_by_xpath(cfg.get('org_index','org_manage_xpath')).click()
    time.sleep(2)  
    driver.find_element_by_link_text(u"管理我申请的代理").click()
    driver.find_element_by_link_text(u"管理代理资料").click()
    driver.find_element_by_link_text(u"发布").click()
    time.sleep(3)
    driver.find_element_by_id(cfg.get('courseRedirect','title_id')).clear()
    driver.find_element_by_id(cfg.get('courseRedirect','title_id')).send_keys(course_title)
    str_price = driver.execute_script("return $('.ablableSNew .colorGreen').text()")
    #print str_price 
    try:
        temp = re.search(r'\d{1,10}.\d',str_price) 
        price = temp.group(0)
    
        driver.find_element_by_id(cfg.get('courseRedirect','price_id')).clear()
        driver.find_element_by_id(cfg.get('courseRedirect','price_id')).send_keys(price)
        driver.find_element_by_id("courseRank").clear()
        driver.find_element_by_id("courseRank").send_keys(100)
        time.sleep(3)
    except Exception, e:#如果是免费的代理课程会在上面取价格的时候就会报错，免费的直接点发布即可
        pass
    finally:
        driver.find_element_by_id(cfg.get('courseRedirect','finish_btn_id')).click()
        time.sleep(2)
    
    
def release_href_course(cfg,driver, base_url, org_name):
    
    rand_name = str(random.randint(1000,9999))
    an_title = u'外链了视频的公告'+rand_name
    
    driver.get(base_url + org_name)
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='orgTab']/div[2]/div[2]/a").click()
    time.sleep(2)
    driver.find_element_by_link_text(u"获取视频链接").click()
    href = driver.execute_script("return document.getElementsByTagName('textarea')[1].value")
    #print href
    
    an_content = href
    user_management.release_announcement(cfg, driver, base_url, org_name, an_title, an_content)
    
    return an_title
    