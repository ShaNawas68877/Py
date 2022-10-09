#Writing text files

cities = ["Adelaide","Alice springs", "Darwin", "Melbourne", "Sydney"]

with open("C:\\Users\\Shanawas\\Desktop\\cities.txt",'w') as city_file:
    for city in cities:
        print(city, file=city_file, flush=True)#flush to remove the buffer immediately which would slow down the writing process
'''
cities = []
with open("cities.txt",'r') as city_file:
    for city in city_file:
        cities.append(city)

print(cities)
for city in cities:
    print(city)

'''

#print("Adelaide".strip('A'))#strip removes the character only from beginning or end

'''
imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"),(2, "Psycho"),(3,"Mayhem"),(4,"Kentish Town Waltz"))
with open("imelda.txt",'w') as imelda_file:
    print(imelda, file=imelda_file)

'''

with open("imelda.txt",'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year) #eval pulls data out of tuple but effectively only within a program so external pull is not good as its leaves vulns
