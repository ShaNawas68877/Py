import pyautogui
import time
n = 'Meeeeee*Tooooo'
m = len(n)/2
o = int(float(m))
##print(o)
time.sleep(2)
pyautogui.click(502,695)
for i in range(0,len(n)):
    time.sleep(0.2)
    if i<o:
        time.sleep(0.2)
        pyautogui.press('space', presses = i)
        pyautogui.typewrite(n[i])
        pyautogui.typewrite('\n')
    else:
        time.sleep(0.2)
        pyautogui.press('space', presses =((o*2)-i))
        pyautogui.typewrite(n[i])
        pyautogui.typewrite('\n')


##    if i<o:
##        time.sleep(0.2)
##        pyautogui.typewrite(' '*i+n[i])
##        pyautogui.typewrite('\n')
##    else:
##        time.sleep(0.2)
##        pyautogui.typewrite(' '* ((o*2)-i)+n[i])
##        pyautogui.typewrite('\n')
