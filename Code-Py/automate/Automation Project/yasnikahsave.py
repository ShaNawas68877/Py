import pyautogui
import time
i=14
pyautogui.click(220,746)
while i < 57:
    time.sleep(1)
    pyautogui.hotkey('ctrl','s')
    time.sleep(1)
    pyautogui.typewrite('{}'.format(i))
    time.sleep(1)
    pyautogui.typewrite('\n')
    time.sleep(1)
    pyautogui.click(1139,69)
    time.sleep(1)
    pyautogui.click(1140,109)
    time.sleep(2)
    pyautogui.hotkey('ctrl','tab')
    time.sleep(1)
    i = i + 1
    time.sleep(2)
