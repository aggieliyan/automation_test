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
	org_name = "salesdemo"
	try:
		user_management.modify_pagefoot(cfg, driver, base_url, org_name) 
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
        driver.find_elements("css selector",".dialog-button-container button")[1].click()#先不删除呀   
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
            print'不是三分屏或双视频课程,没有编辑三分屏章节'
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
        driver.find_elements("css selector", ".dialog-button-container button")[1].click()#点击取消删除
        time.sleep(1)
    except Exception:
        print traceback.format_exc()
        print u"课程详情页面：没有教学教务-课程课件-课程管理的删除权限"         

#前台-课程中心-课程详情页-答疑讨论区        
def course_detail_ansquetion():
    #答疑讨论区 
    time.sleep(3)
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
    time.sleep(3)
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
        driver.find_elements("css selector", ".dialog-button-container button")[1].click()#先取消删除以后改过来
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
        driver.find_elements("css selector", ".dialog-button-container button")[1].click()#先取消删除以后改过来
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
        driver.find_elements("css selector", ".dialog-button-container button")[1].click()#先点击取消
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
        driver.find_elements("css selector", ".dialog-button-container button")[-1].click()#先取消删除以后改过来  
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
    try:
        #置顶显示
        driver.find_element_by_link_text(u"置顶显示").click()
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

        
#后台首页-教学互动		    
def teaching():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-我的私信、网校答疑
	menu_dic = {u"我的私信":teaching_letter, 
			       u"网校答疑":teaching_ansquestion,}
	menu_title = u"后台首页"
	check_menu(menu_title, menu_dic)
			
#后台首页-授权管理
def authmanage():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-授权购买记录、已使用授权 在线购买授权
	menu_dic = {u"授权购买记录":authmanage_buyRecord, 
			       u"已使用授权":authmanage_usegrant,
			       u"在线购买授权":authmanage_buygrant}
	menu_title = u"后台首页"
	check_menu(menu_title, menu_dic)   

#后台首页-课程合作代理
def courseagent():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-管理我授权的代理、管理我申请的代理
	menu_dic = {u"管理我授权的代理":agent_grant, 
			       u"管理我申请的代理":agent_apply}
	menu_title = u"后台首页"
	check_menu(menu_title, menu_dic)
		
#后台首页-学习卡
def learnigcard():
	driver.get("%smyOffice.do" %(base_url))
	#学习卡-管理卡组、卡使用记录
	menu_dic = {u"管理卡组":learnigcard_group, 
					       u"卡使用记录":learnigcard_record}
	menu_title = u"后台首页"
	check_menu(menu_title, menu_dic)

#后台首页-统计管理
def countmanage():
	driver.get("%smyOffice.do" %(base_url))
	#统计管理-外链视频流量统计  浏览量统计 新增学员量统计
	menu_dic = {u"外链视频流量统计":countmanage_outvideo, 
			       u"浏览量统计":countmanage_views,
			       u"新增学员量统计":countmanage_newstudent,}
	menu_title = u"后台首页"
	check_menu(menu_title, menu_dic)
				     
#系统设置-管理员/客服
def manageorservice():
	driver.get("%smyOffice.do" %(base_url))
	#管理员/客服-网校管理员  网校客服
	menu_dic = {u"网校管理员":manageorservice_manage, 
	               u"网校客服":manageorservice_service,}
	menu_title = u"系统设置"
	check_menu(menu_title, menu_dic)

#系统设置-页面建设
def pagecreate():
	driver.get("%smyOffice.do" %(base_url))
	#页面建设-首页高级编辑  自定义页面  网络图片库  自定义登录图片
	menu_dic = {u"首页高级编辑":pagecreate_edit, 
	               u"自定义页面":pagecreate_selfpage,
	               u"网络图片库":pagecreate_netpic,
	               u"自定义登录图片":pagecreate_selflogin,}
	menu_title = u"系统设置"
	check_menu(menu_title, menu_dic)	
            
#学员/员工-网校学员
def stuoremp():
	driver.get("%smyOffice.do" %(base_url))
	#统计管理-外链视频流量统计  浏览量统计 新增学员量统计
	menu_dic = {u"学员管理":stuoremp_stumanage, 
	                u"员工管理":stuoremp_empmanage,
                    u"学员类目":stuoremp_stucate,
	                #u"员工申请 ":stuoremp_empapply, #手动测试吧
	                u"学员学习记录":stuoremp_stulearnrecord,}
	menu_title = u"学员/员工"
	check_menu(menu_title, menu_dic)
	
#后台首页-教学互动-我的私信
def teaching_letter():
	time.sleep(1)
	try:
		driver.find_element("class name", "x-tab-strip-text").click()
	except Exception:
		print traceback.format_exc()
		print u"没有我的私信的读权限"
		return
	time.sleep(2)	
	try:
        #收件箱发送私信
		driver.find_element("class name", "sendEmialBtn").click()
		time.sleep(1)
		driver.find_element("name", "username").send_keys("success")
		time.sleep(1)
		driver.find_element("name", "subject").send_keys(u"标题")
		time.sleep(1)
		driver.find_element("name", "msg").send_keys(u"内容")
		time.sleep(1)
		driver.find_element("css selector", ".x-panel-btn-td button").click()
		#发件箱发送私信
		time.sleep(1)
		driver.find_element_by_link_text(u"发件箱").click()
		time.sleep(1)
		driver.execute_script("$('#composeMsgTitle').click()")
		#driver.find_element("id", "composeMsgTitle").click()#点击写信  
		time.sleep(1)
		driver.find_element("name", "username").send_keys("gy0411")
		time.sleep(1)
		driver.find_element("name", "subject").send_keys(u"标题")
		time.sleep(1)
		driver.find_element("name", "msg").send_keys(u"内容")
		time.sleep(1)
		driver.find_element("css selector", ".x-panel-btn-td button").click()
		time.sleep(1)
		driver.find_element("class name", "x-tab-strip-text").click()#点击收件箱            
	except Exception, e:
		print traceback.format_exc()
		print u"没有我的私信的编辑权限"
        
	time.sleep(2)		
	try:
        #收件箱删除私信
		driver.find_element("class name", "deleteS").click()
		time.sleep(2)
		driver.find_elements("css selector", ".x-panel-btns-center .x-btn-center button")[1].click()
		time.sleep(1)
        #发件箱删除私信
		driver.find_element_by_link_text(u"发件箱").click()
		time.sleep(1)
		driver.find_element("css selector", ".priceAndFeedBGrid .deleteS").click()
		time.sleep(1)
		driver.find_elements("css selector", ".x-window-br .x-btn-text")[1].click()
	except Exception:
		print traceback.format_exc()
		print u"没有我的私信的删除权限"
				 
