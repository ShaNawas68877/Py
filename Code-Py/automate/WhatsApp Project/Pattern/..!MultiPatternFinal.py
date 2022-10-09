import pyautogui
import time
n = 'I am here'
p = n.split(' ')
time.sleep(2)
pyautogui.click(502,695)
for j in range(0, len(p)):
    for i in range(0, len(p[j])):
        if(i != (len(p[j])-1)):
           pyautogui.typewrite(p[j][i] + '..')
        else:
           pyautogui.typewrite(p[j][i] + '..!')
