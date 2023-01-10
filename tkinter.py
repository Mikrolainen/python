from tkinter import *

#akna seaded
aken = Tk()
aken.title("Mirko")
aken.configure(background='white')
#aken.iconbitmap('favicon.ico')
aken.geometry("300x300+100+100")
aken.resizable(0,0)

#tekst
Label(aken, text="Mirko Kohava", font="Tahoma 16 bold italic",bg="white").pack()
Label(aken, text="IT22", font="Tahoma 16 bold italic",bg="white").pack()
Label(aken, text="2023", font="Tahoma 16 bold italic",bg="white").pack()
aken.mainloop()