#后台首页-教学互动-网校答疑    
def teaching_ansquestion():
	time.sleep(1)
	try:
		driver.find_elements("class name", "x-form-arrow-trigger")[0].click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item")[0].click()
	except Exception, e:
		print traceback.format_exc()
		print u"没有网校答疑的读权限"
		return	
	time.sleep(2)	   
	try:
	    driver.find_element_by_link_text(u"回复").click()#没有具体回复
	    time.sleep(1)
	    driver.find_element_by_link_text(u"取消").click() 
	    time.sleep(2)	
	    driver.find_element_by_link_text(u"编辑").click()
	    time.sleep(1)    
	    driver.find_element_by_link_text(u"保存").click() 	
	except Exception:
		print traceback.format_exc()
		print u"没有我的私信的编辑权限"  

	time.sleep(1)		 
	try:
	    driver.find_element_by_link_text(u"删除").click()
	except Exception, e:
		print traceback.format_exc()
		print u"没有我的私信的删除权限"  
		
#后台首页-授权管理-授权购买记录	
def authmanage_buyRecord():
	time.sleep(1)
	try:
	    driver.find_element("class name", "cc-arrow").click()#下拉选择
	    time.sleep(1)
	    driver.find_elements("class name", "cc-item")[1].click()
	    time.sleep(2)	
	    driver.find_elements("class name", "j-gldp-target")[0].click()#日期筛选
	    time.sleep(1)    
	    driver.find_element("class name", "outday").click()
	    time.sleep(1)    
	    driver.find_elements("class name", "j-gldp-target")[1].click()
	    time.sleep(1)    
	    driver.find_elements("class name", "outday")[-1].click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"查询").click()
	    time.sleep(2)	    
	    driver.find_element_by_link_text(u"购买授权").click()   
	except Exception, e:
	    print traceback.format_exc()
	    print u"没有授权购买记录的读、编辑、删除权限"
	    
#后台首页-授权管理-已使用授权		
def authmanage_usegrant():
	time.sleep(1)
	try:
	    driver.find_element("name", "authType").click()#下拉选择扣除方式
	    time.sleep(1)
	    driver.find_elements("css selector", "select option")[1].click()
	    time.sleep(2)
	    driver.find_element("name", "authStatus").click()#下拉选择状态
	    time.sleep(1)
	    driver.find_elements("css selector", "select option")[-1].click()
	    time.sleep(2)
	    driver.find_elements("class name", "x-form-date-trigger")[0].click()#日期筛选
	    time.sleep(1)
	    driver.find_element("class name", "x-date-active").click()
	    time.sleep(2)	
	    driver.find_elements("class name", "x-form-date-trigger")[1].click()
	    time.sleep(1)    
	    driver.find_elements("class name", "x-date-active")[-1].click()
	    time.sleep(2)
	    driver.find_element("class name", "x-btn-text").click()#点击过滤
	    time.sleep(1)	        
	except Exception:
		print traceback.format_exc()
		print u"没有已使用授权的读、编辑、删除权限"
		
#后台首页-授权管理-在线购买授权	
def authmanage_buygrant():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"在线购买授权").click()   
	except Exception:
		print traceback.format_exc()
		print u"没有在线购买授权的读、删除权限"
		return
#	user_name = 'none'
#	bnum = 1
	current_url = driver.current_url
	time.sleep(1) 
	try:
	    driver.find_element("class name", "authorizeNum").clear()
	    time.sleep(1)
	    driver.find_element("class name", "authorizeNum").send_keys('1')
	    time.sleep(1)		
	    driver.find_element_by_link_text(u"确认购买").click()   
#		student_management.buy_open_num(cfg, driver, base_url, user_name, bnum)
	except Exception:
		print traceback.format_exc()
		print u"没有在线购买授权的编辑权限"
	time.sleep(2)
	driver.get(current_url)

#后台首页-课程合作代理-管理我申请的代理	
def agent_apply():
	courseagent_apply()
	paperagent_apply()

#后台首页-课程合作代理-管理我授权的代理-课程代理
def courseagent_grant():
	time.sleep(1)
	current_url = driver.current_url
	time.sleep(2)
	try:
	    driver.find_element("class name", "agency-navInfo").click()#接受or拒绝
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看课程").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看记录").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"订单管理").click()
 	    time.sleep(1)
 	    bh = driver.window_handles 	    
	    driver.find_element_by_link_text(u"订单详情").click()
 	    time.sleep(2)
 	    ah = driver.window_handles
 	    swithing_window(bh,ah)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的读、删除权限"
		return

	time.sleep(2) 
	try:
		driver.find_element("class name", "agency-province").click()#选择代理区域
		time.sleep(1)
		driver.find_elements("css selector", ".agency-province option")[2].click()
		time.sleep(1)
		driver.find_element("class name", "agency-city").click()#选择代理区域
		time.sleep(1)
		driver.find_elements("css selector", ".agency-city option")[2].click()
		time.sleep(1)
		driver.find_element("class name", "agency-rank").click()#选择代理级别
		time.sleep(1)
		driver.find_elements("css selector", ".agency-rank option")[2].click()
		time.sleep(1)    
		driver.find_element_by_link_text(u"新建订单").click()#新建订单  
		time.sleep(3)		
		driver.find_elements("name", "categoryItems")[-1].click()
		time.sleep(2)
		driver.find_element("id", "J_acceptProtocol").click()
		time.sleep(2)
		driver.find_element("class name", "x-btn-text").click()#点击发送订单
		time.sleep(2)
		driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
		time.sleep(2)		
#		driver.get(current_url)
#		time.sleep(2)
#		driver.find_element_by_link_text(u"订单管理").click()  
#		time.sleep(1)
		bh = driver.window_handles
		driver.find_element_by_link_text(u"修改订单").click()#进行修改订单
		time.sleep(2)
		ah = driver.window_handles
		swithing_window(bh,ah)
		time.sleep(2)
		driver.find_element("id", "J_acceptProtocol").click()
		time.sleep(1)
		driver.find_element("class name", "x-btn-text").click()
		time.sleep(1)
		driver.find_element("css selector", ".dialog-button-container button").click()
#		driver.get(current_url)
#		driver.find_element_by_link_text(u"订单管理").click() 
		time.sleep(2)
		driver.find_element_by_link_text(u"取消订单").click()
		time.sleep(1)
		driver.find_element("css selector", ".dialog-button-container button").click()
		time.sleep(1)				  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的编辑权限"
	time.sleep(2)
	driver.get(current_url)		
