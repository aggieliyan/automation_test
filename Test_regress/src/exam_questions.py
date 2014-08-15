# -*- coding: UTF-8 -*-
import time
from selenium.webdriver.common.keys import Keys

def importquestions(cfg, driver, base_url, template):
    driver.get(base_url + "exam/")
    driver.implicitly_wait(30)
    driver.find_element("link text", u"试题库").click()
    driver.implicitly_wait(30)
    
    driver.find_element(cfg.get('exam', "import_questions_by"), \
                             cfg.get('exam', 'import_questions')).click()    
    driver.execute_script("$('#J_uploadFileInput').attr('style','height:20px;opacity:1;transform:translate(0px, 0px) scale(1)')")
    time.sleep(1)
    driver.find_element(cfg.get('exam', "path_by"), \
                             cfg.get('exam', "path")).send_keys(template)
    driver.find_element(cfg.get('exam', "upload_button_by"), \
                             cfg.get('exam', "upload_button")).click()
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('exam', "close_button_by"), \
                             cfg.get('exam', "close_button")).click()
    
    
#创建单选题
def exam_question_Single(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    driver.find_element(cfg.get('exam_questions', "question_creat_by"), \
        cfg.get('exam_questions', "question_creat")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)') \
        .attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    #添加音频
    driver.find_element(cfg.get('exam_questions', "question_music_by"), \
        cfg.get('exam_questions', "question_music")).send_keys \
        (r"\\data.ablesky.com\workspace\Testing\Testing Files\Automation_test\123.mp3")
    driver.implicitly_wait(10)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(2)') \
        .attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument; element=idocument.getElementById('tinymce'); \
    element.innerHTML = \'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(3)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    #添加选项
    driver.find_element(cfg.get('exam_questions', "question_Single_addanswer_by"), \
        cfg.get('exam_questions', "question_Single_addanswer")).click()
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(4)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    #添加解析
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(5)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    #添加标签
    driver.find_element(cfg.get('exam_questions', "question_Single_addlabel_by"), \
        cfg.get('exam_questions', "question_Single_addlabel")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Single_addlabeladd_by"), \
        cfg.get('exam_questions', "question_Single_addlabeladd")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Single_addlabel2_by"), \
        cfg.get('exam_questions', "question_Single_addlabel2")).send_keys(question_ansa + question_ansa)
    driver.implicitly_wait(30)
    #添加重要等级
    driver.find_element(cfg.get('exam_questions', "question_Single_important_by"), \
        cfg.get('exam_questions', "question_Single_important")).click()
    driver.implicitly_wait(30)
    #添加难度
    driver.find_element(cfg.get('exam_questions', "question_Single_difficulty_by"), \
        cfg.get('exam_questions', "question_Single_difficulty")).click()
    driver.implicitly_wait(30)
    #添加考频
    driver.find_element(cfg.get('exam_questions', "question_Single_frequency_by"), \
        cfg.get('exam_questions', "question_Single_frequency")).click()
    driver.implicitly_wait(30)
    #添加相关推荐
    driver.find_element(cfg.get('exam_questions', "question_Single_recommendation_by"), \
        cfg.get('exam_questions', "question_Single_recommendation")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    #保存
    driver.find_element(cfg.get('exam_questions', "question_save_by"), \
        cfg.get('exam_questions', "question_save")).click()
    driver.implicitly_wait(30)
    #跳转页面
    driver.find_element_by_link_text(u"单选题").click()
    driver.implicitly_wait(30)

    #创建多选题
def exam_question_Multiple(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    driver.find_element(cfg.get('exam_questions', "question_creat_by"), \
        cfg.get('exam_questions', "question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions', "question_type_by"), \
        cfg.get('exam_questions', "question_type")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_type_Multiple_by"), \
        cfg.get('exam_questions', "question_type_Multiple")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)').attr('id')")
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(2)') \
        .attr('id')")
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(3)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    #添加选项
    driver.find_element(cfg.get('exam_questions', "question_Single_addanswer_by"), \
        cfg.get('exam_questions', "question_Single_addanswer")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(4)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById(\'" + iframe_id + "\');\
    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    #保存
    driver.find_element(cfg.get('exam_questions', "question_save_by"), \
        cfg.get('exam_questions', "question_save")).click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"单选题").click()
    driver.implicitly_wait(30)

#创建是非题
def exam_question_TrueOrFalse(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    driver.find_element(cfg.get('exam_questions', "question_creat_by"), \
        cfg.get('exam_questions', "question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions', "question_type_by"), \
        cfg.get('exam_questions', "question_type")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_type_TrueOrFalse_by"), \
        cfg.get('exam_questions', "question_type_TrueOrFalse")).click()
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
        #修改答案
    driver.find_element(cfg.get('exam_questions', 'question_TrueOrFalse_changeanswer1_by'), \
                        cfg.get('exam_questions', 'question_TrueOrFalse_changeanswer1')).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', 'question_TrueOrFalse_changeanswer1_by'), \
                        cfg.get('exam_questions', 'question_TrueOrFalse_changeanswer1')).clear()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', 'question_TrueOrFalse_changeanswer1_by'), \
                        cfg.get('exam_questions', 'question_TrueOrFalse_changeanswer1')).send_keys("right")
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_save_by"), \
                        cfg.get('exam_questions', "question_save")).click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"单选题").click()
#    driver.implicitly_wait(30)

#创建问答题
def exam_question_Answer(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    driver.find_element(cfg.get('exam_questions', "question_creat_by"), \
        cfg.get('exam_questions', "question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions', "question_type_by"), \
        cfg.get('exam_questions', "question_type")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_type_Answer_by"), \
        cfg.get('exam_questions', "question_type_Answer")).click()
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(2)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_save_by"), \
        cfg.get('exam_questions', "question_save")).click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"单选题").click()

#创建填空题
def exam_question_Blank(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    driver.find_element(cfg.get('exam_questions', "question_creat_by"), \
        cfg.get('exam_questions', "question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions', "question_type_by"), \
        cfg.get('exam_questions', "question_type")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_type_Blank_by"), \
        cfg.get('exam_questions', "question_type_Blank")).click()
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Blank_by"), \
        cfg.get('exam_questions', "question_Blank")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    #添加答案
    driver.find_element(cfg.get('exam_questions', "question_Blank_1addanswer_by"), \
        cfg.get('exam_questions', "question_Blank_1addanswer")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Blank_1addanswerc_by"), \
        cfg.get('exam_questions', "question_Blank_1addanswerc")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Blank_2addanswer_by"), \
        cfg.get('exam_questions', "question_Blank_2addanswer")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Blank_2addanswerc_by"), \
        cfg.get('exam_questions', "question_Blank_2addanswerc")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    #保存
    driver.find_element(cfg.get('exam_questions', "question_save_by"), \
        cfg.get('exam_questions', "question_save")).click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"单选题").click()

#创建完型填空题
def exam_question_Cloze(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    driver.find_element(cfg.get('exam_questions', "question_creat_by"), \
        cfg.get('exam_questions', "question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions', "question_type_by"), \
        cfg.get('exam_questions', "question_type")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_type_Cloze_by"), \
        cfg.get('exam_questions', "question_type_Cloze")).click()
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze1_by"), \
        cfg.get('exam_questions', "question_Cloze1")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze2_by"), \
        cfg.get('exam_questions', "question_Cloze2")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze3_by"), \
        cfg.get('exam_questions', "question_Cloze3")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze4_by"), \
        cfg.get('exam_questions', "question_Cloze4")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    #添加选项
    driver.find_element(cfg.get('exam_questions', "question_Cloze_1addanswer_by"), \
        cfg.get('exam_questions', "question_Cloze_1addanswer")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze_1addanswerc_by"), \
        cfg.get('exam_questions', "question_Cloze_1addanswerc")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze_2addanswer_by"), \
        cfg.get('exam_questions', "question_Cloze_2addanswer")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze_2addanswerc1_by"), \
        cfg.get('exam_questions', "question_Cloze_2addanswerc1")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze_2addanswerc2_by"), \
        cfg.get('exam_questions', "question_Cloze_2addanswerc2")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze_2addanswerc3_by"), \
        cfg.get('exam_questions', "question_Cloze_2addanswerc3")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_Cloze_2addanswerc4_by"), \
        cfg.get('exam_questions', "question_Cloze_2addanswerc4")).send_keys(question_ansa)
    driver.implicitly_wait(30)
    #添加解析
    driver.find_element(cfg.get('exam_questions', "question_Cloze_analysis1_by"), \
        cfg.get('exam_questions', "question_Cloze_analysis1")).send_keys(question_ansa)
    driver.find_element(cfg.get('exam_questions', "question_Cloze_analysis_by"), \
        cfg.get('exam_questions', "question_Cloze_analysis")).send_keys(question_ansa)
    #保存
    driver.find_element(cfg.get('exam_questions', "question_save_by"), \
        cfg.get('exam_questions', "question_save")).click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"单选题").click()

