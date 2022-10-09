'''Ip address should be entered at the keyboard
number of segment and lenght of each segment
'''
ip = input('Please enter the ip address: ')
length = 0
segment = 1
for a in ip:
    length = length + 1
    if a == '.':
        segment = segment + 1
        print(length-1)
        length = 0
print(length)
print('Number of Segments =', segment)
