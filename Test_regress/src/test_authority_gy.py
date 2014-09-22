# -*- coding: UTF-8 -*-
import os
import ConfigParser
import traceback
import time, random
from selenium import webdriver

import login
import new_course_management
import cate_management, student_management, new_course_management, card_management, user_management
    
def execute_func(func_name):
	func_name()

def check_menu(menu_title, menu_dic):
	try:
		time.sleep(2)
		ahref = driver.find_element_by_link_text(menu_title).get_attribute("href")
		#print ahref
		if ahref == "javascript:;":
			print u"没有%s权限"%menu_title
			return
		else:
			driver.find_element_by_link_text(menu_title).click()
		time.sleep(1)
		for item in menu_dic.keys():
			try:
				driver.implicitly_wait(5)
				driver.find_element_by_link_text(item).click()
				time.sleep(1)
				execute_func(menu_dic[item])
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有%s-%s权限"%(menu_title, item)
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有%s权限"%menu_title

def fore_stage():
    navi_dic = {u"首页":firstpage, 
                   u"课程中心":course_center_relate, 
                   u"报班中心":class_center_relate,
                   u"在线考试":online_exam_relate, 
                   u"网校公告":school_notice, 
                   u"直播课程":live_course_relate,
                   u"特惠课程":cheap_course_relate,
                   u"在线答疑":online_ansquestion, 
                   u"名师团队":teacher_team,
                   u"网校成员":school_members, 
                   u"关于我们":about_us,
                   u"帮助中心":help_center}
    check_navigation(navi_dic) 
    
def check_navigation(navi_dic): 
    time.sleep(1)   
    driver.find_element_by_link_text(u"网校首页").click()
    time.sleep(1)
    for item in navi_dic.keys():  
        try:
            driver.find_element_by_link_text(item).click()
        except:
            time.sleep(1)
            driver.execute_script("$('.dnl-list-ul').attr('style','display:block')")
            time.sleep(1)
            driver.find_element_by_link_text(u"导航管理").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"导航编辑").click()
            time.sleep(1)
            driver.find_element_by_link_texts(u"隐藏")[-1].click()#隐藏最后一个
            time.sleep(1)
            title = driver.execute_script("return $('.hidden-module-en .nav-items-uen .limitword').eq(0).val()")
            time.sleep(1)
            #显示第一个
            if navigation_title == title:
                driver.find_element_by_link_texts(u"显示")[0].click()
            #显示第二个
            else:            
                driver.find_element_by_link_texts(u"显示")[1].click()
            time.sleep(1)                   
            driver.find_element_by_link_text(u"保存").click()
            time.sleep(1)
        finally:           
            execute_func(navi_dic[item])
#切换窗口公共方法
def swithing_window(bh,ah):
     while len(bh) == len(ah):
	     ah = driver.window_handles
     for h in ah:
	     if h not in bh:
		     driver.switch_to_window(h)
		     	
#前台-首页导航
def firstpage():
	current_url = driver.current_url
	#首页装扮
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"首页装扮").click()
	    time.sleep(2)
	    driver.find_element_by_link_text(u"保存").click()
	except Exception:
		print traceback.format_exc()
		print u"所有管理员都应该有首页装扮的权限"
	
	#发布课程	
	time.sleep(1)
	try:
	    ah = driver.window_handles
	    driver.find_element_by_link_text(u"发布课程").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1)
	    alert = driver.switch_to_alert()
	    time.sleep(1)
	    alert.accept() 
	except Exception:
		print traceback.format_exc()
		print u"此管理员没有：教学教务-课程课件-课程管理-编辑权限"
	
	#导航管理	
	time.sleep(1)
	try:
	    time.sleep(1)
	    driver.execute_script("$('.dnl-list-ul').attr('style','display:block')")
	    time.sleep(1)
	    driver.find_element_by_link_text(u"导航管理").click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"导航编辑").click()
	    time.sleep(2)
	    driver.find_element_by_link_text(u"保存").click()
	    time.sleep(1)
	    driver.execute_script("$('.dnl-list-ul').attr('style','display:block')")
	    time.sleep(1)
	    driver.find_element_by_link_text(u"导航管理").click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"导航颜色").click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"保存").click()
	    time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"所有管理员都应该有导航管理的权限"
	
	#页面SEO	
	time.sleep(1)
	try:
		bh = driver.window_handles 	    
		driver.find_element_by_link_text(u"页面SEO").click()
		time.sleep(1)
		ah = driver.window_handles
		swithing_window(bh,ah)
		driver.find_element("class name", "submit-btn")#点击确定
		time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"所有管理员都应该有页面SEO的权限"

    #编辑页脚
	time.sleep(1)
	try:
		bh = driver.window_handles 	    
		driver.find_element_by_link_text(u"编辑页脚").click()
		time.sleep(1)
		ah = driver.window_handles
		swithing_window(bh,ah)
		driver.find_element("class name", "submit-btn")#点击确定
		time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"所有管理员都应该有编辑页脚的权限"

    #自定义页面
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"自定义页面").click()
	    time.sleep(1)
	    driver.get(current_url)
	except Exception:
		print traceback.format_exc()
		print u"所有管理员都应该有自定义页面的权限"
	
	#网校首页头像logo
	org_name = "salesdemo"	
	time.sleep(1)
	try:
	    user_management.change_homelogo(cfg, driver, base_url, org_name)
	    time.sleep(1)
	    driver.get(current_url)
	except Exception:
		print traceback.format_exc()
		print u"所有管理员都应该有修改网校首页头像页面的权限"

    #编辑课程关键词
	time.sleep(1)
	try:
	    driver.find_element("class name","keyword-mask").click()
	    time.sleep(1)
	    driver.find_element("css selector",".dialog-button-container button").click()#点击确定	    
	except Exception:
		print traceback.format_exc()
		print u"所有管理员都应该有编辑课程关键字的权限"
	
	#编辑右上角咨询热线和服务时间	
	time.sleep(2)
	try:
	    driver.find_element_by_link_text(u"编辑").click()
	    time.sleep(1)
	    driver.find_element("css selector",".dialog-button-container button").click()#点击确定	   
	except Exception:
		print traceback.format_exc()
		print u"所有管理员都应该有编辑咨询热线和服务时间的权限"   
