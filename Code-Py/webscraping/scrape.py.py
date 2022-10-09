#Scrape.py
import csv
import requests
from bs4 import BeautifulSoup

url = 'http://www.aalimec.ac.in/placement-details-2012-2013/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
table = soup.find('tbody')


list_of_rows = []
for row in table.findAll('tr')[1:10]:
    list_of_cells = []
    for cell in row.findAll('td')[1:10]:
        list_of_cells.append(cell)
    list_of_rows.append(list_of_cells)
    
outfile = open('./placed_students.csv', 'w', newline='')
output = csv.writer(outfile)
output.writerow(["company", "Student name", "Department"])
output.writerows(list_of_rows)
print(list_of_rows)
