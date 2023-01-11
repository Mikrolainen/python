from tkinter import *

#akna seaded
aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.configure(background='white')
#aken.iconbitmap('favicon.ico')
aken.geometry("450x200")
aken.resizable(0,0)

def arvuta():
    
    kaibe= var.get()
    arv= float(sisestus.get())
    
    vastus= arv*kaibe
    print(arv,kaibe,vastus)
    
    tekst7.config(text=str(vastus)+"€")
    
    tekst6.config(text=str(vastus+arv)+"€")
#tekstid

tekst1 = Label(aken, text="Hind käibemaksuta:", font="Tahoma 16",bg="white")
tekst1.grid(row= 0,column= 0)

tekst2 = Label(aken, text="Käibemaksumäär:", font="Tahoma 16",bg="white")
tekst2.grid(row= 1,column= 0)

tekst3 = Label(aken, text="_________________________________________", font="Tahoma 16",bg="white")
tekst3.grid(row= 2,columnspan= 4)

tekst4 = Label(aken, text="Hind käibemaksuga:", font="Tahoma 16",bg="white")
tekst4.grid(row= 4,column= 0)

tekst5 = Label(aken, text="Käibemaks", font="Tahoma 16",bg="white")
tekst5.grid(row= 3,column= 0)

tekst6 = Label(aken, text="0,00€", font="Tahoma 16",bg="white")
tekst6.grid(row= 4,column= 1)

tekst7 = Label(aken, text="0,00€", font="Tahoma 16",bg="white")
tekst7.grid(row= 3,column= 1)

#kaibemakusmaaru valik

var = DoubleVar()

valikukast1 = Radiobutton(aken,text="9%", variable=var, value=0.09)
valikukast1.grid(row=1,column= 1)

valikukast2 = Radiobutton(aken,text="20%", variable=var, value=0.2)
valikukast2.grid(row=1,column= 2)

#sisestusvali

sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

#OK nupp

nupp1 = Button(aken, text="OK", width=7, height=1,command=arvuta)
nupp1.grid(row=5, column=2)




aken.mainloop()
