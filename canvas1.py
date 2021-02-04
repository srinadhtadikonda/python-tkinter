from tkinter import *
root=Tk()
c=Canvas(bg="red",width="140",height="100")
line = c.create_line(0, 0, 100,100)
c.pack()
mainloop()