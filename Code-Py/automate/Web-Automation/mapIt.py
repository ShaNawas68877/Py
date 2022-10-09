import webbrowser, sys, pyperclip#pyperclip takes the string or value from clipboard
if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+address)