#前台-课程中心（教学教务-课程课件-课程管理权限）
def course_center():
#    time.sleep(1)   
#    try:
#        #课程中心
#        driver.find_element_by_link_text(u"全部").click()
#        time.sleep(1)     
#    except Exception:
#        print traceback.format_exc()
#        print u"课程中心：没有教学教务-课程课件-课程管理的读权限"   
    current_url = driver.current_url	
    time.sleep(1)   
    try:
        #课程中心
        driver.execute_script("$('.coursecenter-module-hover').attr('style','display:block')")#显示隐藏操作
        #排序
        time.sleep(1)
        driver.find_element_by_link_text(u"排序").click()
        time.sleep(1)
        driver.find_element("class name", "courseRank").click()
        #置顶显示、取消置顶
        time.sleep(1)
        driver.execute_script("$('.coursecenter-module-hover').attr('style','display:block')")#显示隐藏操作
        time.sleep(1)
        driver.find_element_by_link_text(u"置顶显示").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"取消置顶").click()
        #获取视频链接
        time.sleep(1)
        driver.find_element_by_link_text(u"获取视频链接").click()
        time.sleep(1)
        driver.find_element("class name", "dialog-button-container").click()#点击关闭  
        #显示编辑
        time.sleep(1)
        driver.find_elements_by_link_text(u"编辑")[1].click()
        time.sleep(1)
        driver.find_element("id", "J_complete").click()#保存
        time.sleep(1)
        driver.execute_script("$('.coursecenter-module-hover').attr('style','display:block')")#显示隐藏操作
        time.sleep(1)   
        #显示编辑三分屏章节
        time.sleep(1)
        try:
            driver.find_element_by_link_text(u"编辑三分屏章节").click()
            time.sleep(1)
            driver.get(current_url)
            time.sleep(1)
            driver.execute_script("$('.coursecenter-module-hover').attr('style','display:block')")#显示隐藏操作
            time.sleep(1)        
        except:
            print '此页没有三分屏课程，没有编辑三分屏章节！'       
        #显示发布相似课程 
        time.sleep(1)  
        driver.execute_script("$('.coursecenter-module-hover').attr('style','display:block')")#显示隐藏操作      
        time.sleep(1)
        driver.find_element_by_link_text(u"发布相似课程").click()
        time.sleep(1)
        driver.get(current_url)
        alert = driver.switch_to_alert()
        alert.accept()    
    except Exception:
        print traceback.format_exc()
        print u"课程中心：没有教学教务-课程课件-课程管理的编辑权限"

    time.sleep(1)
    try:
        #课程中心
        driver.execute_script("$('.coursecenter-module-hover').attr('style','display:block')")#显示隐藏操作
        time.sleep(1)
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(1)
        driver.find_element("css selector",".dialog-button-container button").click()#删除
    except Exception:
        print traceback.format_exc()
        print u"课程中心：没有教学教务-课程课件-课程管理的删除权限"
           
