# -*- coding: UTF-8 -*-
'''
Created on Oct 23, 2012

@author: yilulu
'''
import MySQLdb,user_management,ConfigParser,login
from selenium import webdriver


def connect_db(dbhost,database):
    try:
        conn = MySQLdb.connect(host=dbhost, user='root',passwd='mysqlpwd1',db=database,charset='utf8')
    except Exception,e:
        print e
    return conn

def get_course_id():
    
    dbhost = "192.168.190.250"
    db='ajaxableskydb'
    conn = connect_db(dbhost,db)
    sql = "SELECT c.id FROM course c,account a WHERE c.ACCOUNT_ID=a.ID AND c.CHARGETYPE=2 AND c.ENABLED=1 AND c.ONLINESTATUS='online' AND a.username='offcn'"
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()#关闭数据库连接
    return results

def buy_course():
    
    user_name = "stu_aa02"
    user_psw = "1234"     
    cfg_file = 'config.ini'
    test_enviroment = "omega"
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file)
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    base_url = "http://www."+test_enviroment+".ablesky.com/"
    
    results = get_course_id()
    login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
    for id in results[50:]:
        print id[0]
        url = "http://www.omega.ablesky.com/viewCourseDetail.do?courseId="+str(id[0])
        try:
            user_management.buy_course(cfg, driver, url)
        except Exception,e:
            print url
        
    driver.quit()
    
if __name__ == "__main__":
   
    buy_course()