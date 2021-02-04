from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to app")
selected = StringVar()
rad1 = Radiobutton(window,text='CASH', value="cash", variable=selected)
rad2 = Radiobutton(window,text='CHEQUE', value="cheque", variable=selected)
rad3 = Radiobutton(window,text='DD', value="dd", variable=selected)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
lb1=Label(textvariable=selected).grid(column=0,row=1)
window.mainloop()