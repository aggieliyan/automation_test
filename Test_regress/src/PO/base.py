import random


class Base():

	def __init__(self, driver):

		self.dr = driver

	def rand_name(self):
		rand_name = chr(random.randint(97, 122)) \
		+ chr(random.randint(97, 122)) + chr(random.randint(97, 122)) \
		+ str(random.randint(1000, 9999))

		return rand_name

	def datatime_name(self):
		name = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
		return name

    def is_element_present(self, how, what):
        try: self.dr.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def save_screenshot(self):
    	file_name = self.datatime_name() + '.png'
    	driver.save_screenshot(r"C://test_rs_pic//"+filename)