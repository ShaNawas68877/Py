from tkinter import *
#from tkinter import ttk
#import logging
#import datetime
master = Tk()
whatever_you_do = "Every Soul Shall Taste DEATH\n"
referene = "-Qur'an (3:185)\n"
msg = Message(master, text = whatever_you_do)
mssg = Message(master, text = referene, justify = LEFT)
msg.config(bg='white', font=('times', 20, 'bold'), relief = 'SUNKEN', fg = 'red')
mssg.config(bg='dark green', font=('times', 15, 'bold'), fg = 'white')
master.geometry = ("500*500")
msg.pack()
mssg.pack( )
mainloop( )
master.mainloop()
