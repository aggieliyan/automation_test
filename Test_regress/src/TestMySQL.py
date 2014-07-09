#coding=utf-8
'''
Created on Nov 25, 2011

@author: fujun
'''
import MySQLdb
from datetime import datetime
from datetime import timedelta
class MySQL():
    
    def queryByUsername(self,username,xml):
        #新建数据库连接
        conn = MySQLdb.connect(host=xml.getValue(xml.getNode("mysqlurl")[0]), user=xml.getValue(xml.getNode("mysqluser")[0]),passwd=xml.getValue(xml.getNode("mysqlpassword")[0]),db='ajaxableskydb',charset=xml.getValue(xml.getNode("mysqlcharacterset")[0]))
        sql = "select * from account where username = '"+username+"'"
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    def queryByFileName(self,filename,xml):
        #新建数据库连接
        conn = MySQLdb.connect(host=xml.getValue(xml.getNode("mysqlurl")[0]), user=xml.getValue(xml.getNode("mysqluser")[0]),passwd=xml.getValue(xml.getNode("mysqlpassword")[0]),db='ajaxableskydb',charset=xml.getValue(xml.getNode("mysqlcharacterset")[0]))
        sql = "select * from content where filename='"+filename+"' order by id desc limit 1"#取文件名为上传文件的最新一条记录
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

#关闭连接，释放资源
        cursor.close();
if __name__ == "__main__":
    #mysql = MySQL()
    conn = MySQLdb.connect(host='192.168.200.24', user='root',passwd='mysqlpwd1',db='ajaxableskydb',charset='utf8')
    sql = "SELECT a.USERNAME,a.PASSWORD FROM account a,course c,coursecontent cc,course_authority ca WHERE a.ID=ca.BUYER_ID AND c.ID=cc.COURSE_ID AND c.ID=ca.COURSE_ID AND cc.ID=ca.COURSE_CONTENT_ID AND cc.TIMES_LIMIT>ca.TOTAL_TIMES_LIMIT AND c.ACCOUNT_ID=611227"
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print len(results)
