# -*- coding: UTF-8 -*-
'''
Created on Aug 12, 2013

@author: yilulu
'''
import re
import time
from selenium.common.exceptions import NoSuchElementException

from PO.course_page import CourseStepOnePage, CourseInfoPage
from PO.class_page import OnLineClassListPage, ClassInfoPage
from PO.agency_page import CourseAgencyPage, AgentCourseInputPage

def course_redirect(cfg, driver, base_url, isthree=0,\
    course_title=u"course", course_describe='hello world', \
    course_tags='english\n', course_price=0):
    """
    upload是发点播课程的时候需要用的，1是存储空间上传，2是本地上传
    isthree代表是不是发三分屏，1代表发三分屏，0代表发的是单视频, 2代表发双视频
    本地上传没了，先留着不去掉了。
    如果是本地上传的话 course_file 是要上传文件的本地路径
    course_title 是要发的课程的课程标题
    course_describe 是课程信息页面的课程详情
    course_tags 标签
    course_price 价格 填0时为免费的课
    """

    course = CourseStepOnePage(driver, cfg)
    #进入发课页面
    course.open()

    if isthree != 0:
        course.choose_three_video()
        
        #三分屏左上角的必须传视频文件
        course.click_upload(1)
        course.choose_flv()
        course.click_choose_ok()

        #双视频的右边讲义部分传视频flv，普通三分屏传pdf
        course.click_upload(2)
        if isthree == 1:
            course.choose_pdf()
        else:
            course.choose_flv()
        course.click_choose_ok()

    else:
        course.click_upload(0)
        course.choose_flv()
        course.click_choose_ok()     

    course.click_next_step()
    #第二步填写课程信息页面
    course_info = CourseInfoPage(driver, cfg)
    course_info.input_course_title(course_title)

    #课程价格
    if course_price != 0:
        course_info.click_charge()
        course_info.input_price(str(course_price))


    course_info.input_description(course_describe)
    course_info.click_service_cate()
    course_info.input_tag(course_tags)
    course_info.click_save()

def class_redirect(cfg, driver, base_url, classname='onlineclass', \
    ctype=1, price=10, course_describe='hello world', course_tags='english\n'):
    '''
    ctype代表发课类型，1代表普通网络班（打包），2代表预售网络班
    '''

    olclass = OnLineClassListPage(driver, cfg)
    olclass.open()
    olclass.click_create()

    cinfo = ClassInfoPage(driver, cfg)
    if ctype == 1:
        cinfo.chooes_course()
    else:
        cinfo.click_presell()
        cinfo.choose_cate()
        cinfo.input_price(price)

    cinfo.input_classname(classname)
    cinfo.input_description(course_describe)
    cinfo.input_tag(course_tags)
    cinfo.click_service_cate()
    cinfo.click_save()

#发布代理课程-没有发布了现在代理人只能编辑代理的课程
def release_agency_course(cfg, driver, base_url, course_title=u'代理课程'):

    cg = CourseAgencyPage(driver, cfg)
    cg.open()
    cg.click_manage_course()
    cg.click_edit()

    ac = AgentCourseInputPage(driver, cfg)
    ac.input_title(course_title)

    str_price = driver.execute_script(\
        "return $('.ablableSNew .colorGreen').text()")
    if str_price:
        temp = re.search(r'\d{1,10}.\d', str_price)
        price = temp.group(0)
        ac.input_price()
        ac.input_rank(100)

    ac.click_save()
