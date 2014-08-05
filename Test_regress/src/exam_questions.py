# -*- coding: UTF-8 -*-
import time

def importquestions(self,cfg,driver, base_url,template):
    db = 'ablesky_examsystem'
    conn = self.connect_db(db)
    cursor = conn.cursor()
    sql = "SELECT COUNT(*) FROM e_question_q"
    cursor.execute(sql)
    num1 = cursor.fetchall()[0][0]
    cursor.close()
    #以下部分可删除,要求调用此函数的同学保证停在试题库页面
    driver.get(base_url + "exam/")
    #driver.find_element("partial link text", "点击这里").click()
    driver.implicitly_wait(30)
    driver.find_element("link text", u"试题库").click()
    driver.implicitly_wait(30)
    driver.find_element("link text", u"单选题").click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam', "import_questions_by"), \
                             cfg.get('exam', 'import_questions')).click()
    driver.find_element(cfg.get('exam', "path_by"), \
                             cfg.get('exam', "path")).send_keys(template)
    driver.find_element(cfg.get('exam', "upload_button_by"), \
                             cfg.get('exam', "upload_button")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam', "close_button_by"), \
                             cfg.get('exam', "close_button")).click()
    conn = self.connect_db(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    num2 = cursor.fetchall()[0][0]
    num = num2 - num1
    cursor.execute \
        ("SELECT content_q,content_q FROM e_question_q ORDER BY id_q DESC LIMIT 1")
    title = cursor.fetchall()[0][0]
    msg = u"导入%d道试题,最后一个试题题目为%s"%(num, title)
    print msg

#创建单选题 
def exam_question_Single(cfg,driver, base_url,question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成 
    driver.find_element(cfg.get('exam_questions',"question_creat_by"),\
        cfg.get('exam_questions',"question_creat")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    #添加音频
    driver.find_element(cfg.get('exam_questions',"question_yinpin_by"),\
        cfg.get('exam_questions',"question_yinpin")).send_keys\
        ("//data.ablesky.com/workspace/Testing/Testing Files/Automation_test/123.mp3")    
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(2)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(3)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_save_by"),\
        cfg.get('exam_questions',"question_save")).click()
    time.sleep(2)
    driver.find_element_by_link_text("单选题").click()
    time.sleep(2)
    
    #创建多选题
def exam_question_Multiple(cfg,driver, base_url,question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成     
    driver.find_element(cfg.get('exam_questions',"question_creat_by"),\
        cfg.get('exam_questions',"question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_by"),\
        cfg.get('exam_questions',"question_type")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_duoxuan_by"),\
        cfg.get('exam_questions',"question_type_duoxuan")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(2)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(3)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_save_by"),\
        cfg.get('exam_questions',"question_save")).click()
    time.sleep(2)
    driver.find_element_by_link_text("单选题").click()
    time.sleep(2)
    
#创建是非题
def exam_question_TrueOrFalse(cfg,driver, base_url,question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成  
    driver.find_element(cfg.get('exam_questions',"question_creat_by"),\
        cfg.get('exam_questions',"question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_by"),\
        cfg.get('exam_questions',"question_type")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_shifei_by"),\
        cfg.get('exam_questions',"question_type_shifei")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_save_by"),\
        cfg.get('exam_questions',"question_save")).click()
    time.sleep(2)
    driver.find_element_by_link_text("单选题").click()
#    time.sleep(2)
    
#创建问答题
def exam_question_Answer(cfg,driver, base_url,question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成      
    driver.find_element(cfg.get('exam_questions',"question_creat_by"),\
        cfg.get('exam_questions',"question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_by"),\
        cfg.get('exam_questions',"question_type")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_wenda_by"),\
        cfg.get('exam_questions',"question_type_wenda")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(2)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_save_by"),\
        cfg.get('exam_questions',"question_save")).click()
    time.sleep(2)
    driver.find_element_by_link_text("单选题").click()
    
#创建填空题
def exam_question_Blank(cfg,driver, base_url,question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成  
    driver.find_element(cfg.get('exam_questions',"question_creat_by"),\
        cfg.get('exam_questions',"question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_by"),\
        cfg.get('exam_questions',"question_type")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_tiankong_by"),\
        cfg.get('exam_questions',"question_type_tiankong")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    #driver.find_element_by_xpath(cfg.get('exam_questions','question_tiankonganswer_xpath_by')).send_keys("123")
    driver.find_element(cfg.get('exam_questions',"question_tiankonganswer_by"),\
        cfg.get('exam_questions',"question_tiankonganswer")).send_keys(question_ansa)
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_save_by"),\
        cfg.get('exam_questions',"question_save")).click()
    time.sleep(2)
    driver.find_element_by_link_text("单选题").click()
    
#创建完型填空题
def exam_question_Cloze(cfg,driver, base_url,question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成  
    driver.find_element(cfg.get('exam_questions',"question_creat_by"),\
        cfg.get('exam_questions',"question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_by"),\
        cfg.get('exam_questions',"question_type")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_wanxing_by"),\
        cfg.get('exam_questions',"question_type_wanxing")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_wanxinganswer1_by"),\
        cfg.get('exam_questions',"question_wanxinganswer1")).send_keys(question_ansa)
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_wanxinganswer2_by"),\
        cfg.get('exam_questions',"question_wanxinganswer2")).send_keys(question_ansa)
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_wanxinganswer3_by"),\
        cfg.get('exam_questions',"question_wanxinganswer3")).send_keys(question_ansa)
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_wanxinganswer4_by"),\
        cfg.get('exam_questions',"question_wanxinganswer4")).send_keys(question_ansa)
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_save_by"),\
        cfg.get('exam_questions',"question_save")).click()
    time.sleep(2)
    driver.find_element_by_link_text("单选题").click()
    
#创建综合题
def exam_question_Composite(cfg,driver, base_url,question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成  
    driver.find_element(cfg.get('exam_questions',"question_creat_by"),\
        cfg.get('exam_questions',"question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_by"),\
        cfg.get('exam_questions',"question_type")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_type_zonghe_by"),\
        cfg.get('exam_questions',"question_type_zonghe")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(2)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(4)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(5)').attr('id')")    
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions',"question_save_by"),\
        cfg.get('exam_questions',"question_save")).click()
    time.sleep(2)
    driver.find_element_by_link_text("单选题").click()
    time.sleep(2)
    
def auto_exam_questions(cfg,driver, base_url,question_ansa, num):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    #num为循环次数
    # 试题名称：
    # Single:单选题
    # Multiple：多选题
    # TrueOrFalse：是非题
    # Blank：填空题
    # Answer：问答题
    # cloze：完型题
    # Composite：综合题
    time.sleep(2)
    driver.get(base_url + "exam/")
    time.sleep(2)
    driver.find_element_by_link_text("试题库").click()
    time.sleep(2)
    driver.find_element_by_link_text("单选题").click()
    time.sleep(2) 
    for i in range(num):
        exam_question_Single(cfg,driver, base_url,question_ansa)
        exam_question_Multiple(cfg,driver, base_url,question_ansa)
        exam_question_TrueOrFalse(cfg,driver, base_url,question_ansa)
        exam_question_Blank(cfg,driver, base_url,question_ansa)
        exam_question_Answer(cfg,driver, base_url,question_ansa)
        exam_question_Cloze(cfg,driver, base_url,question_ansa)
        exam_question_Composite(cfg,driver, base_url,question_ansa)
        
def auto_exam_onequestion(cfg,driver, base_url,question_ansa, onetype):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    #onetype == 1:创建单选题
    #onetype == 2:创建多选题
    #onetype == 3:创建是非题
    #onetype == 4:创建填空题
    #onetype == 5:创建问答题
    #onetype == 6:创建完型题
    #onetype == 7:创建综合题
    time.sleep(2)
    driver.get(base_url + "exam/")
    time.sleep(2)
    driver.find_element_by_link_text("试题库").click()
    time.sleep(2)
    driver.find_element_by_link_text("单选题").click()
    time.sleep(2) 
    if onetype == 1:
        exam_question_Single(cfg,driver, base_url,question_ansa)
    elif onetype == 2:
        exam_question_Multiple(cfg,driver, base_url,question_ansa)
    elif onetype == 3:
        exam_question_TrueOrFalse(cfg,driver, base_url,question_ansa)
    elif onetype == 4:
        exam_question_Blank(cfg,driver, base_url,question_ansa)
    elif onetype == 5:
        exam_question_Answer(cfg,driver, base_url,question_ansa)
    elif onetype == 6:
        exam_question_Cloze(cfg,driver, base_url,question_ansa)
    elif onetype == 7:
        exam_question_Composite(cfg,driver, base_url,question_ansa)       
     