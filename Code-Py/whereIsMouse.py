#! python3
#MouseNow.py
import sys
import os
import pyautogui
print('press ctrl+c to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x)+'Y:'+str(y)
        print(positionStr, end = '')
        print('\b', end = '', file = sys.stdout, flush = True)
except KeyboardInterrupt:
    print('\nDone')

