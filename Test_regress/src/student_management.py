# -*- coding: UTF-8 -*-
'''
Created on Jun 2, 2012

@author: yilulu
'''
import time, random
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def is_element_present(driver, how, what):
    try: driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

def import_one_student(cfg, driver, base_url, org_name, stu_name):

    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员/员工").click()
    driver.implicitly_wait(2)
    try:
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
            cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员管理").click()
    driver.find_element(cfg.get('org_manage', "stu_input_by"), \
    	cfg.get('org_manage', "stu_input")).send_keys(stu_name)
    driver.implicitly_wait(1)
    driver.find_element(cfg.get('org_manage', "stu_import_btn_by"), \
    	cfg.get('org_manage', "stu_import_btn")).click()
    driver.implicitly_wait(3)

def import_multi_student(cfg, driver, base_url, org_name, stu_txt):

    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员/员工").click()
    driver.implicitly_wait(2)
    try:
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
            cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.implicitly_wait(5)
    driver.find_element_by_link_text(u"学员管理").click()
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"批量导入学员").click()
    driver.implicitly_wait(2)
    driver.find_element(cfg.get('org_manage', "stu_file_by"), \
    	cfg.get('org_manage', "stu_file")).send_keys(stu_txt)
    driver.find_element(cfg.get('org_manage', "stu_file_ok_by"), \
    	cfg.get('org_manage', "stu_file_ok")).click()
    count = 0
    while is_element_present(driver, By.LINK_TEXT, u"继续批量导入学员") != True or count <= 30:
        time.sleep(3)
        count += 3

def create_student(cfg, driver, base_url, org_name, stu_txt):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员/员工").click()
    driver.implicitly_wait(2)
    try:
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
            cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员管理").click()
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"批量创建学员").click()
    driver.implicitly_wait(2)
    driver.find_element(cfg.get('org_manage', "stu_file_by"), \
    	cfg.get('org_manage', "stu_file")).send_keys(stu_txt)
    driver.implicitly_wait(2)
    driver.find_element(cfg.get('org_manage', "stu_file_ok_by"), \
    	cfg.get('org_manage', "stu_file_ok")).click()
    driver.implicitly_wait(2)
    count = 0
    while is_element_present(driver, By.LINK_TEXT, u"继续批量创建学员") != True: #or count >= 30:
        driver.implicitly_wait(3)
        count += 3

def auto_create_student(cfg, driver, base_url, org_name, stu_num):
    #自动生成用户名文件创建学员
    #stu_num为需要创建学员的数量
    prefix = chr(random.randint(97, 122)) + chr(random.randint(97, 122)) \
     + chr(random.randint(97, 122))
    stu_txt = r"C:\create_stu.txt"
    stu_file = open(stu_txt, 'w')
    for i in range(stu_num):
        stu_name = 'stu_' + prefix + str(i)
        stu_psw = '1234aa'
        if i == 0:
            stu_file.writelines(" \n")
        stu_file.writelines(stu_name + " " + stu_psw + "\n")
    stu_file.close()
    create_student(cfg, driver, base_url, org_name, stu_txt)

def open_course_for_one(cfg, driver, base_url, org_name, stu_num=1):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员/员工").click()
    try:
        driver.implicitly_wait(2)
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
        	cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员管理").click()
    time.sleep(5)
    # driver.find_element_by_xpath \
    # ("//div["+str(stu_num)+"]/table/tbody/tr/td[2]/div/p/a").click()
    driver.find_element(cfg.get('org_manage', "open_course_by"), \
    cfg.get('org_manage', "open_course")).click()
    #开通知识资料
    time.sleep(4)
    driver.find_element(cfg.get('org_manage', "open_cate_by"), \
    cfg.get('org_manage', "open_cate")).click()#未归类内容，展开资料
    time.sleep(5)
    driver.find_element(cfg.get('org_manage', "open_course_1_by"), \
    cfg.get('org_manage', "open_course_1")).click()#选中资料
    driver.find_element(cfg.get('org_manage', "open_ok_by"), \
    cfg.get('org_manage', "open_ok")).click()#确认开通
    time.sleep(2)
    driver.find_element(cfg.get('org_manage', "open_popup_by"), \
    cfg.get('org_manage', "open_popup")).click()#弹出框中确认
    time.sleep(2)