#后台首页-课程合作代理-管理我申请的代理-课程代理		
def courseagent_apply():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"管理我申请的代理").click()
	    current_url = driver.current_url
	    time.sleep(2)
	    driver.find_element_by_link_text(u"管理课程").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看记录").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"订单管理").click()
 	    time.sleep(1)
	    driver.find_element_by_link_text(u"订单详情").click()
 	    time.sleep(1)
 	    bh = driver.window_handles 	    
	    driver.find_element_by_link_text(u"订单详情").click()
 	    time.sleep(2)
 	    ah = driver.window_handles
	    swithing_window(bh,ah)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我申请的代理的课程代理的读、编辑权限"
		return

	time.sleep(2)
	rand_name = str(random.randint(1000, 9999))
	title = u"agencycourse"+rand_name 
	try:
        #管理课程-编辑课程
		new_course_management.release_agency_course(cfg, driver, base_url, course_title=title)
		driver.get(current_url)
		time.sleep(2)
        #订单管理-立即支付
		driver.find_element_by_link_text(u"订单管理").click()
		bh = driver.window_handles 	  
		time.sleep(1)
		try:
		    driver.find_element_by_link_text(u"立即支付").click()
		except:
			print "没有立即支付的课程订单"
		ah = driver.window_handles
		swithing_window(bh,ah)
		time.sleep(1)
		driver.get(current_url)					  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的编辑权限"
	time.sleep(2)
	
#后台首页-课程合作代理-管理我授权的代理-考试代理
def paperagent_grant():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"考试代理").click()
	    current_url = driver.current_url
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看试卷").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看记录").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"订单管理").click()
 	    time.sleep(1)
 	    bh = driver.window_handles 	    
	    driver.find_element_by_link_text(u"订单详情").click()
 	    time.sleep(2)
 	    ah = driver.window_handles
	    swithing_window(bh,ah)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的考试代理的读、删除权限"
		return

	time.sleep(2) 
	try:
		driver.find_element("class name", "agency-province").click()#选择代理区域
		time.sleep(1)
		driver.find_elements("css selector", ".agency-province option")[2].click()
		time.sleep(1)
		driver.find_element("class name", "agency-city").click()#选择代理区域
		time.sleep(1)
		driver.find_elements("css selector", ".agency-city option")[2].click()
		time.sleep(1)
		driver.find_element("class name", "agency-rank").click()#选择代理级别
		time.sleep(1)
		driver.find_elements("css selector", ".agency-rank option")[2].click()
		time.sleep(1)    
		driver.find_element_by_link_text(u"新建订单").click()#新建订单 
		time.sleep(2)  
		driver.find_element_by_link_text(u"全选试卷").click()
		time.sleep(2)
		driver.find_element("id", "readed_check").click()
		time.sleep(2)
		driver.find_element("id", "submit_btn").click()
		time.sleep(2)
		driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
		time.sleep(2)		
#		driver.get(current_url)
#		time.sleep(2)
#		driver.find_element_by_link_text(u"订单管理").click()  
#		time.sleep(1)
		bh = driver.window_handles
		driver.find_element_by_link_text(u"修改订单").click()#进行修改订单
		time.sleep(2)
		ah = driver.window_handles
		swithing_window(bh,ah)
		time.sleep(2)
		driver.find_element("id", "readed_check").click()
		time.sleep(1)
		driver.find_element("id", "submit_btn").click()
		time.sleep(1)
		driver.find_element("css selector", ".dialog-button-container button").click()
#		driver.get(current_url)
#		driver.find_element_by_link_text(u"订单管理").click() 
		time.sleep(2)
		driver.find_element_by_link_text(u"取消订单").click()
		time.sleep(1)
		driver.find_element("css selector", ".dialog-button-container button").click()
		time.sleep(1)			  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的考试代理的编辑权限"
	driver.get(current_url)	
	time.sleep(2)
#后台首页-课程合作代理-管理我申请的代理-考试代理
def paperagent_apply():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"考试代理").click()
	    current_url = driver.current_url
	    time.sleep(2)
	    driver.find_element_by_link_text(u"管理试卷").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看记录").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"订单管理").click()
 	    time.sleep(1)
	    driver.find_element_by_link_text(u"订单详情").click()
 	    time.sleep(1)
 	    bh = driver.window_handles 	    
	    driver.find_element_by_link_text(u"订单详情").click()
 	    time.sleep(2)
 	    ah = driver.window_handles
	    swithing_window(bh,ah)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我申请的代理的考试代理的读、编辑权限"
		return

	time.sleep(2)
	rand_name = str(random.randint(1000, 9999))
	title = u"agencycourse"+rand_name 
	try:
        #管理试卷
	    driver.find_element_by_link_text(u"管理试卷").click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"编辑").click()#编辑试卷
	    ah = driver.window_handles
	    swithing_window(bh,ah)
	    time.sleep(1)
	    driver.find_element("id", "paper_name_input").clear()
	    time.sleep(1)
	    driver.find_element("id", "paper_name_input").send_keys(title)
	    time.sleep(1)
	    driver.find_element("id", "save_btn").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1) 	    
	    driver.find_element_by_link_text(u"订单管理").click()
 	    bh = driver.window_handles  
	    time.sleep(1)
	    try:  
	        driver.find_element_by_link_text(u"立即支付").click()
	    except:
	    	print "没有立即支付的考试订单"
	    ah = driver.window_handles
	    swithing_window(bh,ah)
	    time.sleep(1)				  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的编辑权限"
	driver.get(current_url)	
	time.sleep(2)

#后台首页-课程合作代理-管理我授权的代理    
def agent_grant():
    time.sleep(1)
    courseagent_grant()
    paperagent_grant()
    
