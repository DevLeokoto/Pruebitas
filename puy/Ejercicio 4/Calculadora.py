import tkinter as tk #modulo crear gui
import tkinter.ttk as ttk #modulo para crear gui mas bonitos

numero=""

def agregar_texto (x):
    global numero
    numero +=str(x)
    #texto.delete(1.0, tk.END)
    texto.insert(tk.END, numero)
    numero=""


def evalular_operacion_():
    global numero
    try:
        resultado=str(eval(texto.get(1.0, tk.END)))
        texto.delete(1.0, tk.END)
        texto.insert(1.0, resultado)
    except:
        limpieza()
        texto.insert(1.0, "Cagaste")

def limpieza():
    texto.delete(1.0, tk.END)


cal=tk.Tk() #creamos una variable que va a ser la app o la ventana de la app y donde meteremos todo

cal.title("Calculadora")
cal.configure(background="black")
#cosas que le puedo meter a la app widgets

texto=tk.Text(height=2,width=30, fg='black', bg='grey', font=24)
texto.grid(columnspan=5) 

boton=tk.Button(text="1", height=1, width=9, fg='black', bg='grey', command=lambda: agregar_texto(1))
boton.grid(row=1,column=0)

boton=tk.Button(text="2", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto(2))
boton.grid(row=1,column=1)

boton=tk.Button(text="3", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto(3))
boton.grid(row=1,column=2)

boton=tk.Button(text="4", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto(4))
boton.grid(row=2,column=0)

boton=tk.Button(text="5", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto(5))
boton.grid(row=2,column=1)

boton=tk.Button(text="6", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto(6))
boton.grid(row=2,column=2)

boton=tk.Button(text="7", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto(7))
boton.grid(row=3,column=0)

boton=tk.Button(text="8", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto(9))
boton.grid(row=3,column=1)

boton=tk.Button(text="9", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto(9))
boton.grid(row=3,column=2)

boton=tk.Button(text="+", height=1, width=7,fg='black', bg='grey', command=lambda: agregar_texto("+"))
boton.grid(row=1,column=3)

boton=tk.Button(text="-", height=1, width=7,fg='black', bg='grey', command=lambda: agregar_texto("-"))
boton.grid(row=2,column=3)

boton=tk.Button(text="X", height=1, width=7,fg='black', bg='grey', command=lambda: agregar_texto("*"))
boton.grid(row=3,column=3)

boton=tk.Button(text="/", height=1, width=7,fg='black', bg='grey', command=lambda: agregar_texto("/"))
boton.grid(row=4,column=3)

boton=tk.Button(text="(", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto("("))
boton.grid(row=4,column=0)

boton=tk.Button(text="0", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto("0"))
boton.grid(row=4,column=1)

boton=tk.Button(text=")", height=1, width=9,fg='black', bg='grey', command=lambda: agregar_texto(")"))
boton.grid(row=4,column=2)



########

boton=tk.Button(text="Clear", height=1, width=20, fg='black', bg='grey', command=lambda: limpieza())
boton.grid(row=5,column=0, columnspan=2)

boton=tk.Button(text="Resultado", height=1, width=18,fg='black', bg='grey', command=lambda: evalular_operacion_())
boton.grid(row=5,column=2, columnspan=2)


cal.mainloop() #para que no se cierre la app