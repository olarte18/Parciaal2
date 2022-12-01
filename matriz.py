from tkinter import*
def matriz():
    j=0
    k=0
    for i in range(int(m.get())):
        
        recta=c.create_rectangle(j,k,BASE/int(m.get()),ALTURA/int(m.get()), fill="black")
        j=j+BASE/int(m.get())
        k=k+BASE/int(m.get())
    
        

        
    


BASE=480
ALTURA=240
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Matrices")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="black")

m= StringVar()
b  = StringVar()


#--------------------
#frame entrada datos
#--------------------

frame_opera = Frame(ventana_principal)
frame_opera.config(bg = "white", width = 480 , height = 220)
frame_opera.place(x = 10, y = 265)

#labels
lb_x = Label(frame_opera, text = "Orden de la matriz = ")
lb_x.config(bg="white", fg="black", font=("Arial",16))
lb_x.place(x=10, y=20,  height=30)

lb_x = Label(frame_opera, text = "buscar= ")
lb_x.config(bg="white", fg="black", font=("Arial",16))
lb_x.place(x=330, y=20,  height=30)
#entrys
valorm=Entry(frame_opera, textvariable=m )
valorm.config(font=("Arial",15), justify=LEFT,fg="black")
valorm.place(x=220, y=20,width=30)

buscar=Entry(frame_opera, textvariable=b)
buscar.config(font=("Arial",15), justify=LEFT,fg="black")
buscar.place(x=420, y=20,width=30)

#buttons
bt_crear = Button(frame_opera, text="crear" , command=matriz)
bt_crear.place(x=50, y=65, width=100, height=30)


bt_buscar = Button(frame_opera, text="buscar")
bt_buscar.place(x=300, y=65, width=100, height=30)
#creacion canvas
c = Canvas(ventana_principal, width=BASE, height=ALTURA)
c.place(x=10, y=20)


ventana_principal.mainloop()