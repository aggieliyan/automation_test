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
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"学员/员工").click()
    driver.implicitly_wait(5)
    try:
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
            cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.find_element_by_link_text(u"学员管理").click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "stu_input_by"), \
    	cfg.get('org_manage', "stu_input")).send_keys(stu_name)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "stu_import_btn_by"), \
    	cfg.get('org_manage', "stu_import_btn")).click()
    time.sleep(2)

def import_multi_student(cfg, driver, base_url, org_name, stu_txt):

    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"学员/员工").click()
    driver.implicitly_wait(5)
    try:
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
            cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.find_element_by_link_text(u"学员管理").click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"批量导入学员").click()
    driver.implicitly_wait(30)
    driver.execute_script("$('#fileFieldName-file').attr('style','height:20px;opacity:1;transform:translate(0px, 0px) scale(0.5)')")
    driver.find_element(cfg.get('org_manage', "stu_file_by"), \
    	cfg.get('org_manage', "stu_file")).send_keys(stu_txt)
    driver.find_element(cfg.get('org_manage', "stu_file_ok_by"), \
    	cfg.get('org_manage', "stu_file_ok")).click()
    time.sleep(2)
#    count = 0
#    while is_element_present(driver, By.LINK_TEXT, u"继续批量导入学员") != True or count <= 30:
#        time.sleep(3)
#        count += 3

def create_student(cfg, driver, base_url, org_name, stu_txt):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"学员/员工").click()
    driver.implicitly_wait(5)
    try:
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
            cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.find_element_by_link_text(u"学员管理").click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "create_multi_by"), \
        cfg.get('org_manage', "create_multi")).click()
    driver.implicitly_wait(30)
    driver.execute_script("$('#fileFieldName-file').attr('style','height:20px;opacity:1;transform:translate(0px, 0px) scale(0.5)')")
    driver.find_element(cfg.get('org_manage', "stu_file_by"), \
    	cfg.get('org_manage', "stu_file")).send_keys(stu_txt)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "stu_file_ok_by"), \
    	cfg.get('org_manage', "stu_file_ok")).click()
    time.sleep(2)
#    count = 0
#    while is_element_present(driver, By.LINK_TEXT, u"继续批量创建学员") != True: #or count >= 30:
#        driver.implicitly_wait(3)
#        count += 3

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
    time.sleep(2)
    create_student(cfg, driver, base_url, org_name, stu_txt)
    time.sleep(5)

def open_course_for_one(cfg, driver, base_url, org_name, stu_num=1):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"学员/员工").click()
    try:
        driver.implicitly_wait(5)
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
        	cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.find_element_by_link_text(u"学员管理").click()
    time.sleep(5)
    # driver.find_element_by_xpath \
    # ("//div["+str(stu_num)+"]/table/tbody/tr/td[2]/div/p/a").click()
    driver.find_element(cfg.get('org_manage', "open_course_by"), \
    cfg.get('org_manage', "open_course")).click()
    #开通课程
    time.sleep(4)
    driver.find_element(cfg.get('org_manage', "open_cate_by"), \
    cfg.get('org_manage', "open_cate")).click()#未归类内容，展开资料
    time.sleep(5)
    driver.find_element(cfg.get('org_manage', "open_course_1_by"), \
    cfg.get('org_manage', "open_course_1")).click()#选中资料
    time.sleep(2)
    driver.find_element(cfg.get('org_manage', "open_ok_by"), \
    cfg.get('org_manage', "open_ok")).click()#确认开通
    time.sleep(2)
    driver.find_element(cfg.get('org_manage', "open_popup_by"), \
    cfg.get('org_manage', "open_popup")).click()#弹出框中确认
    time.sleep(2)

