import webbrowser

#webbrowser.open("https://www.python.org")
##for m in dir(webbrowser):
##    print(m)
##help(webbrowser)#text based browsers available in Linux called Lynx or whatever
####
####for i in range(10):
####    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=':', end='')#123456789 are objects parameter#sep parameter to separate
####    print()
#####Print is a method and various arguments are passed

#help(webbrowser)

#webbrowser.get()

#ARGUMENTS AND PARAMETER

#ARGUMENTS' VALUE IS PARAMETER

chrome = webbrowser.get(using='google-chrome')
chrome.open_new("https://www.python.org")