#后台首页-学习卡-管理卡组
def learnigcard_group():
	time.sleep(1)
	current_url = driver.current_url	
	try:
		driver.find_element_by_link_text(u"浏览卡").click()
		time.sleep(1)
		driver.get(current_url)
		#查看卡组页面-浏览卡
		time.sleep(1)
		driver.find_element("class name","textaligncenter").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"浏览卡").click()
		time.sleep(1)
		#点击该卡组的Excel文件
		time.sleep(1)
		driver.get(current_url)       	
	except Exception:
		print traceback.format_exc()
		print u"没有管理卡组的读权限"
		return
		
	time.sleep(2)	   
	try: 
        #购买试听卡
	    driver.find_element_by_link_text(u"购买试听卡").click()
		#card_management.buy_listen_card(cfg,driver,base_url)#购买试听卡
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1)
        #查看卡组页面-编辑卡组
	    time.sleep(1)
	    driver.find_element("class name","textaligncenter").click()
	    time.sleep(1)
	    driver.find_element("class name","x-btn-center").click()#点击编辑卡组
	    time.sleep(1)
	    driver.find_elements("class name","x-btn-center")[1].click()#点击保存卡组
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1)
        #添加卡组
	    org_name = "stu_gy"
	    rand_name = str(random.randint(1000, 9999))
	    group_name = u"prepaidcard"+rand_name
	    group_price = 100
	    card_management.add_prepaid_cardgroup(cfg, driver, base_url, org_name, group_name, group_price)#添加卡组
	    card_prifix = "auto" + chr(random.randint(97, 122)) + \
		chr(random.randint(97, 122)) + chr(random.randint(97, 122))
	    card_management.add_card(cfg, driver, base_url, org_name,card_prifix)#添加卡
		#driver.find_element_by_link_text(u"添加卡组").click()	
		#time.sleep(1)
		#driver.get(current_url)
		#time.sleep(1)
		#driver.find_element_by_link_text(u"添加卡").click()	
		#time.sleep(1)
		#driver.get(current_url)
        #浏览卡
	    time.sleep(1)
	    driver.find_element_by_link_text(u"浏览卡").click()		
	    time.sleep(1)
	    driver.find_elements("css selector", "input[type=checkbox]")[1].click()#勾选第一个卡
	    time.sleep(1)
        #禁用
	    driver.find_element("class name", "x-form-arrow-trigger").click()#禁用
	    time.sleep(1)
	    driver.find_elements("class name", "x-combo-list-item")[1].click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"应用").click()#应用
	    time.sleep(2)
        #启用
	    driver.find_elements("css selector", "input[type=checkbox]")[1].click()#勾选第一卡
	    time.sleep(1)
	    driver.find_element("class name", "x-form-arrow-trigger").click()#启用
	    time.sleep(1)	    
	    driver.find_elements("class name", "x-combo-list-item")[2].click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"应用").click()#应用
	    time.sleep(1)
        #添加卡
	    driver.find_elements("class name", "colorwhite")[1].click()#点击向该卡组添加卡
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
        #编辑卡组	    
	    driver.find_element_by_link_text(u"编辑卡组").click()#编辑卡组
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#保存修改
	    time.sleep(1)					  
	except Exception, e:
		print traceback.format_exc()
		print u"没有管理卡组的编辑权限"
		
	time.sleep(2)	   
	try:
        #浏览卡页面-删除卡
	    driver.find_element_by_link_text(u"浏览卡").click()		
	    time.sleep(1)
	    driver.find_elements("css selector", "input[type=checkbox]")[1].click()#勾选第一个卡
	    time.sleep(1)
	    driver.find_element("class name", "x-form-arrow-trigger").click()#删除
	    time.sleep(1)
	    driver.find_elements("class name", "x-combo-list-item")[0].click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"应用").click()#应用
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
        #删除卡组
	    driver.find_element_by_link_text(u"删除卡组").click()
	    time.sleep(1)
	    driver.find_elements("css selector", ".x-panel-bwrap .x-btn-text")[5].click()
	    time.sleep(1)
	except Exception, e:
		print traceback.format_exc()
		print u"没有管理卡组的删除权限"
#后台首页-学习卡-卡使用记录	
def learnigcard_record():
	time.sleep(1)
	try:
	    driver.find_element("class name", "x-form-arrow-trigger").click()#下拉选择充卡类型
	    time.sleep(2)
	    driver.find_elements("class name", "x-combo-list-item")[-1].click()
	    time.sleep(1)
	    driver.find_elements("class name", "x-form-date-trigger")[0].click()#日期筛选
	    time.sleep(1)
	    driver.find_element("class name", "x-date-active").click()
	    time.sleep(2)	
	    driver.find_elements("class name", "x-form-date-trigger")[1].click()
	    time.sleep(1)    
	    driver.find_elements("class name", "x-date-active")[-1].click()
	    time.sleep(2)
	    driver.find_element("class name", "x-btn-text").click()#点击过滤
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有卡使用记录的读、编辑、删除权限"

#后台首页-统计管理-外链视频流量统计
def countmanage_outvideo():
	time.sleep(1)
	try:
	    driver.find_element("css selector", "div[data-type=cur-year]").click()#点击本年
	    time.sleep(1)
	    driver.find_element("class name", "x-form-arrow-trigger").click()#按日显示
	    time.sleep(2)	
	    driver.find_elements("class name", "x-combo-list-item")[0].click()
	    time.sleep(1)
	    driver.find_element("id", "J_exportExcel").click()#点击导入excel列表
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有外链视频流量统计的读、编辑、删除权限"
		
#后台首页-统计管理-浏览量统计
def countmanage_views():
	time.sleep(1)
	try:
	    driver.find_element("css selector", "span[data-type=recent3month]").click()#点击最近3个月
	    time.sleep(1)
	    driver.find_element("class name", "cc-arrow").click()#按日查询
	    time.sleep(2)	
	    driver.find_elements("class name", "cc-item")[0].click()
	    time.sleep(1)
	    driver.find_element("class name", "exportExecl").click()
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有浏览量的读、编辑、删除权限"
		
#后台首页-统计管理-新增学员量统计	
def countmanage_newstudent():
	time.sleep(1)
	try:
	    driver.find_element("css selector", "span[data-type=last-month]").click()#点击上个月
	    time.sleep(1)
	    driver.find_element("class name", "cc-arrow").click()#按日查询
	    time.sleep(2)	
	    driver.find_elements("class name", "cc-item")[0].click()
	    time.sleep(1)
	    driver.find_element("class name", "exportExecl").click()
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有新增学员量统计的读、编辑、删除权限"		
 
#系统设置-管理员/客服-网校管理员
def manageorservice_manage():
	time.sleep(1)
	current_url = driver.current_url
	try:
	    driver.find_element("class name","colorGray")#找到编辑管理员的置灰span
	except Exception:
		print traceback.format_exc()
		print u"没有管理员的读权限"

	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"添加管理员").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1)
	    driver.find_element_by_link_text(u"编辑管理员").click()
	    time.sleep(1)
	    driver.get(current_url)	    	    
	except Exception:
		print traceback.format_exc()
		print u"没有管理员的编辑权限"
		
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"删除管理员").click()
	    time.sleep(1)
	    driver.find_elements("class name","x-btn-text")[1].click()#先取消删除   	    
	except Exception:
		print traceback.format_exc()
		print u"没有管理员的删除权限"
		
