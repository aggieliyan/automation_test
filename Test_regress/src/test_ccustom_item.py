#coding=utf-8
import MySQLdb


conn = MySQLdb.connect(host='192.168.120.110', user='root',passwd='mysqlpwd1',db='ajaxableskydb',charset='utf8')
ORGID = "2594"
sql = "select id from course where ACCOUNT_ID = "+ORGID+" and ENABLED = 1 limit 2000;"
cursor = conn.cursor()
cursor.execute(sql)
results = cursor.fetchall()
# print results[0][0]

for courseid in results:
	sql2 = "insert into course_custom_item_detail \
	(id_course_ccid, id_custom_item_ccid, value_ccid, id_account_ccid ) \
	values("+str(courseid[0])+", 25, 'aaa' ,2594)"
	cursor.execute(sql2)

conn.commit()