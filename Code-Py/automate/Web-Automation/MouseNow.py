import pyautogui
try:
    while True:
        x = pyautogui.position()
        print(x)   
except KeyboardInterrupt:
    print('\ndone')

