# -*- coding: UTF-8 -*-
'''
Created on Aug 12, 2013

@author: yilulu
'''
import time
import login

def course_redirect(cfg, driver, base_url, ctype= 1, isthree=0, upload=1, course_file =u"D:\\manual.pdf",course_title=u"course",course_describe='hello world',course_tags='english',course_price=0):
    """
    ctype代表发课类型 1表示点播课程，2表示系列课程，3表示预售课程
    upload是发点播课程的时候需要用的，1是存储空间上传，2是本地上传
    isthree代表是不是发三分屏，1代表发三分屏，0代表发的是单视频
    本地上传没了，先留着不去掉了。
    如果是本地上传的话 course_file 是要上传文件的本地路径
    course_title 是要发的课程的课程标题
    course_describe 是课程信息页面的课程详情
    course_tags 标签
    course_price 价格 填0时为免费的课
    
    """
    #进入发课页面
    url = "%s/coursePostRedirect.do?action=courseStepOne"%(base_url)#
    driver.get(url)
    time.sleep(1)
    
    #发点播课程
    if ctype == 1:        
        #从存储空间上传
        if isthree == 1:#发三分屏
            driver.find_element_by_class_name(cfg.get('courseRedirect','threevideo_class')).click()
            driver.find_elements_by_css_selector(cfg.get('courseRedirect','upload_btn_css'))[1].click()
            time.sleep(1)
            driver.execute_script("$(\'.spacefile-name input\').last().click()")
            driver.execute_script("$(\'.dialog-button-container button\').eq(0).click()")
            time.sleep(1)
        
            driver.find_elements_by_css_selector(cfg.get('courseRedirect','upload_btn_css'))[2].click()
            time.sleep(1)
            driver.execute_script("$(\'.spacefile-name input\').eq(0).click()")
            driver.execute_script("$(\'.dialog-button-container button\').eq(0).click()")
            time.sleep(1)
            
            driver.find_elements_by_class_name(cfg.get('courseRedirect','next_btn_class'))[1].click()
        else:#单视频
            if upload == 1:
                driver.find_element_by_css_selector("span.greenbtn30_text").click()
                time.sleep(1)
                
                #全选          
                #driver.execute_script("$(\'.bottomInfo input\').eq(0).click()")
                driver.find_element_by_name("checkAll").click()
                
                driver.execute_script("$(\'.dialog-button-container button\').eq(0).click()")
                time.sleep(1)
            #本地上传
            else:        
                #把input显示出来才可以用否则会报当前元素不可见的错
                driver.execute_script("$('.fileinput-button input').eq(0).attr('style','height:20px;opacity:1;display:block;position:static;transform:translate(0px, 0px) scale(1)')")
                time.sleep(1)
                input = driver.find_element_by_name("files").send_keys(course_file)
                time.sleep(3)
            
            driver.find_element_by_name("files").send_keys(u"D:\\manual.pdf")
            driver.find_element_by_id(cfg.get('courseRedirect','single_btn_id')).click()          
    
    #发布系列课程
    elif ctype == 2:
        driver.find_element_by_class_name("seriescourse").click()
        driver.find_element_by_name("checkAll").click()
        driver.find_element_by_id(cfg.get('courseRedirect','series_btn_id')).click()
    #发布预售课程
    elif ctype == 3:
        driver.find_element_by_class_name("presellcourse").click()  
        driver.find_element_by_name("cateTreeInput").click() 
        driver.find_element_by_id(cfg.get('courseRedirect','presell_btn_id')).click()  
                              
    #发课第二步-课程信息页面
    time.sleep(2)
    driver.find_element_by_name("courseTitle").click()
    driver.find_element_by_name("courseTitle").send_keys(course_title)
    #设置价格
    if course_price != 0:
        driver.find_element_by_id("J_charge").click()
        driver.find_element_by_name(cfg.get('courseRedirect','price_name')).send_keys(course_price)            
    #填课程详情
    driver.execute_script("var element=window.document.getElementById('courseDesc-editor_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');element.innerHTML =\'"+course_describe+"\';")
    #选择服务分类
    driver.execute_script("$(\'li.level2\').click()") 
    driver.execute_script("$(\'li.level3.selected\').click()")    
    #填写课程标签
    driver.find_element_by_css_selector("div.text-layer.clearfix > input[type=\"text\"]").send_keys(course_tags)
    time.sleep(1)
    #完成
    driver.find_element_by_id(cfg.get('courseRedirect','done_btn_id')).click()
    time.sleep(2)

def class_redirect(driver, base_url):
    classname = "onlineclass"
    course_describe = "hello"
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"报班管理").click()
    time.sleep(3)
    driver.find_element_by_css_selector("span.greenbtn25_text").click()
    driver.find_element_by_id("J_className").send_keys(classname)
    driver.find_element_by_name("checkAll").click()
    time.sleep(1)
    #填课程详情
    driver.execute_script("var element=window.document.getElementById('courseDescribe-editor_ifr');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');element.innerHTML =\'"+course_describe+"\';")
    driver.find_element_by_css_selector("div.text-layer.clearfix > input[type=\"text\"]").send_keys("english")
    driver.find_element_by_xpath("xpath=(//input[@name='category'])[1]").click()
    #选择服务分类
    driver.execute_script("$(\'li.level2\').click()") 
    driver.execute_script("$(\'li.level3.selected\').click()") 
    driver.execute_script("$('.greenbtn25_text').click()")
    time.sleep(5)
    driver.save_screenshot(r'D:/test_rs_pic/onlineclass.png')
    
def forsale_couse(driver, base_url):
    filepath = "W:\Testing\auto_test_file\headpic.jpg"
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"发布特惠课程").click()
    time.sleep(3)
    driver.find_element_by_id("selectCourseBtn").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[3]/div/div/table/tbody/tr/td[2]/em/button").click()
    time.sleep(2)
    price = driver.execute_script("return $('#oldPrice').text()")
    driver.find_element_by_id("asprice_field").send_keys(price)
    driver.find_element_by_id("picFieldName-file").send_keys(filepath)
    driver.find_element_by_xpath("//div[3]/div/div/table/tbody/tr/td[2]/em/button").click()
    driver.find_element_by_id("total_field").send_keys("100")
    driver.find_element_by_id("preset_field").send_keys("0")
    driver.find_element_by_id("ext-gen48").click()