#前台-课程中心-课程详情页（教学教务-课程课件-课程管理权限）             
def course_detail():  
    time.sleep(1)
    bh = driver.window_handles  
    try:
        #课程详情页
        driver.find_element("class name", "coursecenter-details-pic").click()#点击第一个课程进入课程详情页  
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        current_url = driver.current_url
        time.sleep(1)
        bh = driver.window_handles 
        #分享
        driver.find_element("class name", "bdshare_b")#显示分享
        time.sleep(1)
        #显示开始播放
        driver.find_element_by_link_text(u"开始播放").click()
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        driver.get(current_url)
        time.sleep(1)    
    except Exception:
        print traceback.format_exc()
        print u"课程详情页面：没有教学教务-课程课件-课程管理的读权限"
        
    time.sleep(1)   
    try:
        #显示编辑
        driver.find_elements_by_link_text(u"编辑")[1].click()
        time.sleep(1)
        driver.find_element("id", "J_complete").click()#保存
        #显示获取视频链接
        try:
            driver.find_element_by_link_text(u"获取视频链接").click()
            time.sleep(1)
            driver.find_element("class name", "dialog-button-container").click()#点击关闭  
        except:
            print'不是视频课程，没有获取视频链接！'
        time.sleep(2)
        #显示编辑三分屏章节
        try:
            driver.find_element_by_link_text(u"编辑三分屏章节").click()
            time.sleep(1)
            driver.get(current_url) 
        except:
            print'不是三分屏或双视频课程,没有编辑三分屏章节!'
        time.sleep(1)
        #显示发布相似课程
        driver.find_element_by_link_text(u"发布相似课程").click()
        time.sleep(1)
        driver.get(current_url)
        alert = driver.switch_to_alert()
        alert.accept() 
        time.sleep(1)
        #显示编辑课件
        driver.find_element_by_link_text(u"编辑课件").click()
        time.sleep(1)
        driver.find_elements("css selector", ".breadcrumb a")[-1].click()#返回课程详情页
        time.sleep(1)         
    except Exception:
        print traceback.format_exc()
        print u"课程详情页面：没有教学教务-课程课件-课程管理的编辑权限！" 
        
    time.sleep(3)   
    try:
        #删除
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击删除
        time.sleep(1)             
    except Exception:
        print traceback.format_exc()
        print u"课程详情页面：没有教学教务-课程课件-课程管理的删除权限"         

#前台-课程中心-课程详情页-答疑讨论区        
def course_detail_ansquetion():
    #答疑讨论区 
    time.sleep(1)       
    try:
        try:
            #回复提问
            driver.find_element_by_link_text(u"回复").click()                                                
        except:
            print '课程详情页的答疑区：还没有提问！'
            return
        time.sleep(1)
        driver.find_element("class name", "replay-textarea").send_keys("hello")
        time.sleep(1)
        driver.find_element("class name", "send-replay").click()#点击回复按钮  
        time.sleep(1)
        driver.find_element("class name", "delete-my").click()#删除刚才的回复
        #删除提问
        time.sleep(1)
        driver.find_element("class name", "delete-all").click()
        time.sleep(1)                                              
    except Exception:
        print traceback.format_exc()
        print u"课程详情页面：答疑讨论区相关操作权限应该对所有的管理员开放"             

#课程播放页面的答疑讨论区收到测试吧

#前台-课程中心导航（教学教务-课程课件-课程管理权限）
def course_center_relate():
    time.sleep(1)
    driver.find_element_by_link_text(u"课程中心").click()
    course_center()
    course_detail()
    time.sleep(1)
    driver.find_element_by_link_text(u"网校首页").click()#删除课程返回了ablesky首页了
    time.sleep(1) 
    driver.find_element_by_link_text(u"课程中心").click()#课程中心
    time.sleep(1)  
    bh = driver.window_handles 
    driver.find_element("class name", "coursecenter-details-pic").click()#点击第一个课程进入课程详情页,为后续答疑在准备  
    time.sleep(1)
    ah = driver.window_handles
    swithing_window(bh,ah)
    time.sleep(1)    
    course_detail_ansquetion()

#前台-报班中心(教学教务-报班中心-报班管理)
def class_center():
    time.sleep(1)   
    try:
        #报班中心
        driver.find_element_by_link_text(u"全部").click()
    except Exception:
        print traceback.format_exc()
        print u"报班中心：没有教学教务-报班中心-报班管理的读、删除权限"

    time.sleep(1)
    current_url = driver.current_url 
    try:
        #置顶显示、取消置顶
        driver.find_element_by_link_text(u"置顶显示").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"取消置顶").click()
        time.sleep(1)
        #班级管理
        driver.find_element_by_link_text(u"报班管理").click()
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)        
    except Exception:
        print traceback.format_exc()
        print u"报班中心：没有教学教务-报班中心-报班管理的编辑权限"
    
