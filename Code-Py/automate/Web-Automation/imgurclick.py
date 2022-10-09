from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import pyautogui
browser = webdriver.Firefox()
browser.get('http:imgur.com')
loginn = browser.find_element_by_class_name('icon-search')
loginn.click()
loginn.send_keys('Charotte le bon')
loginn.send_keys(u'\ue007')#IT works for enter
#loginn.send_keys(ENTER)
#pyautogui.press('enter') NO PYAUTOGUI
#pwd = browser.find_element_by_id('pass')
#pwd.send_keys('Facebookpassword')
#loginButton = browser.find_element_by_id('loginbutton')

'''
press('enter')
loginButton.click()
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

