from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
import pyautogui
browser = webdriver.Firefox()
browser.get('https://en.wikipedia.org/wiki/Web_scraping')
all_links = browser.find_element_by_tag_name('a')
res = requests.get(all_links)
print(res.text[:250])


