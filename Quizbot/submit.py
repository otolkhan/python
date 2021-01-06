from selenium import webdriver
browser=webdriver.Chrome()
#browser open
browser.get('http://timesink.be/quizbot/index.php')
file=open("answer.txt","r")
line_vals=file.readlines()

for line in line_vals:
	answer=line.strip()
	insert=browser.find_element_by_id('insert_answer')
	insert.send_keys(answer)
	btn=browser.find_element_by_name('submit')
	btn.click()
file.close()
