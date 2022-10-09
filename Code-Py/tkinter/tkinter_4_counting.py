import tkinter as tk

counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
  
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
button1 = tk.Button(root, text='Start', width=25, command=counter_label)
counter_label(label)
button2 = tk.Button(root, text='Stop', width=25, command=root.destroy)
button1.pack()
button2.pack()
root.mainloop()