#批量创建读权限管理员
def create_manage_read():
	user_file = open(r"C:/register_admin_user_list_read.txt", 'w')
	i = 1
	pre_name='relog_'
	for item in driver.find_elements("class name","categoryAuthority-look-active"):
		admin_username = create_manage_fillmanage(pre_name, i, user_file)
		time.sleep(1)
		if i != 1:
			driver.execute_script("$('.onOff').click()")
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none')")
		time.sleep(1)
		driver.find_element_by_link_text(u"取消").click()
		time.sleep(1)
		user_file.writelines(admin_username + "\n")
		i = i + 1
		time.sleep(5)
		driver.find_element_by_link_text(u"添加管理员").click() 
		time.sleep(3)
	print '读权限管理员个数:' + str(i)
	user_file.close()

#批量创建编辑权限管理员
def create_manage_edit():
	i = 1
	pre_name = 'edlog_'
	for item in driver.find_elements("class name", "categoryAuthority-add"):
		user_file = open(r"C:/register_admin_user_list_edit.txt", 'w')
		admin_username = create_manage_fillmanage( pre_name, i, user_file)
		if i != 1:
			driver.execute_script("$('.onOff').click()")
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-add-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-add').eq(" + str(i-1) + ").attr('style','display:none')")
		time.sleep(1)
		driver.find_element_by_link_text(u"取消").click()
		time.sleep(1)
		user_file.writelines(admin_username + "\n")
		i = i + 1
		time.sleep(1)
		driver.find_element_by_link_text(u"添加管理员").click() 
		time.sleep(1)
	print '编辑权限管理员个数:' + str(i)
	user_file.close()

#批量创建删除权限管理员
def create_manage_delete():
	user_file = open(r"C:/register_admin_user_list_delete.txt", 'w')
	i = 1
	pre_name = 'delog_'
	for item in driver.find_elements("class name", "categoryAuthority-delete"):
		admin_username = create_manage_fillmanage(pre_name, i, user_file)
		if i != 1:
			driver.execute_script("$('.onOff').click()")
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-delete-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-delete').eq(" + str(i-1) + ").attr('style','display:none')")
		time.sleep(1)
		driver.find_element_by_link_text(u"取消").click()
		time.sleep(1)
		user_file.writelines(admin_username + "\n")
		i = i + 1
		time.sleep(1)
		driver.find_element_by_link_text(u"添加管理员").click() 
		time.sleep(1)
	print '删除权限管理员个数' + str(i)
	user_file.close()

#批量创建查看、编辑、删除权限管理员
def create_manage_all():
	user_file = open(r"C:/register_admin_user_list_all.txt", 'w')
	i = 1
	pre_name = 'alllog_'
	for item in driver.find_elements("class name", "categoryAuthorityBox"):
		admin_username = create_manage_fillmanage(pre_name, i, user_file)
		if i == 1:
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-add-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-add').eq(" + str(i-1) + ").attr('style','display:none'); \
				$('.categoryAuthority-delete-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-delete').eq(" + str(i-1) + ").attr('style','display:none')")
		else:
			driver.execute_script("$('.onOff').click()")
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none'); \
				$('.categoryAuthority-add-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-add').eq(" + str(i-1) + ").attr('style','display:none'); \
				$('.categoryAuthority-delete-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-delete').eq(" + str(i-1) + ").attr('style','display:none')")
		time.sleep(1)
		driver.find_element_by_link_text(u"取消").click()
		time.sleep(1)
		user_file.writelines(admin_username + "\n")
		i = i + 1
		time.sleep(1)
		driver.find_element_by_link_text(u"添加管理员").click() 
		time.sleep(5)
	print '删除权限管理员个数' + str(i)
	user_file.close()

#创建管理员填写信息公用方法
def create_manage_fillmanage(pre_name, i, user_file):
	time.sleep(1)
	prefix = chr(random.randint(97, 122)) + chr(random.randint(97, 122)) + chr(random.randint(97, 122))
	admin_name = pre_name + prefix + str(i)
	admin_username = admin_name 
	admin_email = admin_name + "@sohu.com"
	admin_psw = 'gy0411'
	time.sleep(1)
	driver.find_element("id", "admin_name").send_keys(admin_name)#管理员名称
	time.sleep(1)
	driver.find_element("id", "admin_username").send_keys(admin_username)#用户名
	time.sleep(1)
	driver.find_element("id", "admin_password").send_keys(admin_psw)#密码
	time.sleep(1)
	driver.find_element("id", "admin_repassword").send_keys(admin_psw)#再次输入密码
	time.sleep(1)
	driver.find_element("id", "admin_email").send_keys(admin_email)#邮箱
	time.sleep(1)
	driver.find_element("id", "admin_reemail").send_keys(admin_email)#再次确认邮箱
	time.sleep(1)
	return admin_username

#创建管理员
def create_manage():
	time.sleep(15)
	driver.get("%smyOffice.do" %(base_url))
	time.sleep(8)
	driver.find_element_by_link_text(u"系统设置").click()   
	time.sleep(6)
	driver.find_element_by_link_text(u"网校管理员").click() 
	time.sleep(6)
	driver.find_element_by_link_text(u"添加管理员").click() 
	time.sleep(4)
	# create_manage_read()#批量创建读权限管理员
	# create_manage_edit()#批量创建编辑权限管理员
	# create_manage_delete()#批量创建删除权限管理员
	create_manage_all()#批量创建读、编辑、删除权限管理员

#系统设置-管理员/客服-网校客服
def manageorservice_service():
	time.sleep(1)
	current_url = driver.current_url
	time.sleep(1)
	try:
	    driver.find_element("class name", "header-cs")#找到网校客服查看网校管理员帮助视频>>
	except Exception:
		print traceback.format_exc()
		print u"没有网校客服的读权限"
	
	time.sleep(2)		
	rand_name = str(random.randint(1000, 9999))
	service_name = u"se" + rand_name
	try:
		#创建机构客服
	    driver.find_element("class name", "toCreatePage").click()#点击创建机构客服
	    time.sleep(1)
	    driver.find_element("class name", "x-form-arrow-trigger").click()#下拉选择用户名
	    time.sleep(1)
	    driver.find_elements("class name", "x-combo-list-item")[1].click()
	    time.sleep(1)
	    driver.find_element("id", "reg_supName").send_keys(service_name)#输入客服名
	    time.sleep(1)
	    driver.find_element("class name", "GreenBtn_ab").click()#点击保存
	    time.sleep(1)
	    #编辑
	    driver.find_elements("css selector", ".supportUl .editSup")[-1].click()#点击编辑  
	    time.sleep(1)
	    driver.find_element("class name", "GreenBtn_ab").click()#点击保存
	    time.sleep(1)
	    #编辑-机构客服显示方式
	    driver.find_element("css selector", ".supportDisplay .editDisplay").click()#点击编辑  
	    time.sleep(1)
	    driver.find_element("class name", "GreenBtn_ab").click()#点击保存
	    time.sleep(1)
	    #选择使用自定义客服-编辑
	    driver.find_elements("name", "customizedSupportEnabled")[1].click()#选择使用自定义客服
	    time.sleep(1)
	    driver.find_element("id", "J_toEditBtn").click()#点击编辑
	    time.sleep(1)	      	    
	    driver.find_element("id", "J_saveCodeBtn").click()#点击保存
	    time.sleep(1)
	    #选择使用AbkeSky机构客服 
	    driver.find_element("name", "customizedSupportEnabled").click()#选择使用AbkeSky机构客服    	    	    	    
	except Exception:
		print traceback.format_exc()
		print u"没有网校客服的编辑权限"
		
	time.sleep(2)
	try:
		#删除
	    driver.find_elements("css selector", ".supportUl .delSup")[-1].click()#点击删除-最后一个创建的机构客服  
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击确定
	    time.sleep(1)	    
	except Exception:
		print traceback.format_exc()
		print u"没有网校客服的删除权限"	
			