#前台-报班中心--班级详情页(教学教务-报班中心-报班管理)
def class_detail():
    time.sleep(2)
    bh = driver.window_handles 
    try:
        driver.find_element("css selector", ".course-title a").click()#点击第一个班级进入详情页
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        time.sleep(1)
        #分享
        driver.find_element("id", "bdshare")
        time.sleep(1)
        bh = driver.window_handles 
        current_url = driver.current_url
        time.sleep(1) 
        #查看报名情况
        driver.find_element("class name", "see-faceDetial").click()
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)
        #开始观看
        try:
            driver.find_element("class name", "see-now")
            time.sleep(1)
        except:
            print '此班级是面授班，没有开始观看按钮！'        
    except Exception:
        print traceback.format_exc()
        print u"班级详情页面：没有教学教务-报班中心-报班管理的读、删除权限"

    time.sleep(1)
    try:
        #编辑
        driver.find_element("class name", "detialEdit")
        time.sleep(1)
        #下架
        try:
            driver.find_element("class name", "upclass").click()
            driver.find_element("class name", "upclass").click()
        except:
            print '此班级是面授班或者是免费网络班，没有下架按钮！'       
    except Exception:
        print traceback.format_exc()
        print u"班级详情页面：没有教学教务-报班中心-报班管理的编辑权限"

#前台-报班中心--班级详情页-答疑区(网络班)
def class_detail_ansquestion():
    #答疑讨论区 
    time.sleep(2)
    try:
        try:
            #回复提问
            driver.find_element_by_link_text(u"回复").click()                                                
        except:
            print '网络班答疑讨论区还没有提问或者是面授班没有答疑区！'
            return
        time.sleep(1)
        driver.find_element("class name", "replay-textarea").send_keys("hello")
        time.sleep(1)
        driver.find_element("class name", "send-replay").click()#点击回复按钮  
        time.sleep(1)
        driver.find_element("class name", "delete-my").click()#删除刚才的回复
        #删除提问
        time.sleep(1)
        driver.find_element("class name", "delete-all").click()
        time.sleep(1)                                              
    except Exception:
        print traceback.format_exc()
        print u"班级详情页面：答疑讨论区相关操作权限应该对所有的管理员开放"   
 
#前台-报班中心导航
def class_center_relate():
    time.sleep(1)
    driver.find_element_by_link_text(u"报班中心").click()   
    class_center()
    class_detail()
    class_detail_ansquestion()

#前台-在线答疑
def online_ansquestion():
    time.sleep(1)
    driver.find_element_by_link_text(u"在线答疑").click() 
    course_detail_ansquetion()

#前台-直播课程
def live_course():
    time.sleep(1)   
    try:
        driver.find_element("class name", "see-course")#找到进入课程或者查看详情
    except Exception:
        print traceback.format_exc()
        print u"直播课程：没有教学教务-直播课程-发布直播课程的读权限"

    time.sleep(1)
    bh = driver.window_handles 
    current_url = driver.current_url
    try:
        #发布直播课程
        driver.find_element("css selector", ".post-btn a").click()
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        driver.get(current_url)
        time.sleep(1)
        #编辑
        driver.find_elements_by_link_text(u"编辑")[1].click()
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"直播课程：没有教学教务-直播课程-发布直播课程的编辑权限"
        
    try:
        #删除
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#先删除
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"直播课程：没有教学教务-直播课程-发布直播课程的删除权限"

