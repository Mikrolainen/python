from tkinter import *

#akna seaded
aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.configure(background='white')
#aken.iconbitmap('favicon.ico')
aken.geometry("400x250")
aken.resizable(0,0)

#tekst
tekst1 = Label(aken, text="Hind käibemaksuta:", font="Tahoma 16",bg="white")
tekst1.grid(row= 0,column= 0)

tekst2 = Label(aken, text="Käibemaksumäär:", font="Tahoma 16",bg="white")
tekst2.grid(row= 1,column= 0)

tekst3 = Label(aken, text="____________________", font="Tahoma 16",bg="white")
tekst3.grid(row= 2)

tekst4 = Label(aken, text="Käibemaks:", font="Tahoma 16",bg="white")
tekst4.grid(row= 3,column= 0)

tekst5 = Label(aken, text="Käibemaksumäär:", font="Tahoma 16",bg="white")
tekst5.grid(row= 4,column= 0)

def naita_valikut():
    print(var.get())

var = IntVar()

valikukast = Radiobutton(aken,text="9%", variable=var, value=1, command=naita_valikut)
valikukast.grid(row=1,column= 1)

valikukast = Radiobutton(aken,text="20%", variable=var, value=2, command=naita_valikut)
valikukast.grid(row=1,column= 2)



aken.mainloop()