#创建综合题
def exam_question_Composite(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    driver.find_element(cfg.get('exam_questions', "question_creat_by"), \
        cfg.get('exam_questions', "question_creat")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions', "question_type_by"), \
        cfg.get('exam_questions', "question_type")).click()
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_type_Composite_by"), \
        cfg.get('exam_questions', "question_type_Composite")).click()
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(0)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    #默认第一小题单选题
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(2)').attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(4)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(5)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    #添加选项
    driver.find_element(cfg.get('exam_questions', "question_Composite_Single_addanswer_by"), \
        cfg.get('exam_questions', "question_Composite_Single_addanswer")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(6)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    #添加解析
    driver.implicitly_wait(30)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(7)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    #添加第二题
    driver.find_element(cfg.get('exam_questions', "question_Composite_add_by"), \
        cfg.get('exam_questions', "question_Composite_add")).click()
    time.sleep(2)
    #第二小题多选题
    driver.find_element(cfg.get('exam_questions', "question_Composite_addtype_by"), \
        cfg.get('exam_questions', "question_Composite_addtype")).click()
    time.sleep(2)
    driver.find_element(cfg.get('exam_questions', "question_Composite_type_Multiple_by"), \
        cfg.get('exam_questions', "question_Composite_type_Multiple")).click()
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(8)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(10)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    time.sleep(2)
    iframe_id = driver.execute_script("return $('#sbjFormCon iframe:eq(11)'). \
        attr('id')")
    driver.execute_script("var element=window.document.getElementById \
        (\'" + iframe_id + "\'); \
    idocument=element.contentDocument;element=idocument.getElementById('tinymce'); \
    element.innerHTML =\'" + question_ansa + "\';")
    driver.implicitly_wait(30)
    driver.find_element(cfg.get('exam_questions', "question_save_by"), \
        cfg.get('exam_questions', "question_save")).click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"单选题").click()
    driver.implicitly_wait(30)

def auto_exam_questions(cfg, driver, base_url, question_ansa, num):
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
    driver.implicitly_wait(30)
    driver.get(base_url + "exam/")
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"试题库").click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"单选题").click()
    driver.implicitly_wait(30)
    for i in range(num):
        exam_question_Single(cfg, driver, base_url, question_ansa)
        exam_question_Multiple(cfg, driver, base_url, question_ansa)
        exam_question_TrueOrFalse(cfg, driver, base_url, question_ansa)
        exam_question_Blank(cfg, driver, base_url, question_ansa)
        exam_question_Answer(cfg, driver, base_url, question_ansa)
        exam_question_Cloze(cfg, driver, base_url, question_ansa)
        exam_question_Composite(cfg, driver, base_url, question_ansa)

def auto_exam_onequestion(cfg, driver, base_url, question_ansa, onetype):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    #onetype == 1:创建单选题
    #onetype == 2:创建多选题
    #onetype == 3:创建是非题
    #onetype == 4:创建填空题
    #onetype == 5:创建问答题
    #onetype == 6:创建完型题
    #onetype == 7:创建综合题
    driver.implicitly_wait(30)
    driver.get(base_url + "exam/")
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"试题库").click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"单选题").click()
    driver.implicitly_wait(30)
    if onetype == 1:
        exam_question_Single(cfg, driver, base_url, question_ansa)
    elif onetype == 2:
        exam_question_Multiple(cfg, driver, base_url, question_ansa)
    elif onetype == 3:
        exam_question_TrueOrFalse(cfg, driver, base_url, question_ansa)
    elif onetype == 4:
        exam_question_Blank(cfg, driver, base_url, question_ansa)
    elif onetype == 5:
        exam_question_Answer(cfg, driver, base_url, question_ansa)
    elif onetype == 6:
        exam_question_Cloze(cfg, driver, base_url, question_ansa)
    elif onetype == 7:
        exam_question_Composite(cfg, driver, base_url, question_ansa)
     