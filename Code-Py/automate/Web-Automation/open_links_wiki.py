from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://en.wikipedia.org/wiki/Postmodernism')
for a in range(10):
    linkElem = browser.find_element_by_tag_name('a')
    #browser.get(linkElem)
    linkElem.click()