#系统设置-页面建设-首页高级编辑 
def pagecreate_edit():
	time.sleep(1)
	try:
		#预览首页
	    driver.find_elements("class name", "GreenBtn_ab")[-1].click()#点击预览首页
	    time.sleep(1)	    
	except Exception:
		print traceback.format_exc()
		print u"没有首页高级编辑的读、删除权限"	

	time.sleep(1)
	try:
		#发布
	    driver.find_element("class name", "OrangeBtn_ab").click()#点击发布  
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击关闭窗口
	    time.sleep(1)	    
	except Exception:
		print traceback.format_exc()
		print u"没有首页高级编辑的编辑权限"	

#系统设置-页面建设-自定义页面 
def pagecreate_selfpage():
	time.sleep(1)
	try:
		#找到页面html图片
	    driver.find_element("css selector",".floatleft img")
	    time.sleep(1)   
	except Exception:
		print traceback.format_exc()
		print u"没有自定义页面的读权限"
		
	time.sleep(2)
	rand_name = str(random.randint(1000, 9999))
	page_name = u"page" + rand_name	
	try:
		#添加页面
	    driver.find_element("class name", "yellow_btn_center").click()#点击添加页面
	    time.sleep(1)
	    driver.find_element("id", "orgPageField").send_keys(page_name)#页面名称
	    time.sleep(1)
	    driver.find_element("id", "orgWebField").send_keys(rand_name)#为页面设定链接
	    time.sleep(1)
	    driver.find_element("id", "orgInfoField").send_keys("<html><body>hello word!</body></html>")#代码嵌入
	    time.sleep(1)
	    driver.find_elements("class name", "x-btn-text")[-1].click()#点击保存
	    time.sleep(1)
	    #编辑
	    driver.find_element_by_link_text(u"编辑").click()#点击编辑
	    time.sleep(1)
	    driver.find_elements("class name", "x-btn-text")[-1].click()#点击保存
	    time.sleep(1)	    
	    #设为自设导航模块
	    driver.find_element_by_link_text(u"设为自设导航模块").click()#点击设为自设导航模块
	    time.sleep(1)
	    driver.find_element("id", "titleFieldId").send_keys(rand_name)#导航名称
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击确定
	    time.sleep(1)	    
	    #取消自设导航模块
	    driver.find_element_by_link_text(u"取消自设导航模块").click()#点击取消自设导航模块
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击确定
	    time.sleep(1)	    	    	    
	except Exception:
		print traceback.format_exc()
		print u"没有自定义页面的编辑权限"	

	time.sleep(2)
	try:
		#删除
	    driver.find_element_by_link_text(u"删除").click()#点击删除
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击删除
	    time.sleep(1)    
	except Exception:
		print traceback.format_exc()
		print u"没有自定义页面的删除权限"
			
#系统设置-页面建设-网络图片库 
def pagecreate_netpic():
	time.sleep(1)
	current_url = driver.current_url
	rand_name = str(random.randint(1000, 9999))
	record_name = u"record" + rand_name
	pic = "C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg"	
	try:
		#点击第一个图片库
	    driver.find_element("class name", "albumName").click()
	    time.sleep(1)
	    driver.find_element("class name", "albumBg").click()#复制第一个链接   
	    time.sleep(1)
	    driver.find_element_by_link_text(u"返回网络图片库").click()
	    #driver.get(current_url)   
	except Exception:
		print traceback.format_exc()
		print u"没有网络图片库的读权限"
		
	time.sleep(1)
	try:
		#创建专辑
	    driver.find_elements("class name", "cursorHand")[1].click()#点击创建专辑
	    time.sleep(1)
	    driver.find_element("id", "orgAlbumField").send_keys(record_name)#输入专辑名称
	    time.sleep(1)  
	    driver.find_element("id", "picture1").send_keys(pic)#点击浏览上传图片
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击上传
	    time.sleep(2)
	    driver.get(current_url)
	    time.sleep(2)
	    #添加新照片
	    driver.find_element("class name", "albumName").click()#点击选择第一个刚创建的图片库
	    time.sleep(1)
	    current_url = driver.current_url
	    driver.find_element_by_link_text(u"添加新照片").click()
	    time.sleep(1)	    
	    driver.find_element("id", "picture1").send_keys(pic)#点击浏览上传图片
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击上传 
	    time.sleep(5)
	    driver.get(current_url)
	    #修改专辑名称	    
	    driver.find_element_by_link_text(u"修改专辑名称").click()
	    time.sleep(1)	    
	    driver.find_element("class name", "x-btn-text").click()#点击保存
	    time.sleep(1)  	    
	except Exception:
	    print traceback.format_exc()
	    print u"没有网络图片库的编辑权限"

	time.sleep(2) 
	try:
	    #删除图片
	    try:
	        driver.find_element("class name", "albumName").click()#点击第一个图片库
	        time.sleep(1)
	        driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[6]/div[2]").click()
	        time.sleep(1)	    
	        driver.find_element("class name", "x-btn-text").click()#点击确认
	        time.sleep(1)
	    except:
	        print '此专辑么有图片哦'
	    #添加图片--上传图片--删除
	    current_url = driver.current_url
	    driver.find_element_by_link_text(u"添加新照片").click()
	    time.sleep(1)	    
	    driver.find_element("id", "picture1").send_keys(pic)#点击浏览上传图片
	    time.sleep(1)
	    driver.find_element("class name", "deleteAb").click()#点击删除 
	    time.sleep(1)
	    driver.get(current_url)	    
#	    #删除专辑 
#	    driver.find_element_by_link_text(u"删除专辑").click()
#	    time.sleep(1)
#	    driver.find_element("class name","x-btn-text").click()#点击确认-网站有bug，报参数错误    
	except Exception:
		print traceback.format_exc()
		print u"没有网络图片库的删除权限"
	