#-直播课程距开课半个小时前
#发布相似课程 导入学员  查看学员 编辑 删除
#发布相似课程 查看学员 编辑 删除
#
#-直播课程距开课半小时内-结束
#发布相似课程 导入学员  查看学员
#发布相似课程 查看学员
#
#-直播课程第一节课结束，第二节课未结束前(手动测试)
#发布相似课程 上传课件  导入学员  查看学员  统计信息
#发布相似课程 上传课件 查看学员 统计信息
#前台-报名中-直播课程详情页
def live_course_detail_continue():
    time.sleep(2)
    driver.find_element("class name", "package-type").click()#点击报名中
    time.sleep(1)
    bh = driver.window_handles   
    try:
        driver.find_elements("class name", "see-course")[0].click()#进入课程
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
    except:
        print u"没有正在报名中的课程"

    time.sleep(1)        
    bh = driver.window_handles 
    current_url = driver.current_url 
    try:
        #查看学员
        try:
            #找到了删除按钮
            driver.find_elements("css selector", ".course-manage a")[4]
            time.sleep(1)
            driver.find_elements("css selector", ".course-manage a")[2].click()
            time.sleep(1)
        except:
            try:
                #找到了删除按钮
                driver.find_elements("css selector", ".course-manage a")[3]
                time.sleep(1)
                driver.find_elements("css selector", ".course-manage a")[1].click()
                time.sleep(1)
            except:
                try:
                    #找到了查看学员
                    driver.find_elements("css selector", ".course-manage a")[2].click()
                    time.sleep(1)
                except:
                    driver.find_elements("css selector", ".course-manage a")[1].click()                   
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        driver.get(current_url)
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"报名中-直播课程详情页：没有直播课程-发布直播课程的读权限"

    time.sleep(1)
    bh = driver.window_handles
    try:
        #发布相似课程
        driver.find_element("css selector", ".course-manage a").click()
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        driver.get(current_url) 
        time.sleep(1)
        #导入学员
        try:
            #找到了删除按钮
            driver.find_elements("css selector", ".course-manage a")[4]
            time.sleep(1)
            driver.find_elements("css selector", ".course-manage a")[1].click()
            time.sleep(1)
            driver.find_element("css selector", ".dialog-button-container button").click()
        except:
            try:
                #找到了删除按钮
                driver.find_elements("css selector", ".course-manage a")[3]
                time.sleep(1)
            except:
                try:
                    #找到了查看学员
                    driver.find_elements("css selector", ".course-manage a")[2]
                    time.sleep(1)
                    driver.find_elements("css selector", ".course-manage a")[1].click()
                    time.sleep(1)
                    driver.find_element("css selector", ".dialog-button-container button").click()
                except:
                   None 
        time.sleep(1)       
        #编辑
        try:
            driver.find_elements("css selector", ".course-manage a")[4]
            time.sleep(1)
            driver.find_elements("css selector", ".course-manage a")[3].click()
            time.sleep(1)
        except:
            try:
                 driver.find_elements("css selector", ".course-manage a")[3]
                 time.sleep(1)
                 driver.find_elements("css selector", ".course-manage a")[2].click()
                 time.sleep(1)
            except:
                None
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        driver.get(current_url) 
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"报名中-直播课程详情页：没有直播课程-发布直播课程的编辑权限"
    
    #删除    
    time.sleep(1)
    try:
        try:
            driver.find_elements("css selector", ".course-manage a")[4].click()
            time.sleep(1)
        except:
            try:
                driver.find_elements("css selector", ".course-manage a")[3].click()
                time.sleep(1)
            except:
                None           
    except Exception:
        print traceback.format_exc()
        print u"报名中-直播课程详情页：没有直播课程-发布直播课程的删除权限"
    #返回直播课程首页 
    time.sleep(1)
    driver.find_element_by_link_text(u"直播课程").click()
            
#前台-已结束-直播课程详情页
def live_course_detail_end():
    time.sleep(1)
    driver.find_element("class name", "face-type").click()#点击已结束
    time.sleep(1)
    bh = driver.window_handles   
    driver.find_element("class name", "see-course").click()#找到进入课程
    time.sleep(1)
    ah = driver.window_handles
    swithing_window(bh,ah)
    current_url = driver.current_url 
    try:
        #统计信息
        bh = driver.window_handles
        driver.find_elements("css selector", ".course-manage a")[2].click()
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)
        #课程结束
        driver.find_element_by_link_text(u"课程结束")
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"报名中-直播课程详情页：没有直播课程-发布直播课程的读权限"

    time.sleep(1)
    bh = driver.window_handles
    try:
        #发布相似课程
        driver.find_element("css selector", ".course-manage a").click()
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        driver.get(current_url) 
        time.sleep(2)
        #上传课件
        driver.find_elements("css selector", ".course-manage a")[1]
        time.sleep(1)
        #编辑
        driver.find_elements("css selector", ".course-manage a")[3].click()
        time.sleep(1)
        ah = driver.window_handles
        swithing_window(bh,ah)
        driver.get(current_url) 
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"报名中-直播课程详情页：没有直播课程-发布直播课程的编辑权限"
    time.sleep(1)
    try:
        #删除
        driver.find_elements("css selector", ".course-manage a")[4].click()
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#删除
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"报名中-直播课程详情页：没有直播课程-发布直播课程的删除权限"
        
#前台-直播课程导航(教学教务-直播课程-发布直播课程权限)
def live_course_relate():
    time.sleep(1)
    driver.find_element_by_link_text(u"直播课程").click()   
    live_course()
    live_course_detail_continue()
    live_course_detail_end()

