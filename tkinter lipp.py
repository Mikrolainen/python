from tkinter import *

aken = Tk()
aken.title('sodi')

#aken.ionbitmap('favicon.ico')

louend = Canvas(aken, width=700, height=500)
louend.pack()


louend.create_rectangle(0,0,710,500, fill='lightblue',width=0)
louend.create_rectangle(0,0,710,300, fill='white',width=0)
louend.create_rectangle(0,0,710,275, fill='black',width=0)
louend.create_rectangle(0,0,710,225, fill='white',width=0)
louend.create_rectangle(0,0,710,200, fill='lightblue',width=0)



aken.mainloop()

