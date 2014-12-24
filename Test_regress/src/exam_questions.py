# -*- coding: UTF-8 -*-
Created on Dec. 24, 2014
@author:liuhongjiao


import time
from selenium.webdriver.common.keys import Keys
from PO.exam_questions_page import QuestionListPage
from PO.exam_questions_page import QuestionInputPage

def import_questions(cfg, driver, template):
    questionlist = QuestionListPage(driver, cfg)
    questionlist.open()
    questionlist.click_import_questions(template)
    
#创建单选题
def exam_question_single(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.save_screenshot()
    question.input_question_name(question_ansa)
    question.add_music()
    question.input_answera(question_ansa)
    question.input_answerb(question_ansa)
    question.save_screenshot()
    question.click_question_save()

    #创建多选题
def exam_question_multiple(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.save_screenshot()
    question.click_question_type()
    question.click_question_multiple()
    question.input_question_name(question_ansa)
    question.input_answera(question_ansa)
    question.input_answerb(question_ansa)
    question.save_screenshot()
    question.click_question_save()

#创建是非题
def exam_question_trueOrFalse(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.save_screenshot()
    question.click_question_type()
    question.click_question_trueOrFalse()
    question.input_question_name(question_ansa)
    question.save_screenshot()
    question.click_question_save()
#    driver.implicitly_wait(30)

#创建问答题
def exam_question_answer(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.save_screenshot()
    question.click_question_type()
    question.click_question_answer()
    question.input_question_name(question_ansa)
    question.input_answer_answer(question_ansa)
    question.save_screenshot()
    question.click_question_save()
#创建填空题
def exam_question_blank(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.save_screenshot()
    question.click_question_type()
    question.click_question_blank()
    question.input_question_name(question_ansa)
    question.input_blank_answer(question_ansa)
    question.save_screenshot()
    question.click_question_save()

#创建完型填空题
def exam_question_cloze(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.save_screenshot()
    question.click_question_type()
    question.click_question_cloze()
    question.input_question_name(question_ansa)
    question.input_cloze1(question_ansa)
    question.input_cloze2(question_ansa)
    question.input_cloze3(question_ansa)
    question.input_cloze4(question_ansa)
    question.save_screenshot()
    question.click_question_save()

#创建综合题
def exam_question_composite(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.save_screenshot()
    question.click_question_type()
    question.click_question_composite()
    question.input_question_name(question_ansa)
    question.input_composite_name(question_ansa)
    question.input_answera(question_ansa)
    question.input_answerb(question_ansa)
    question.save_screenshot()
    question.click_question_save()

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
    questionlist = QuestionListPage(driver, cfg)
    questionlist.open()
    questionlist.save_screenshot()
    for i in range(num):
        exam_question_single(cfg, driver, base_url, question_ansa)
        exam_question_multiple(cfg, driver, base_url, question_ansa)
        exam_question_trueOrFalse(cfg, driver, base_url, question_ansa)
        exam_question_blank(cfg, driver, base_url, question_ansa)
        exam_question_answer(cfg, driver, base_url, question_ansa)
        exam_question_cloze(cfg, driver, base_url, question_ansa)
        exam_question_composite(cfg, driver, base_url, question_ansa)

def auto_exam_onequestion(cfg, driver, base_url, question_ansa, onetype):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    #onetype == 1:创建单选题
    #onetype == 2:创建多选题
    #onetype == 3:创建是非题
    #onetype == 4:创建填空题
    #onetype == 5:创建问答题
    #onetype == 6:创建完型题
    #onetype == 7:创建综合题
    questionlist = QuestionListPage(driver, cfg)
    questionlist.open()
    questionlist.save_screenshot()
    if onetype == 1:
        exam_question_single(cfg, driver, base_url, question_ansa)
    elif onetype == 2:
        exam_question_multiple(cfg, driver, base_url, question_ansa)
    elif onetype == 3:
        exam_question_trueOrFalse(cfg, driver, base_url, question_ansa)
    elif onetype == 4:
        exam_question_blank(cfg, driver, base_url, question_ansa)
    elif onetype == 5:
        exam_question_answer(cfg, driver, base_url, question_ansa)
    elif onetype == 6:
        exam_question_cloze(cfg, driver, base_url, question_ansa)
    elif onetype == 7:
        exam_question_composite(cfg, driver, base_url, question_ansa)
     