#前台-特惠课程(教学教务-特惠课程-管理特惠课程权限)
def cheap_course():
    time.sleep(1)
    try:
        #显示我抢
        driver.find_element("css selector", ".buy a")
    except Exception:
        print traceback.format_exc()
        print u"特惠课程：没有特惠课程-管理特惠课程的读权限"
        
    time.sleep(1)
    try:
        #显示隐藏操作
        driver.execute_script("$('.exit-wrap').attr('style','display:block')")
        time.sleep(1)
        #下架
        driver.find_element_by_link_text(u"下架").click()
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1)      
        #置顶显示
        driver.execute_script("$('.exit-wrap').attr('style','display:block')")
        time.sleep(1)
        driver.find_element_by_link_text(u"置顶显示").click()
        time.sleep(1)                           
        #编辑
        current_url = driver.current_url
        driver.execute_script("$('.exit-wrap').attr('style','display:block')")
        time.sleep(1)
        driver.find_elements_by_link_text(u"编辑")[1].click()
        time.sleep(1)
        driver.find_elements("css selector", ".x-panel-btns-right button")[2].click()#点击保存
        time.sleep(1)
        driver.get(current_url) 
        time.sleep(1)       
    except Exception:
        print traceback.format_exc()
        print u"特惠课程：没有特惠课程-管理特惠课程的编辑权限"        

    time.sleep(1)
    try:
        #显示隐藏操作
        driver.execute_script("$('.exit-wrap').attr('style','display:block')")
        time.sleep(1)
        #删除
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击
        time.sleep(1) 
    except Exception:
        print traceback.format_exc()
        print u"特惠课程：没有特惠课程-管理特惠课程的删除权限" 

#特惠课程留言区
def cheap_course_ansquestion():
    time.sleep(2)
    try:
        try:
            #回复提问
            driver.find_element_by_link_text(u"回复").click()                                                
        except:
            print '特惠课程留言器区还没有留言！'
            return
        time.sleep(1)
        driver.find_element("class name", "replay-textarea").send_keys("hello")
        time.sleep(1)
        driver.find_element("class name", "send-replay").click()#点击回复按钮  
        time.sleep(1)
        driver.find_element("class name", "delete-my").click()#删除刚才的回复
        #删除提问
        time.sleep(1)
        driver.find_element("class name", "delete-all").click()
        time.sleep(1)                                              
    except Exception:
        print traceback.format_exc()
        print u"特惠课程留言区相关操作权限应该对所有的管理员开放"  
                                    
#前台-特惠课程(教学教务-特惠课程-管理特惠课程权限)
def cheap_course_relate():
    time.sleep(1)
    driver.find_element_by_link_text(u"特惠课程").click()
    time.sleep(1)
    cheap_course_ansquestion() #学员留言区
    cheap_course()    #特惠课程    
    
#前台-在线考试(教学教务-考试测评-考试系统权限)
def online_exam():
    time.sleep(1)
    bh = driver.window_handles   
    current_url = driver.current_url       
    try:
        #更多试卷
        driver.find_element("css selector", ".publish-exam a").click()
        ah = driver.window_handles
        swithing_window(bh,ah)
        time.sleep(1)
        driver.get(current_url)     
    except Exception:
        print traceback.format_exc()
        print u"在线考试：没有教学教务-考试测评-考试系统的读权限"   
        
    time.sleep(1)   
    try:
        #在线考试
        driver.execute_script("$('.coursecenter-module-hover').attr('style','display:block')")#显示隐藏操作
        #置顶显示、取消置顶
        time.sleep(1)
        driver.find_element_by_link_text(u"置顶显示").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"取消置顶").click()
        #显示编辑
        time.sleep(1)
        driver.find_element_by_link_text(u"编辑")
    except Exception:
        print traceback.format_exc()
        print u"在线考试：没有教学教务-考试测评-考试系统的编辑权限"
        
    time.sleep(1)   
    try:
        #显示删除
        time.sleep(1)
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(1)        
        driver.find_element("css selector", ".dialog-button-container button").click()#删除  
    except Exception:
        print traceback.format_exc()
        print u"在线考试：没有教学教务-考试测评-考试系统的删除权限"        