def open_course_for_multi(cfg, driver, base_url, org_name):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员/员工").click()
    try:
        driver.implicitly_wait(2)
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
        	cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员管理").click()
    time.sleep(5)
    driver.find_element(cfg.get('org_manage', "all_open_list_by"), \
    cfg.get('org_manage', "all_open_list")).click()#点击下拉框
    driver.implicitly_wait(2)
    driver.find_element(cfg.get('org_manage', "all_open_by"), \
    cfg.get('org_manage', "all_open")).click()#选择批量开通课程
    driver.implicitly_wait(2)
    driver.find_element(cfg.get('org_manage', "all_open_check_by"), \
    cfg.get('org_manage', "all_open_check")).click()#全选
    driver.implicitly_wait(2)
    #driver.find_element_by_xpath(u"//a[contains(text(),'应用')]").click()
    #driver.execute_script("$('#studentListDiv .ls_openClose').click()")
    driver.find_element(cfg.get('org_manage', "all_open_apply_by"), \
    cfg.get('org_manage', "all_open_apply")).click()#应用
    time.sleep(6)
    driver.find_element(cfg.get('org_manage', "open_cate_by"), \
    cfg.get('org_manage', "open_cate")).click()#未归类内容，展开资料
    time.sleep(5)
    driver.find_element(cfg.get('org_manage', "open_course_1_by"), \
    cfg.get('org_manage', "open_course_1")).click()#选中资料
    driver.find_element(cfg.get('org_manage', "open_ok_by"), \
    cfg.get('org_manage', "open_ok")).click()#确认开通
    time.sleep(1)
    driver.find_element(cfg.get('org_manage', "open_popup_by"), \
    cfg.get('org_manage', "open_popup")).click()#弹出框中确认
    time.sleep(2)

#购买开通授权数 bnum为购买的数量
def buy_open_num(cfg, driver, base_url, org_name, bnum):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(3)
    driver.find_element_by_link_text("在线购买授权数").click()
    driver.implicitly_wait(3)
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    driver.find_element_by_class_name("payBtn").click()
    driver.implicitly_wait(3)
    driver.find_element(cfg.get('org_manage', "buy_open_num_sure_by"), \
    	cfg.get('org_manage', "buy_open_num_sure")).click()
    driver.implicitly_wait(3)
    driver.find_element_by_link_text(u"继续购买授权").click()
    driver.implicitly_wait(3)

#管理播放授权数
def manage_course_num(cfg, driver, base_url):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员/员工").click()
    try:
        driver.implicitly_wait(2)
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
        	cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.implicitly_wait(2)
    driver.find_element_by_link_text(u"学员管理").click()
    time.sleep(5)
    driver.find_element_by_link_text("管理播放授权数").click()
    driver.implicitly_wait(2)
    driver.find_element(cfg.get('manage_course_num', \
        "manage_coursenum_opencouse_by"), \
    	cfg.get('manage_course_num', "manage_coursenum_opencouse")).click()
    driver.implicitly_wait(2)
    driver.find_element(cfg.get('manage_course_num', \
        "manage_coursenum_opennum_by"), \
    	cfg.get('manage_course_num', "manage_coursenum_opennum")).click()
    driver.implicitly_wait(2)
    driver.find_element_by_link_text("修改剩余播放次数").click()
    driver.implicitly_wait(2)
    driver.find_element(cfg.get('manage_course_num', \
        'manage_coursenum_change_by'), \
    	cfg.get('manage_course_num', 'manage_coursenum_change')).clear()
    driver.implicitly_wait(2)
    driver.find_element(cfg.get('manage_course_num', \
        'manage_coursenum_change_by'), \
    	cfg.get('manage_course_num', 'manage_coursenum_change')).send_keys("1")
    driver.implicitly_wait(2)
    driver.find_element_by_link_text("保存").click()
 