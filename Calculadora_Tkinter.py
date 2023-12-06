from cgitb import text
from tkinter import *
from turtle import width
from math import *

# importar la librea math si no como quieres que funcione pringao!!!


#Defino la ventana principal

ventanaPrincipal = Tk()
ventanaPrincipal.title("Calculadora")
ventanaPrincipal.iconbitmap('')
ventanaPrincipal.config(bd=1)
ventanaPrincipal.config(relief='solid')
ventanaPrincipal.geometry('560x320')
ventanaPrincipal.resizable(False,False)
ventanaPrincipal.config(bg="NavajoWhite4")

#Defino la pantalla del resultado
textoEnPantalla = StringVar()

PantallaOperaciones = Entry(ventanaPrincipal, font=("clarendon",16,"bold"),width=17 ,borderwidth=10,background="NavajoWhite1", textvariable= textoEnPantalla)
#PantallaOperaciones.grid(row=0,column=0,columnspan=6, padx=20,pady=20)
PantallaOperaciones.place(x=270,y=10)

#Vamos a definir como van a ser los botones

Bancho = 5
Balto = 2
Bcolor = "NavajoWhite3"
#boton de igual
Bigualancho = 15
Bigualalto = 2

#Vamos a hacer que funcione

operacion = "" # es la cadena
resultado = "" # es el resultado

#funcion del clear

def clear():
    global operacion # usamos la palabra clave global para cambiar la variable dentro de la funcion
    operacion = ""
    textoEnPantalla.set("0")

#funcion para recoger los botones que seleccionamos

def botonrecogido(pulsa):
    global operacion
    operacion += str(pulsa) # le decimos que concatene las pulsaciones 
    textoEnPantalla.set(operacion)

#funcion para el resultado

  
def resultado2() :
    global operacion
    global resultado
    
    if resultado != 0 :
        resultado = str(eval(operacion))
    else:
        resultado = "ERROR"
    textoEnPantalla.set(resultado)
    print(operacion,resultado)
           
    # si seguimos haciendo la operacion vamos a tener que continuar por el resultado no por la operqacion
    
  
   
""" def memoria()
    global operacion
    resultado = str(eval(operacion))
    
    textoEnPantalla.set(resultado)
    return resultado
    

def mostrarmemoria():
    global operacion
    global resultado
    resultado = memoria()
    
    textoEnPantalla.set(resultado)
    
 """

#botones numericos + clear + memoria 

Boton1 = Button(ventanaPrincipal,text="1",bg= Bcolor,width=Bancho,height=Balto,command=lambda:botonrecogido(1)).grid(row=1,column=0, padx=15, pady=10)
Boton2 = Button(ventanaPrincipal,text="2",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(2)).grid(row=1,column=1, padx=15, pady=10)
Boton3 = Button(ventanaPrincipal,text="3",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(3)).grid(row=1,column=2, padx=15, pady=10)
Boton4 = Button(ventanaPrincipal,text="4",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(4)).grid(row=2,column=0, padx=15, pady=10)
Boton5 = Button(ventanaPrincipal,text="5",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(5)).grid(row=2,column=1, padx=15, pady=10)
Boton6 = Button(ventanaPrincipal,text="6",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(6)).grid(row=2,column=2, padx=15, pady=10)
Boton7 = Button(ventanaPrincipal,text="7",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(7)).grid(row=3,column=0, padx=15, pady=10)
Boton8 = Button(ventanaPrincipal,text="8",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(8)).grid(row=3,column=1, padx=15, pady=10)
Boton9 = Button(ventanaPrincipal,text="9",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(9)).grid(row=3,column=2, padx=15, pady=10)
Botonparenizq  = Button(ventanaPrincipal,text="(",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("(")).grid(row=4,column=0, padx=15, pady=10)
Boton0 = Button(ventanaPrincipal,text="0",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("0")).grid(row=4,column=1, padx=15, pady=10)
Botonparender= Button(ventanaPrincipal,text=")",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(")")).grid(row=4,column=2, padx=15, pady=10)
#Botonrecuerda = Button(ventanaPrincipal,text="M+",bg= Bcolor,width=Bancho,height=Balto,command=lambda:memoria()).grid(row=5,column=0, padx=15, pady=10)
#Botonrenumrecordado = Button(ventanaPrincipal,text="M",bg= Bcolor,width=Bancho,height=Balto,command=lambda:mostrarmemoria()).grid(row=5,column=1, padx=15, pady=10)
Botoncoma = Button(ventanaPrincipal,text=".",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido(".")).grid(row=5,column=2, padx=15, pady=10)

#botones 100tificos + igual

Botonsumar = Button(ventanaPrincipal,text="+",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("+")).grid(row=2,column=3, padx=15, pady=10)
Botonrestar = Button(ventanaPrincipal,text="-",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("-")).grid(row=2,column=4, padx=15, pady=10)
Botonmultiplicar = Button(ventanaPrincipal,text="x",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("*")).grid(row=2,column=5, padx=15, pady=10)
Botondividir = Button(ventanaPrincipal,text="/",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("/")).grid(row=2,column=6, padx=15, pady=10)
Botonporcien = Button(ventanaPrincipal,text="%",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("%")).grid(row=3,column=3, padx=15, pady=10)

Botonseno = Button(ventanaPrincipal,text="Sen()",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("sin")).grid(row=3,column=4, padx=15, pady=10)
Botoncoseno = Button(ventanaPrincipal,text="Cos()",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("cos")).grid(row=3,column=5, padx=15, pady=10)
Botontang = Button(ventanaPrincipal,text="Tg()",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("tan")).grid(row=3,column=6, padx=15, pady=10)
BotonRaiz = Button(ventanaPrincipal,text="√",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("sqrt")).grid(row=4,column=6, padx=15, pady=10)  
Botonpi = Button(ventanaPrincipal,text="π",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("pi")).grid(row=4,column=5, padx=15, pady=10)      
Botonclear = Button(ventanaPrincipal,text="C",bg= Bcolor,width=Bancho,height=Balto,command=clear).grid(row=5,column=4, padx=15, pady=10)

BotonLog = Button(ventanaPrincipal,text="Log",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("log")).grid(row=4,column=3, padx=15, pady=10)
Botonexp = Button(ventanaPrincipal,text="EXP",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("exp")).grid(row=4,column=4, padx=15, pady=10) 
BotonLognep = Button(ventanaPrincipal,text="Log(n)",bg= Bcolor,width=Bancho,height=Balto, command=lambda:botonrecogido("ln")).grid(row=5,column=3, padx=15, pady=10) # NO FUNCIONA

Botonigual = Button(ventanaPrincipal,text=" = ",bg= Bcolor,width=Bigualancho,height=Bigualalto,command=resultado2).grid(row=5,column=5,columnspan=2, padx=15, pady=10)



ventanaPrincipal.mainloop()


