# -*- coding: UTF-8 -*-
import time
from selenium.webdriver.common.keys import Keys
from PO.exam_questions_page import ExamQuestions

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
    ogstumanage = ExamQuestions(driver, cfg)
    ogstumanage.click_question_creat()
    ogstumanage.click_question_name(question_ansa)
    ogstumanage.click_music()
    ogstumanage.click_answerA(question_ansa)
    ogstumanage.click_answerB(question_ansa)
    ogstumanage.click_question_save()

    #创建多选题
def exam_question_Multiple(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    ogstumanage = ExamQuestions(driver, cfg)
    ogstumanage.click_question_creat()
    ogstumanage.click_question_type()
    ogstumanage.click_question_Multiple()
    ogstumanage.click_question_name(question_ansa)
    ogstumanage.click_answerA(question_ansa)
    ogstumanage.click_answerB(question_ansa)
    ogstumanage.click_question_save()

#创建是非题
def exam_question_TrueOrFalse(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    ogstumanage = ExamQuestions(driver, cfg)
    ogstumanage.click_question_creat()
    ogstumanage.click_question_type()
    ogstumanage.click_question_TrueOrFalse()
    ogstumanage.click_question_name(question_ansa)
    ogstumanage.click_question_save()
#    driver.implicitly_wait(30)

#创建问答题
def exam_question_Answer(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    ogstumanage = ExamQuestions(driver, cfg)
    ogstumanage.click_question_creat()
    ogstumanage.click_question_type()
    ogstumanage.click_question_Answer()
    ogstumanage.click_question_name(question_ansa)
    ogstumanage.click_answer_Answer(question_ansa)
    ogstumanage.click_question_save()
#创建填空题
def exam_question_Blank(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    ogstumanage = ExamQuestions(driver, cfg)
    ogstumanage.click_question_creat()
    ogstumanage.click_question_type()
    ogstumanage.click_question_Blank()
    ogstumanage.click_question_name(question_ansa)
    ogstumanage.click_Blank_answer(question_ansa)
    ogstumanage.click_question_save()

#创建完型填空题
def exam_question_Cloze(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    ogstumanage = ExamQuestions(driver, cfg)
    ogstumanage.click_question_creat()
    ogstumanage.click_question_type()
    ogstumanage.click_question_Cloze()
    ogstumanage.click_question_name(question_ansa)
    ogstumanage.click_Cloze1(question_ansa)
    ogstumanage.click_Cloze2(question_ansa)
    ogstumanage.click_Cloze3(question_ansa)
    ogstumanage.click_Cloze4(question_ansa)
    ogstumanage.click_question_save()

#创建综合题
def exam_question_Composite(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    ogstumanage = ExamQuestions(driver, cfg)
    ogstumanage.click_question_creat()
    ogstumanage.click_question_type()
    ogstumanage.click_question_Composite() 
    ogstumanage.click_question_name(question_ansa)
    ogstumanage.click_Composite_name(question_ansa)
    ogstumanage.click_answerA(question_ansa)
    ogstumanage.click_answerB(question_ansa)
    ogstumanage.click_question_save()

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
    ogstumanage = ExamQuestions(driver, cfg)
    ogstumanage.open()
    ogstumanage.click_questions()
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
    ogstumanage = ExamQuestions(driver, cfg)
    ogstumanage.open()
    ogstumanage.click_questions()
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
     