import requests
from bs4 import BeautifulSoup
import csv
import urllib

url='http://www.mapsofindia.com/districts-india/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
table=soup.find('table', attrs={'class':'tableizer-table'})
list_of_rows=[]
for row in table.findAll('tr')[1:]:
    list_of_cells=[]
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)
outfile = open('./immates.csv','w', newline='')
writer=csv.writer(outfile)
writer.writerow(['SNo', 'States', 'Dist', 'Population'])
writer.writerows(list_of_rows)
print(list_of_rows)