#前台-在线考试-试卷详情页面(教学教务-考试测评-考试系统权限)
def online_exam_detail():
    time.sleep(1)
    driver.find_element("css selector", ".onlineexam-module-txtes a").click()
    time.sleep(1)   
    current_url = driver.current_url       
    try:
        #显示试卷标题
        driver.find_element("class name", "onlineexam-introduce")  
    except Exception:
        print traceback.format_exc()
        print u"试卷详情：没有教学教务-考试测评-考试系统的读、编辑权限"   
        
    time.sleep(1)   
    try:
        #2个编辑按钮
        driver.find_element("class name", "start-test")
        time.sleep(1) 
        driver.find_element("class name", "onlineexam-btn") 
        time.sleep(1)   
    except Exception:
        print traceback.format_exc()
        print u"试卷详情：没有教学教务-考试测评-考试系统的编辑权限"  

#前台-在线考试(教学教务-考试测评-考试系统权限)
def online_exam_relate():
    time.sleep(1)
    driver.find_element_by_link_text(u"网校首页").click() 
    time.sleep(1)
    driver.find_element_by_link_text(u"在线考试").click()
    online_exam()
    online_exam_detail()
    
#前台-网校公告(适用于所有管理员) 
def school_notice():
    time.sleep(1)
    driver.find_element_by_link_text(u"网校公告").click() 
    an_content = "noticecontent"      
    try:
        #新建栏目
        driver.find_element("class name", "create-column").click()#点击新建栏目
        time.sleep(1)
        driver.find_element("class name", "columnName").send_keys("columnname")#栏目名称
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1)
        driver.find_elements("css selector", ".left-global-ul li")[-1].click()#选择刚才新建的栏目
        #新建公告
        time.sleep(1)
        driver.find_elements("css selector", ".content-right-title .notice-btn")[-1].click()#新建公告
        time.sleep(1)
        driver.find_element("class name", "titleName").send_keys('notice_title')#输入标题
        time.sleep(1)
        driver.execute_script("var element=window.document.getElementById('editNotice_ifr');\
        idocument=element.contentDocument;\
        element=idocument.getElementById('tinymce');\
        element.innerHTML='" + an_content + "'")#内容  
        time.sleep(1)
        driver.find_element("class name", "edit-column-sure").click()#确定
        #置顶显示
        time.sleep(1)
        driver.execute_script("$('.notice-content-bottom').attr('style','display:block')")#显示隐藏操作
        time.sleep(1)
        driver.find_element("class name", "subNotice-top").click()
        time.sleep(1)        
        #编辑公告
        driver.find_elements("css selector", ".notice-content-bottom .notice-btn")[1].click()
        time.sleep(1)
        driver.find_element("class name", "edit-column-sure").click()#确定        
        #删除公告
        time.sleep(1)
        driver.execute_script("$('.notice-content-bottom').attr('style','display:block')")#显示隐藏操作
        time.sleep(1)
        driver.find_element("class name", "notice-del").click()#点击删除公告
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1)        
        #编辑栏目
        driver.find_element("class name", "edit-column").click()#点击编辑栏目
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1)
        #隐藏栏目
        driver.find_element("class name", "notice-hide").click()
        time.sleep(1)        
        #删除栏目   
        driver.find_element("class name", "column-del").click()#点击确定
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1)    
    except Exception:
        print traceback.format_exc()
        print u"所有管理员都应该有网校公告相关权限"   

#前台-名师团队(教学教务-名师团队-名师管理)
def teacher_team():
    time.sleep(1)
    driver.find_element_by_link_text(u"名师团队").click()           
    time.sleep(1)   
    current_url = driver.current_url   
    time.sleep(1)    
    try:
        #置顶显示
        driver.find_element_by_link_text(u"置顶显示").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"取消置顶").click()
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)
        #编辑
        driver.find_elements_by_link_text(u"编辑")[1].click()
        time.sleep(1)
        driver.find_element("css selector", ".submit-wrap a").click()#发布
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"名师团队：没有教学教务-名师团队-名师管理的编辑权限" 

#前台-网校成员(教学教务-网校成员-成员管理)
def school_members():
    time.sleep(1)
    driver.find_element_by_link_text(u"网校成员").click()
    time.sleep(1)   
    current_url = driver.current_url       
    try:
        #管理机构成员
        driver.find_element("css selector", ".weizhi-right a").click()#点击管理机构成员
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"名师团队：没有教学教务-网校成员-成员管理的读、删除权限" 
                
    time.sleep(1)   
    current_url = driver.current_url       
    try:
        #置顶显示
        driver.find_element_by_link_text(u"置顶显示").click()
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)
        #取消置顶
        driver.find_element_by_link_text(u"取消置顶").click()
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"名师团队：没有教学教务-网校成员-成员管理的编辑权限"   