#系统设置-页面建设-自定义登录图片 
def pagecreate_selflogin():
	time.sleep(1)
	current_url = driver.current_url
	try:
		#能找到第一个的登录图片
	    driver.find_element("id","J_showImage")   
	    time.sleep(1)  
	except Exception:
		print traceback.format_exc()
		print u"没有自定义登录图片的读、删除权限"

	time.sleep(1)
	pic = "C:\\Users\\Public\\Pictures\\Sample Pictures\\1.jpg"
	try:
		#点击浏览
	    time.sleep(1)
	    driver.find_element("id", "picFieldName-file").send_keys(pic)#浏览   
	    time.sleep(1)
	    driver.find_elements("class name", "x-btn-text")[1].click()#上传
	    time.sleep(2)
	    driver.get(current_url)
	    time.sleep(1)
	    #恢复默认
	    driver.find_element("id", "J_restoreDefault").click()
	except Exception:
		print traceback.format_exc()
		print u"没有自定义登录图片的编辑权限"
			
#学员/员工-网校学员-学员类目   
def stuoremp_stucate():
	time.sleep(1)
	current_url = driver.current_url
	try:
		driver.find_element("class name", "expandSub ")#找到展开图标
		time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有学员类目的读权限"

	time.sleep(1)
	try:
	    driver.find_element("id", "J_genTopCateg").click()#新建一级类目
	    creat_stucate()#新建一级类目
	    driver.get(current_url)
	    bh = driver.window_handles
	    manage_catestu(bh)#管理类目学员
	    bh = driver.window_handles 
	    opencourseBatch(bh)#批量开通课程
	    driver.get(current_url)
	    driver.find_element("class name", "editCateg").click()#编辑类目
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击确定		
	    time.sleep(1)
	    driver.find_element("class name", "addSub").click()#添加子类目
	    creat_stucate()
	    time.sleep(1)				    
	except Exception:
		print traceback.format_exc()
		print u"没有学员类目的编辑权限"

	time.sleep(2)
	try:
	    driver.find_elements("class name", "delete")[-1].click()#删除类目
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击删除		
	    time.sleep(2)	
	except Exception:
		print traceback.format_exc()
		print u"没有学员类目的删除权限"
	driver.get(current_url)
	time.sleep(2)

#新建一级类目和子类目的方法		
def creat_stucate():
	time.sleep(1)
	rand_name = str(random.randint(1000, 9999))
	cate_name = u"catetest" + rand_name
	try:
	   driver.find_element("id", "reg_topCateName").send_keys(cate_name)#输入类目名称
	except:
	    try:
	        driver.find_element("id", "reg_textField").send_keys(cate_name)#输入类目名称
	    except:
		    None		
	time.sleep(1)
	driver.find_element("class name", "x-btn-text").click()#点击确定			
	time.sleep(1)

#管理类目学员的方法
def manage_catestu(bh):
	time.sleep(3)
	driver.find_element("class name", "manageCategStudent").click()
	ah = driver.window_handles
	swithing_window(bh,ah)
	time.sleep(3)
	driver.find_element_by_link_text(u"添加现有学员").click()
	time.sleep(2)
	driver.find_element_by_link_text(u"全部").click()
	time.sleep(2)
	driver.find_elements("css selector", ".x-panel-bwrap .x-btn-text")[-1].click()
	time.sleep(2)
	driver.find_element_by_link_text(u"返回").click()
	time.sleep(2)

#批量开通课程
def opencourseBatch(bh):
	time.sleep(1)
	driver.find_elements("class name", "openCourseBatch")[0].click()
	time.sleep(3)
	ah = driver.window_handles
	swithing_window(bh,ah)
	driver.find_elements("css selector", "input[type=checkbox]")[-1].click()#勾选最后一个课程类目
	time.sleep(2)
	driver.find_element("class name", "x-btn-text").click()
	time.sleep(2)
	driver.find_elements("css selector", ".x-btn-center .x-btn-text")[1].click()
	time.sleep(3)		
#学员/员工-网校学员-学员管理
def stuoremp_stumanage():
	time.sleep(2)
	current_url = driver.current_url
	try:
		driver.find_element_by_link_text(u"筛选").click()#点击筛选
		time.sleep(1)
		#页面下方批量操作-导出账户信息
		driver.find_element("name","userCheck").click()#勾选第一个学员
		time.sleep(1)
		driver.find_element("class name","x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name","x-combo-list-item ")[1].click()
		time.sleep(1)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有学员管理的读权限"
	
	org_name = "stu_gy"
	user_name = "stu_gy50"
	stu_num = 5
	driver.get(current_url)
	time.sleep(3)
	try:
		driver.find_element_by_link_text(u"批量导入学员").click()#批量导入学员
		time.sleep(2)
		driver.find_element_by_link_text(u"返回").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"批量创建学员").click()#批量创建学员
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"开通课程").click()#开通课程
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click() 
		time.sleep(1)
		driver.find_element_by_link_text(u"管理播放授权数").click()#管理播放授权数
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click() 
		time.sleep(1)
		driver.find_element_by_link_text(u"延长授权").click()#延长授权
		time.sleep(1)
		driver.find_elements("class name", "x-btn-text")[-1].click()#点击取消
		time.sleep(1)
		#逐一导入手动导入测试
#		student_management.import_multi_student(cfg, driver, \
#			base_url, org_name, r"C:\register_user_list.txt")#批量导入学员
#		time.sleep(1)
#		driver.get(current_url)
#		time.sleep(1)
#		student_management.auto_create_student(cfg, driver, \
#			base_url, org_name, stu_num)#批量创建学员
#		time.sleep(1)
#		driver.get(current_url)
#		time.sleep(1)
#		student_management.open_course_for_one(cfg, driver, base_url, org_name)#开通课程
#		time.sleep(1)			
#		student_management.manage_course_num(cfg, driver, base_url, user_name)#管理播放授权数 
#		time.sleep(2)
#		driver.find_element_by_link_text(u"延长授权").click()#延长授权
#		time.sleep(1)
#		driver.find_elements("class name", "x-btn-text")[-1].click()#点击取消
		time.sleep(1)
		#页面下方的批量操作-开通课程
		driver.find_element("name","userCheck").click()#勾选第一个学员
		time.sleep(1)
		driver.find_element("class name","x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name","x-combo-list-item ")[0].click()
		time.sleep(1)
		driver.get(current_url)
		time.sleep(1)													
	except Exception:
		print traceback.format_exc()
		print u"没有学员管理的编辑权限" 

	time.sleep(2)
	try:
		driver.find_element_by_link_text(u"删除学员").click()#删除学员
		time.sleep(1)
		driver.find_element("css selector", ".x-panel-btns-right .x-btn-text").click()#点击确定
		time.sleep(1)
		try:
			driver.find_element_by_link_text(u"删除帐号").click()
			time.sleep(1)
			driver.find_element("class name", "x-btn-text").click()#点击确定
			time.sleep(2)
		except:
			print "没有找到删除帐号"
		#页面下方的批量操作-删除员工（删除账号手动测试）
		driver.find_element("name", "userCheck").click()#勾选第一个
		time.sleep(1)
		driver.find_element("class name", "x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item ")[2].click()
		time.sleep(2)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(2)
		driver.find_element("css selector", ".x-panel-btns-right .x-btn-text").click()#确定		
	except Exception:
		print traceback.format_exc()
		print u"没有学员管理的删除权限"
	  
