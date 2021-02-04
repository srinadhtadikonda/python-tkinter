from tkinter import *
root = Tk()

def var_states():
   print("DCA: %d,\nJAVA: %d,\nPYTHON: %d" % (var1.get(), var2.get(),var3.get()))

Label(root, text="Your Course:").grid(row=0, sticky=W)

var1 = IntVar()
Checkbutton(root, text="DCA", variable=var1).grid(row=1, sticky=W)

var2 = IntVar()
Checkbutton(root, text="JAVA", variable=var2).grid(row=2, sticky=W)


var3 = IntVar()
Checkbutton(root, text="PYTHON", variable=var3).grid(row=3, sticky=W)

Button(root, text='Quit', command=quit).grid(row=4, sticky=W, pady=4)
Button(root, text='Show', command=var_states).grid(row=5, sticky=W, pady=4)
mainloop()
