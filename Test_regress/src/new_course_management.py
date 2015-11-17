# -*- coding: UTF-8 -*-
'''
Created on Aug 12, 2013

@author: yilulu
'''
import re
import time
from selenium.common.exceptions import NoSuchElementException

from PO.course_page import CourseStepOnePage, CuorsefilePage, CourseInfoPage, CourseManageListPage
from PO.class_page import OnLineClassListPage, ClassInfoPage
from PO.agency_page import CourseAgencyPage, AgentCourseInputPage

def course_redirect(cfg, driver, base_url, isthree=0,\
    course_title=u"course", course_describe='hello world', \
    course_tags='english\n', course_price=0, chapter=0):
    """
    upload是发点播课程的时候需要用的，1是存储空间上传，2是本地上传
    isthree代表是不是发三分屏，1代表发三分屏，0代表发的是单视频, 2代表发双视频
    本地上传没了，先留着不去掉了。
    如果是本地上传的话 course_file 是要上传文件的本地路径
    course_title 是要发的课程的课程标题
    course_describe 是课程信息页面的课程详情
    course_tags 标签
    course_price 价格 填0时为免费的课
    chapter 表示是否带章节0为不带 1 为带
    """

    course = CourseStepOnePage(driver, cfg)
    #进入发课页面
    course.open()
    course.save_screenshot()
    
    course.input_course_title(course_title)
    course.click_service_cate()

    
    course.save_screenshot()
    course.click_next_step()

    #课程章节页面，传课件
    cfile = CuorsefilePage(driver, cfg)

    cnum = 0
    cfile.click_know()
    if chapter:
        cfile.click_add_chapter()
        cfile.input_cname()
        cfile.click_save()
        cfile.click_add_section()
        cfile.input_cname(1)
        cfile.click_save()
        cnum = 2


    cfile.click_add_classhour(cnum)
    if isthree != 0:
        cfile.choose_three_video()
        cfile.input_cname()
        
        # #三分屏左上角的必须传视频文件
        cfile.click_add(0)
        cfile.choose_flv()
        cfile.click_choose_ok()

        # #双视频的右边讲义部分传视频flv，普通三分屏传pdf
        cfile.click_add(0)
        if isthree == 1:
            cfile.choose_pdf()
        else:
            cfile.choose_flv()
        cfile.click_choose_ok()

        cfile.click_save()
    else:
        cfile.click_singlevideo()
        cfile.choose_flv()
        cfile.click_choose_ok()

    cfile.save_screenshot()

    cfile.click_info()

    #课程信息页面
    course_info = CourseInfoPage(driver, cfg)
     
    #课程价格
    if course_price != 0:
        course_info.click_charge()
        course_info.input_price(str(course_price))
   
    course_info.input_tag(course_tags)
    course_info.input_description(course_describe)
    course_info.save_screenshot()
    course_info.click_save()

def course_edit(cfg, driver):
    couremanage = CourseManageListPage(driver, cfg)
    couremanage.open()
    couremanage.click_manage()
    couremanage.click_edit()
    couremanage.click_window_ok()
    
    courefile = CuorsefilePage(driver, cfg)
    courefile.click_know()
    courefile.click_info()
    
    courseinfo = CourseInfoPage(driver, cfg)
    courseinfo.click_teacher()
    courseinfo.click_choiceteacher()
    courseinfo.choice_firsteacher()
    courseinfo.click_window_sure()
    courseinfo.click_save()
    driver.refresh()
    
def class_redirect(cfg, driver, base_url, classname='onlineclass', \
    ctype=1, price=10, course_describe='hello world', course_tags='english\n'):
    '''
    ctype代表发课类型，1代表普通网络班（打包），2代表预售网络班
    '''

    olclass = OnLineClassListPage(driver, cfg)
    olclass.open()
    olclass.save_screenshot()
    olclass.click_create()
    olclass.save_screenshot()

    cinfo = ClassInfoPage(driver, cfg)
    if ctype == 1:
        cinfo.chooes_course()
        cinfo.save_screenshot()
    else:
        cinfo.click_presell()
        cinfo.save_screenshot()
        cinfo.choose_cate()

    cinfo.input_current_price(price)
    cinfo.input_price(price)
    cinfo.input_classname(classname)
    cinfo.input_description(course_describe)
    cinfo.input_tag(course_tags)
    cinfo.click_service_cate()
    cinfo.click_save()
    time.sleep(2)

def class_face(cfg, driver, base_url, classname, address, classnum, \
    price=10, course_describe='hello world', course_tags='english\n'):
    
    olclass = OnLineClassListPage(driver, cfg)
    olclass.open()
    olclass.save_screenshot()
    olclass.click_classface()
    olclass.click_create()
    olclass.save_screenshot()

    cinfo = ClassInfoPage(driver, cfg)
    cinfo.input_classname(classname)
    cinfo.input_current_price(price)
    cinfo.input_price(price)
    cinfo.input_classadress(address)
    cinfo.input_classnum(classnum)
    cinfo.input_description(course_describe)
    cinfo.input_tag(course_tags)
    cinfo.click_service_cate()
    cinfo.click_save()
    time.sleep(2)
    
#发布代理课程-没有发布了现在代理人只能编辑代理的课程
def release_agency_course(cfg, driver, base_url, course_title=u'代理课程'):

    cg = CourseAgencyPage(driver, cfg)
    cg.open()
    cg.save_screenshot()
    cg.click_manage_course()
    cg.click_edit()

    ac = AgentCourseInputPage(driver, cfg)
    ac.click_modify()
    ac.input_title(course_title)
    ac.click_modify_ok()
    # ac.save_screenshot()

    # str_price = driver.execute_script(\
    #     "return $('.ablableSNew .colorGreen').text()")
    # if str_price:
    #     temp = re.search(r'\d{1,10}.\d', str_price)
    #     price = temp.group(0)
    #     ac.input_price(price)
    #     ac.input_rank(100)
    ac.save_screenshot()
    ac.click_save()