#学员/员工-网校学员-员工管理
def stuoremp_empmanage():
	time.sleep(2)
	current_url = driver.current_url
	try:
		#筛选
		driver.find_element_by_link_text(u"筛选").click()#点击筛选
		time.sleep(1)
		#页面下方批量操作-导出账户信息
		driver.find_element("name","userCheck").click()#勾选第一个
		time.sleep(1)
		driver.find_element("class name","x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name","x-combo-list-item ")[1].click()
		time.sleep(1)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(2)
	except Exception:
		print traceback.format_exc()
		print u"没有员工管理的读权限"
	
	org_name = "stu_gy"
	user_name = "stu_gy50"
	driver.get(current_url)
	time.sleep(3)
	try:
		#逐一导入手动导入测试
		driver.find_element_by_link_text(u"批量导入员工").click()#批量导入员工
		time.sleep(2)
		driver.find_element_by_link_text(u"返回").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"批量创建员工").click()#批量创建员工
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"开通课程").click()#开通课程
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click() 
		time.sleep(1)
		driver.find_element_by_link_text(u"管理播放授权数").click()#管理播放授权数
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click() 
		time.sleep(1)
#		student_management.open_course_for_one(cfg, driver, base_url, org_name)#开通课程
#		time.sleep(1)
#		student_management.manage_course_num(cfg, driver, base_url, user_name)#管理播放授权数 
#		time.sleep(1)
		driver.find_element_by_link_text(u"延长授权").click()#延长授权
		time.sleep(1)
		driver.find_elements("class name", "x-btn-text")[-1].click()#点击取消
		time.sleep(1)
		#页面下方的批量操作-开通课程
		driver.find_element("name","userCheck").click()#勾选第一个
		time.sleep(1)
		driver.find_element("class name","x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name","x-combo-list-item ")[0].click()
		time.sleep(1)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(2)
		driver.get(current_url)
		time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"没有员工管理的编辑权限" 

	time.sleep(2)
	try:
		driver.find_element_by_link_text(u"删除员工").click()#删除员工
		time.sleep(1)
		driver.find_elements("css selector", ".x-panel-btns-right .x-btn-text")[1].click()#先取消删除
		time.sleep(1)
		#页面下方的批量操作-删除员工（删除账号手动测试）
		driver.get(current_url)
		time.sleep(1)
		driver.find_element("name", "userCheck").click()#勾选第一个
		time.sleep(1)
		driver.find_element("class name", "x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item ")[2].click()
		time.sleep(2)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(2)
		driver.find_elements("css selector", ".x-panel-btns-right .x-btn-text")[-1].click()#先取消删除
		time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有员工管理的删除权限"
	
#学员/员工-网校学员-员工申请
def stuoremp_empapply():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"查看资料").click()#点击查看资料
	    time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"没有员工申请的读权限"
	####加黑名单是什么权限？	
	time.sleep(1)
	try:
		driver.find_element("css selector", ".action span").click()#点击通过
		time.sleep(1)
		driver.find_elements("css selector", ".action span")[1].click()#点击拒绝
		time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"没有员工申请的编辑、删除权限"
			
#学员/员工-网校学员-学员学习记录
def stuoremp_stulearnrecord():
	time.sleep(1)
	current_url = driver.current_url
	try:
		#driver.find_element("class name", ".GreenBtn_ab").click()#导出学员学习记录
		time.sleep(1)
		driver.find_element("id", "J_stuType").click()#选择学员类型
		time.sleep(1)
		driver.find_element("css selector", "#J_stuType option").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"查询").click()#点击查询
		time.sleep(1)
#		driver.find_element("class name", "center").click()#点击导出学员学习记录的excel文件
#		time.sleep(3)
		bh = driver.window_handles
		driver.find_element_by_link_text(u"详情").click()
		time.sleep(1)		
		ah = driver.window_handles
		swithing_window(bh,ah)
		time.sleep(1)    
		driver.find_elements("class name", "centercafC")[3].click()#点击学习记录tab
		time.sleep(2)
		driver.find_element("class name", "x-btn-center").click()#点击过滤
		time.sleep(2)
		driver.find_elements("class name", "cursorHand")[1].click()#点击导出学习记录的excel文件
		time.sleep(1)
		driver.get(current_url)
		time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"没有学员学习记录的读、编辑、删除权限"	    		  
   
def admin_athority_check():
    
	global base_url
	global cfg 
	global driver
	base_url = "http://www.ablesky.com/"
	# base_url = "http://www.ablesky-a.com:8080/"
	cfg_file = 'config.ini'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(cfg_file)
	# user_name = "v52"
	# user_psw = "1234"    
	user_name = "sadm_gaoyue"
	user_psw = "123456aa"

	chromedriver = "C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	#driver = webdriver.Ie()

	login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
	# driver.get("%smyOffice.do" %(base_url))

	# #后台-先创建管理员	
	# create_manage()

	# #后台-后台首页
	# teaching()#教学互动
	# authmanage()#授权管理
	# courseagent()#课程合作代理
	# learnigcard()#学习卡
	# countmanage()#统计管理

	# #后台-系统设置
	# manageorservice()#管理员/客服
	# pagecreate()#页面建设

	# #后台-学员/员工
	# stuoremp()#网校学员
	
	##(fore_stage())
	driver.find_element_by_link_text(u"网校首页").click()
	time.sleep(1)
	# firstpage()#首页
	course_center_relate()#课程中心
	# class_center_relate()#报班中心 
	# online_ansquestion()#在线答疑
	# live_course_relate()#直播课程
	# cheap_course_relate()#特惠课程
	# online_exam_relate()#在线考试
	# school_notice()#网校公告
	# teacher_team()#名师团队
	# school_members()#网校成员
	about_us()#关于我们
	help_center()#帮助中心
        
	driver.quit()
    
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	admin_athority_check()
    