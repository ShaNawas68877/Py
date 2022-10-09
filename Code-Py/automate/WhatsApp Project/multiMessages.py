import pyautogui
import time
n = 'test'
time.sleep(2)
pyautogui.click(502,695)
i = 0
while i < 25:
    pyautogui.typewrite(n)
    pyautogui.typewrite('\n')
    i += 1
    time.sleep(0.8)
