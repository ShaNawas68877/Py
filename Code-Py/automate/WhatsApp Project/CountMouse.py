import pyautogui
import time
n = 'Hello there'
m = len(n)/2
o = int(float(m))
##print(o)
time.sleep(2)
pyautogui.click(502,695)
for i in range(0,len(n)):
    time.sleep(0.2)
    pyautogui.typewrite(' '*i+n[i])
    pyautogui.typewrite('\n')
    


##if i<o:
##        print(' '*i+n[i])
##    else:
##        print(' '* ((o*2)-i)+n[i])