def open_course_for_multi(cfg, driver, base_url, org_name):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"学员/员工").click()
    try:
        driver.implicitly_wait(5)
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
        	cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.find_element_by_link_text(u"学员管理").click()
    time.sleep(5)
    driver.find_element(cfg.get('org_manage', "all_open_list_by"), \
    cfg.get('org_manage', "all_open_list")).click()#点击下拉框
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "all_open_by"), \
    cfg.get('org_manage', "all_open")).click()#选择批量开通课程
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "all_open_check_by"), \
    cfg.get('org_manage', "all_open_check")).click()#全选
    driver.implicitly_wait(30)
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
    time.sleep(2)
    driver.find_element(cfg.get('org_manage', "open_ok_by"), \
    cfg.get('org_manage', "open_ok")).click()#确认开通
    time.sleep(5)
    driver.find_element(cfg.get('org_manage', "open_popup_by"), \
    cfg.get('org_manage', "open_popup")).click()#弹出框中确认
    time.sleep(2)

#购买开通授权数 bnum为购买的数量
def buy_open_num(cfg, driver, base_url, org_name, bnum):
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element(cfg.get('org_manage', "buy_open_num_by"), \
        cfg.get('org_manage', "buy_open_num")).click()
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "buy_open_num_input_by"), \
        cfg.get('org_manage', "buy_open_num_input")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "buy_open_num_input_by"), \
        cfg.get('org_manage', "buy_open_num_input")).clear()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "buy_open_num_input_by"), \
        cfg.get('org_manage', "buy_open_num_input")).send_keys("1")
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "buy_open_num_sure1_by"), \
        cfg.get('org_manage', "buy_open_num_sure1")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('org_manage', "buy_open_num_sure2_by"), \
        cfg.get('org_manage', "buy_open_num_sure2")).click()
    time.sleep(2)

#管理播放授权数
def manage_course_num(cfg, driver, base_url):
    driver.get(base_url + "myOffice.do")
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"学员/员工").click()
    try:
        driver.implicitly_wait(5)
        driver.find_element(cfg.get('org_manage', "stu_close_by"), \
        	cfg.get('org_manage', "stu_close")).click()
    except:
        pass
    driver.find_element_by_link_text(u"学员管理").click()
    time.sleep(5)
    driver.find_element_by_link_text(u"管理播放授权数").click()
    driver.implicitly_wait(30)
    #未归类内容展开资料，可能没有开通未归类的课程
    try:
        driver.find_element(cfg.get('manage_course_num', \
            "manage_coursenum_opencouse_by"), \
    	    cfg.get('manage_course_num', "manage_coursenum_opencouse")).click()
        driver.implicitly_wait(30)
        #展开内容
        driver.find_element(cfg.get('manage_course_num', \
            "manage_coursenum_opennum_by"), \
    	    cfg.get('manage_course_num', "manage_coursenum_opennum")).click()
        driver.implicitly_wait(30)
        #修改剩余播放次数,刚开通课程，学员没有登录的不能修改
        try:
            driver.find_element_by_link_text(u"修改剩余播放次数").click()
            driver.implicitly_wait(30)
            driver.find_element(cfg.get('manage_course_num', \
                'manage_coursenum_change_by'), \
    	        cfg.get('manage_course_num', 'manage_coursenum_change')).clear()
            driver.implicitly_wait(30)
            driver.find_element(cfg.get('manage_course_num', \
                'manage_coursenum_change_by'), \
    	        cfg.get('manage_course_num', 'manage_coursenum_change')).send_keys("1")
            driver.implicitly_wait(30)
            driver.find_element_by_link_text(u"保存").click()
            time.sleep(1)
        except:
            pass
            time.sleep(1)
    except:
        pass
    #批量增加剩余授权数
    driver.find_element(cfg.get('manage_course_num', \
        'manage_coursenum_all_by'), \
        cfg.get('manage_course_num', 'manage_coursenum_all')).click()
    time.sleep(1)
    driver.find_element(cfg.get('manage_course_num', \
        'manage_coursenum_allnum_by'), \
        cfg.get('manage_course_num', 'manage_coursenum_allnum')).send_keys("1")
    time.sleep(1)
    driver.find_element(cfg.get('manage_course_num', \
        'manage_coursenum_apply_by'), \
        cfg.get('manage_course_num', 'manage_coursenum_apply')).click()
    time.sleep(2)
 