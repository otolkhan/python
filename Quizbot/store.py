#import
from selenium import webdriver
browser=webdriver.Chrome()
#browser open
browser.get('http://timesink.be/quizbot/index.php')
for i in range(1,1001):
#input
	insert=browser.find_element_by_id('insert_answer')
	insert.send_keys('test')
	btn=browser.find_element_by_name('submit')
	btn.click()
	#answer store
	answer=browser.find_element_by_id('answer')
	file=open('answer.txt','a')
	file.write(answer.text+"\n")
file.close()
