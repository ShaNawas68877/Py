Import webbrowser
import pyautogui
import time
i = 2
while i < 57:
    time.sleep(1.5)
    webbrowser.open('https://yaseennikah.com/Home.php?PageNo='"{}"'&SStatus=%E0%AE%AE%E0%AE%A3%E0%AE%AE%E0%AE%95%E0%AE%A9%E0%AF%8D&SearchMarrital=&SearchLanguage=%E0%AE%89%E0%AE%B0%E0%AF%81%E0%AE%A4%E0%AF%81+%E0%AE%AE%E0%AF%81%E0%AE%B8%E0%AF%8D%E0%AE%B2%E0%AE%BF%E0%AE%AE%E0%AF%8D&SearchAgeMin=30&SearchAgeMax=60&SearchQualifyMin=0&SearchQualifyMax=7&SearchCity=&SearchDistance=&CallerId=Search&Key=SearchProfile'.format(i))
    i = i+1

