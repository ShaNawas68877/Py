from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.naukri.com/job-listings-Field-Sales-Executive-Sanohub-Technologies-Private-Limited-Bengaluru-Hyderabad-1-to-3-years-151018002220?src=jobsearchDesk&sid=15397091787813&xp=2&px=1')
linkElem = browser.find_element_by_link_text('viewCont_trg')
print(linkElem)
