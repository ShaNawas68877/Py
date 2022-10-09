from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https:www.facebook.com')
login = browser.find_element_by_id('email')
login.send_keys('shadotnawas@gmail.com')
pwd = browser.find_element_by_id('pass')
pwd.send_keys('Remwebdriver1!')
loginButton = browser.find_element_by_id('loginbutton')
loginButton.click()
'''
#comment = browser.find_element_by_class_name('_1p1t')
#atleast = browser.find_element_by_id('placeholder-dr5t1')
thisOne = browser.find_element_by_class_name('_5rp7')
#atleast.click()
#atleast.send_keys('Beleive me, i did not enter these words in the status update')
#comment.click()
#comment.send_keys('Beleive me, i did not enter these words in the status update')
thisOne.click()
thisOne.send_keys('Beleive me, i did not enter these words in the status update')


 '''
