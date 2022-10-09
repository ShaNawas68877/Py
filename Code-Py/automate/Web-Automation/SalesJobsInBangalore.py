import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
'''
#for div in BeautifulSoup(urlopen(
req = requests.get("https://www.naukri.com/job-listings-Urgent-Opening-Sales-marketing-Executive-in-Start-up-Food-Industry-Delight-HR-Services-Pvt-Ltd-Bengaluru-1-to-3-years-151018000790?src=jobsearchDesk&sid=15396988388035&xp=2&px=1", headers={'User-Agent': 'Mozilla/5.0'})
page = BeautifulSoup(req.content, "html.parser")
final = page.encode('utf-8')
'''
exampleFile = open('https://www.naukri.com/job-listings-Sales-Executive-Sales-Officer-JCB-Enterprises-Private-Limited-Delhi-NCR-Mumbai-Bengaluru-Chennai-Hyderabad-Pune-Kolkata-Ahmedabad-Chandigarh-1-to-5-years-121018004166?src=jobsearchDesk&sid=15396988388035&xp=1&px=1')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
v = exampleSoup.select('div #viewcontact')
#vvv = page.findAll('div', {'class':'jDisc viewContact'})
for p in v:
    print(p.text)
