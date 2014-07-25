# -*- coding: UTF-8 -*-
def importquestions(self):
    db = 'ablesky_examsystem'
    conn = self.connect_db(db)
    cursor = conn.cursor()
    sql = "SELECT COUNT(*) FROM e_question_q"
    cursor.execute(sql)
    num1 = cursor.fetchall()[0][0]
    cursor.close()
    #以下部分可删除,要求调用此函数的同学保证停在试题库页面
    self.driver.get \
        ("%s/exam/subjectRedirect.do?action=toSubjectList&organizationId=2249" \
         %(self.base_url))
    self.driver.find_element("partial link text", "点击这里").click()
    self.driver.implicitly_wait(30)
    self.driver.find_element("link text", "试题库").click()
    self.driver.implicitly_wait(30)
    self.driver.find_element("link text", "单选题").click()
    self.driver.implicitly_wait(30)
    
    self.driver.find_element(self.cfg.get('exam', "import_questions_by"), \
                             self.cfg.get('exam', 'import_questions')).click()
    self.driver.find_element(self.cfg.get('exam', "path_by"), \
                             self.cfg.get('exam', "path")).send_keys(self.template)
    self.driver.find_element(self.cfg.get('exam', "upload_button_by"), \
                             self.cfg.get('exam', "upload_button")).click()
    self.driver.find_element(self.cfg.get('exam', "close_button_by"), \
                             self.cfg.get('exam', "close_button")).click()
    conn = self.connect_db(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    num2 = cursor.fetchall()[0][0]
    num = num2 - num1
    cursor.execute \
        ("SELECT content_q,content_q FROM e_question_q ORDER BY id_q DESC LIMIT 1")
    title = cursor.fetchall()[0][0]
    msg = "导入%d道试题,最后一个试题题目为%s"%(num, title)
    print msg
     