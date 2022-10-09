import tkinter

class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
def callback():
    print('Called the callback!')

root = Tk()

# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

mainloop()
largest = None

for i in range(0, 3):
    number = int(input('Enter %d integer: ' % i))
    if number % 2 != 0 and (not largest or number > largest):
        largest = number

if largest is None:
    print("You didn't enter any odd numbers")
else:
    print("Your largest odd number was:", largest)