#前台-关于我们(适用于所有管理员) 
def about_us():
    time.sleep(1)
    driver.find_element_by_link_text(u"关于我们").click() 
    an_content = "noticecontent"      
    try:
        #新建栏目
        driver.find_element("css selector", ".column-title a").click()#点击新建栏目
        time.sleep(1)
        driver.find_element("css selector", "#J_inputWordCount input").send_keys("columnname")#栏目标题
        time.sleep(1)
        driver.execute_script("var element=window.document.getElementById('editAboutUs_ifr');\
        idocument=element.contentDocument;\
        element=idocument.getElementById('tinymce');\
        element.innerHTML='" + an_content + "'")#内容  
        time.sleep(1)
        driver.find_element("class name", "edit-column-sure").click()#确定
        time.sleep(1)      
        #编辑
        driver.find_elements("css selector", ".notice-content-title .notice-btn")[2].click()
        time.sleep(1)
        driver.find_element("class name", "edit-column-sure").click()#确定  
        time.sleep(1) 
        #隐藏
        driver.find_element("class name", "column-hide").click()
        time.sleep(1)       
        #删除公告
        driver.find_element("class name", "column-del").click()
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1)        
    except Exception:
        print traceback.format_exc()
        print u"所有管理员都应该有关于我们相关权限"
           
#前台-帮助中心(适用于所有管理员) 
def help_center():
    time.sleep(1)
    driver.find_element_by_link_text(u"帮助中心").click() 
    an_content = "noticecontent"      
    try:
        #管理栏目
        driver.find_element("css selector", ".column-title a").click()#点击管理栏目
        time.sleep(1)
        #新建栏目
        driver.find_element("css selector", ".column-title a").click()#点击新建栏目
        time.sleep(1)
        driver.find_element("class name", "editColumnInput").send_keys("columnname")#栏目名称
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1)   
        #编辑栏目(刚创建的)
        driver.find_elements("css selector", ".column-edit-main .edit-column")[-1].click()
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1) 
        #隐藏栏目
        driver.find_elements("css selector", ".column-edit-main .hide-column")[-1].click()
        time.sleep(1)
        #添加子栏目
        driver.find_elements("css selector", ".column-edit-main a")[-1].click()
        time.sleep(1)
        driver.find_element("css selector", "#J_inputWordCount input").send_keys("columnname")#栏目标题
        time.sleep(1)
        driver.execute_script("var element=window.document.getElementById('editHelpCenter_ifr');\
        idocument=element.contentDocument;\
        element=idocument.getElementById('tinymce');\
        element.innerHTML='" + an_content + "'")#内容  
        time.sleep(1)
        driver.find_element("class name", "edit-column-sure").click()#确定
        time.sleep(1)
        #展开显示出子栏目
        driver.find_elements("class name", "helpcenter-column-title")[-1].click()
        time.sleep(1)         
        #隐藏子栏目
        driver.find_element("css selector", ".column-main-detail .hide-column").click()
        time.sleep(1)
        #编辑子栏目
        driver.find_element("css selector", ".column-main-detail a").click()
        time.sleep(1)
        driver.find_element("class name", "edit-column-sure").click()#点击确定
        time.sleep(1) 
        #删除子栏目
        driver.find_elements("class name", "helpcenter-column-title")[-1].click()#展开显示出子栏目
        time.sleep(1) 
        driver.find_element("css selector", ".column-main-detail .del-column").click()
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1)      
        #删除栏目
        driver.find_elements("css selector", ".column-edit-main .del-column")[-1].click()
        time.sleep(1)
        driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
        time.sleep(1)         
    except Exception:
        print traceback.format_exc()
        print u"所有管理员都应该有帮助中心相关权限" 

def admin_athority_check():
    
	global base_url
	global cfg 
	global driver
	base_url = "http://www.gamma.ablesky.com/"
	cfg_file = 'config.ini'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(cfg_file)
	user_name = "stu_gy000"
	user_psw = "gy0411"    

	chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	#driver = webdriver.Ie()

	login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
	driver.get("%smyOffice.do" %(base_url))

	# ##(fore_stage())
	# driver.find_element_by_link_text(u"网校首页").click()
	# time.sleep(1)
	# firstpage()#首页
	# course_center_relate()#课程中心
	# class_center_relate()#报班中心 
	# online_ansquestion()#在线答疑
	# live_course_relate()#直播课程
	# cheap_course_relate()#特惠课程
	# online_exam_relate()#在线考试
	# school_notice()#网校公告
	# teacher_team()#名师团队
	# school_members()#网校成员
	# # about_us()#关于我们
	# # help_center()#帮助中心
        
	driver.quit()
    
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	admin_athority_check()
    