from tkinter import *

#akna seaded
aken = Tk()
aken.title("Mirko")
aken.configure()
#aken.iconbitmap('favicon.ico')
aken.resizable(0,0)
aken.geometry("200x200")

#tekst
tekst = Label(aken, text="Siia kunagi vastus!",padx=10,pady=10,font="Tahoma 12")
tekst.grid(row=0, column=0, columnspan=4)

#1
nupp1 = Button(aken, text="7", width=4)
nupp1.grid(row=1, column=0,padx=2,pady=2)
nupp2 = Button(aken, text="8", width=4)
nupp2.grid(row=1, column=1,padx=2,pady=2)
nupp3 = Button(aken, text="9", width=4)
nupp3.grid(row=1, column=2,padx=2,pady=2)
nupp3 = Button(aken, text="/", width=4)
nupp3.grid(row=1, column=3,padx=2,pady=2)

#2
nupp4 = Button(aken, text="4", width=4)
nupp4.grid(row=2, column=0,padx=2,pady=2)
nupp5 = Button(aken, text="5", width=4)
nupp5.grid(row=2, column=1,padx=2,pady=2)
nupp6 = Button(aken, text="6", width=4)
nupp6.grid(row=2, column=2,padx=2,pady=2)
nupp7 = Button(aken, text="*", width=4)
nupp7.grid(row=2, column=3,padx=2,pady=2)

#3
nupp8 = Button(aken, text="4", width=4)
nupp8.grid(row=3, column=0,padx=2,pady=2)
nupp9 = Button(aken, text="5", width=4)
nupp9.grid(row=3, column=1,padx=2,pady=2)
nupp10 = Button(aken, text="6", width=4)
nupp10.grid(row=3, column=2,padx=2,pady=2)
nupp11 = Button(aken, text="*", width=4)
nupp11.grid(row=3, column=3,padx=2,pady=2)

#4
nupp12 = Button(aken, text="1", width=4)
nupp12.grid(row=4, column=0,padx=2,pady=2)
nupp13 = Button(aken, text="2", width=4)
nupp13.grid(row=4, column=1,padx=2,pady=2)
nupp14 = Button(aken, text="3", width=4)
nupp14.grid(row=4, column=2,padx=2,pady=2)
nupp15 = Button(aken, text="-", width=4)
nupp15.grid(row=4, column=3,padx=2,pady=2)

#5
nupp16 = Button(aken, text="0", width=4)
nupp16.grid(row=4, column=0,padx=2,pady=2)
nupp17 = Button(aken, text=",", width=4)
nupp17.grid(row=4, column=1,padx=2,pady=2)
nupp18 = Button(aken, text="=", width=4)
nupp18.grid(row=4, column=2,padx=2,pady=2)
nupp19 = Button(aken, text="+", width=4)
nupp19.grid(row=4, column=3,padx=2,pady=2)


aken.mainloop()