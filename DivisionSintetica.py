from fractions import Fraction
import math
import numpy as np
from numpy.polynomial import Polynomial as P 
from tkinter import *
from tkinter import ttk
from math import *
import time
raiz=Tk()
raiz.title("Calculadora de divisiones sintéticas")
raiz.geometry("1050x580")
tituloLabel=Label(raiz,text="Calculadora De Division Sintetica", font = ("Comic Sans MS", 17, "bold"), fg = "#3d405b",bg="#81b29a", width = "250", height = "2")
tituloLabel.pack()
Frame=Frame(raiz,width="1180",height="1920",bg="#f2cc8f")
Frame.pack()

clock=Label(Frame,font=("times",30,"bold"))
entrada=StringVar()
soluciontext3 = StringVar()
soluciontext1 = StringVar()
soluciontext = StringVar()
Mostrar_Funcion= StringVar()
ecuacion=StringVar()

#todas estas lineas hacen parte de los textos utilizados para el menu principal del programa
Expli1=Label(Frame, text="La división sintética.se puede utilizar para dividir una función polinómica por un binomio de la forma x-c,Esto nos permite",font = ("Comic Sans MS", 13,"bold"),fg ="#3d405b",bg="#f2cc8f")
Expli1.place(x=20,y=95)
Expli2=Label(Frame, text="por ejemplo hallar el cociente y el resto que se obtiene al dividir el polinomio por x-c. Además, por el teorema del resto",font = ("Comic Sans MS", 13,"bold"),fg ="#3d405b",bg="#f2cc8f")
Expli2.place(x=20,y=125)
Expli3=Label(Frame, text="al aplicar la división sintética se obtiene el valor funcional del polinomio. También permite encontrar los factores y ceros",font = ("Comic Sans MS", 13,"bold"),fg ="#3d405b",bg="#f2cc8f")
Expli3.place(x=20,y=155)

Poli=Label(Frame, text="Ingrese los coeficicientes del polinomio:", font = ("Comic Sans MS",13),fg = "#3d405b",bg="#f2cc8f")
Poli.place(x=153, y=280)
Raicitas=Label(Frame,textvariable=ecuacion,text="Las raices racionales de la ecuacion polinomica ingresada son las siguientes: ", font = ("Comic Sans MS", 13),fg ="#3d405b",bg="#f2cc8f")
Raicitas.place(x=161, y=350)


##para mostrar el resultado1 
Poli2=Label(Frame, textvariable=soluciontext3, font = ("Comic Sans MS",13),fg = "#3d405b",bg="#f2cc8f")
Poli2.place(x=188, y=480)

##para mostrar el resultado1 
Poli2=Label(Frame, textvariable=soluciontext1, font = ("Comic Sans MS",13),fg = "#3d405b",bg="#f2cc8f")
Poli2.place(x=188, y=380)

##para mostrar el resultado 
Poli2=Label(Frame, textvariable=soluciontext, font = ("Comic Sans MS",13),fg = "#3d405b",bg="#f2cc8f")
Poli2.place(x=505, y=380)

#estas 2 lineas de codigo son los cuadros de texto donde los usuarios podran ingresar los coeficientes del polinomio
Coe=Entry(Frame,textvariable=entrada, font = ("Comic Sans MS", 13, "bold"),fg ="#3d405b",bg="#e07a5f",width="20")
Coe.place(x=498, y=280)

#Aqui tenemos definida una funcion para mostrar el tiempo real en el programa
def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time,font=("Comic Sans MS", 14, "bold"),fg ="#3d405b",bg="#f2cc8f")
    clock.after(1000,times)
clock.place(x=10,y=30)
times()

#esta funcion contiene todas las caractiristicas de la guia de usuario, la forma es como se podra utilizar el programa en caso que necesite ayuda
def v2():
    raiz2 = Toplevel()
    raiz2.geometry("1050x580")
    raiz2.config(bg="#f2cc8f")
    raiz2.title("Manual de usuario")
    titulo2=Label(raiz2,text="Manual se usuario", font = ("Comic Sans MS", 20, "bold"), bg ="#f2cc8f", fg = "#028174", width = "250", height = "2")
    titulo2.pack()
    ##raiz2.iconbitmap("calcu.ico")
    explicacion3=Label(raiz2, text="En el siguiente informe se muestra como se debe utilizar el software para un buen funcionamiento:", font = ("Comic Sans MS", 14),fg ="#3d405b",bg="#f2cc8f")
    explicacion3.place(x=100, y=100)
    explicacion4=Label(raiz2, text="Para que el programa muestre correctamente el resultado se debe tener en cuenta las siguientes", font = ("Comic Sans MS", 14),fg ="#3d405b",bg="#f2cc8f")
    explicacion4.place(x=100, y=135)
    explicacion41=Label(raiz2, text="recomendaciones", font = ("Comic Sans MS", 14, "bold"),fg ="#3d405b",bg="#f2cc8f")
    explicacion41.place(x=100, y=165)
    explicacion5=Label(raiz2, text="1 : Cuando valla a ingresar los datos deben estar separados por comas (,) sin ningun tipo de", font = ("Comic Sans MS", 14),fg = "#3d405b",bg="#f2cc8f")
    explicacion5.place(x=120, y=210)
    explicacion51=Label(raiz2, text="espacios ni caracteres especiales. ", font = ("Comic Sans MS", 14, "bold"),fg = "#3d405b",bg="#f2cc8f")
    explicacion51.place(x=120, y=240)
    explicacion6=Label(raiz2, text="2 : Tenga en cuenta que el algoritmo trabaja de una manera especial por lo cual debera", font = ("Comic Sans MS", 14),fg = "#3d405b",bg="#f2cc8f")
    explicacion6.place(x=120, y=280)
    explicacion61=Label(raiz2, text="ingresar los datos de manera contraria a la que es, Por ejemplo: 2x^2+3x+5 se debe ingresar de", font = ("Comic Sans MS", 14),fg = "#3d405b",bg="#f2cc8f")
    explicacion61.place(x=120, y=310)
    explicacion62=Label(raiz2, text="la forma 5,3,2", font = ("Comic Sans MS", 14,"bold"),fg = "#3d405b",bg="#f2cc8f")
    explicacion62.place(x=120, y=340)

##Aqui esta la imgen del boton, y el titulo donde dice ayuda del boton
imgBoton=PhotoImage(file="libro.png")
botonabrirventana=Button(Frame, text="guia de usuario",image=imgBoton,font = ("MS Sans Serif", 11, "bold"),command=v2,borderwidth="2",relief="flat",bg="#f2cc8f")
botonabrirventana.place(x=932,y=-25)
botonabrirventana.config(
    width="125",
    height="125"
    )
def mostrar():##esta parte del codigo obtendra y mostrara los resultados de los polinomios ingresados en la interfaz
    a = eval(entrada.get())
    p=P(a)
    print (p.roots())
    print(f"{p:unicode}")
    soluciontext1.set(f"{p:unicode}" + "       =   ")
    soluciontext.set(str(np.around(p.roots(), decimals=4)).replace('[','').replace(']','').replace('.j','').replace('j',''))
    ecuacion.set("Las raices racionales de la ecuacion polinomica "+f"{p:unicode}"+" son las siguientes: ")
    np.around(p.roots(), decimals=4)
    print(np.around(p.roots(), decimals=4))

#esta parte es el boton que el usuario utilizara para resolver las funciones polinomicas
botonEnvio=Button(Frame, text="Resolver",font = ("MS Sans Serif", 14, "bold"),fg ="#028174",bg="white", command=mostrar,borderwidth=0)
botonEnvio.place(x=748, y=272)

##------------------------Menu-----------------

menubar = Menu(raiz)                                                                     ## Creamos un menu bar donde le vamos asignar la raiz principal, diciendo que el menu va a estar en la raiz 
raiz.config(menu=menubar)                                                                ## Le damos configuraciones a ese menu 
filemenu = Menu(menubar, tearoff=0)                                                      ## y propiedades visualez tambien

def NuevoA ():                                                                           ## creamos la ventana que va a aparecer cuando se presione ese boton del menu    
    for borrar in tv.get_children():                                                     ## recorremos la tabla    
        tv.delete(borrar)                                                                ## y borramos                                                                 ## vaciamos la caja de texto de las ventanas emergentes  
filemenu.add_command(label="Nuevo Archivo",command=NuevoA)                               ## creamos el menu y le asignamos la funcion 


def AbrirA():
    print(filedialog.askopenfilename(initialdir = "/",title = "Abrir Archivo",defaultextension=".txt",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))
filemenu.add_command(label="Abrir Archivo",command=AbrirA)


def GuardarA():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Guardar Archivo",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))
filemenu.add_command(label="Guardar Archivo",command=GuardarA)


def clicked():                                                                  ## Creamos la funcion que se va a ejecutar cuando se presione el boton del menu archivo - salir 
    answer=messagebox.askyesno('Advertencia', 'Seguro que quieres salir?')
    if answer:
        raiz.destroy()
filemenu.add_command(label="Salir",command=clicked)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")
helpmenu = Menu(menubar, tearoff=0)

def VAyuda():                                                            ## Creamos la funcion que se va a ejecutar cuando se presione el boton del menu Ayuda  - ayudas
    raiz2 = Toplevel()                                                   ## Creamos una raiz de la ventana
    raiz2.geometry("1200x675")                                           ## Le damos un tamaño a esa raiz 
    raiz2.title("Ayuda De Usuario")                                      ## Le damos un titulo a esa raiz 
    raiz2.iconbitmap("libro.ico")                                        ## Le colocamos un icono a esa ventana llamada raiz

    fondoayudaq=PhotoImage(file="picasomantenimiento.gif")               ## le colocamos una imagen de fondo .gif que va a contener todo lo de esa ventana con toda la informacion
    fondo7 = Label(raiz2, image=fondoayudaq).place(x=0,y=0)
    raiz2.mainloop()                                                     ## Cerramos la parte grafica de la ventana vayuda
helpmenu.add_command(label="Ayuda",command=VAyuda)


def AcercaD():                                                           ## Creamos la funcion que se va a ejecutar cuando se presione el boton del menu Ayuda- acerca de 
    raiz3 = Toplevel()                                                   ## Creamos una raiz de la ventana
    raiz3.geometry("900x639")                                            ## Le damos un tamaño a esa raiz 
    raiz3.title("Acerca Del software")                                   ## Le damos un titulo a esa raiz 
    raiz3.iconbitmap("libro.ico")                                        ## Le colocamos un icono a esa ventana llamada raiz
 
    fondoacercad=PhotoImage(file="picasoacercade.gif")                   ## le colocamos una imagen de fondo .gif que va a contener todo lo de esa ventana con toda la informacion## le colocamos una imagen de fondo .gif que va a contener todo lo de esa ventana con toda la informacion
    fondo7 = Label(raiz3, image=fondoacercad).place(x=0,y=0)
    raiz3.mainloop()                                                     ## Cerramos la parte grafica de la ventana acercad
helpmenu.add_command(label="Acerca de...",command=AcercaD)
guiamenu = Menu(menubar, tearoff=0)

def GuiaM():                                                               ## Creamos la funcion que se va a ejecutar cuando se presione el boton del menu Guia de usuarios - guia de metodo de newton raphson 
    raiz4 = Toplevel()                                                     ## Creamos una raiz de la ventana
    raiz4.geometry("1200x675")                                             ## Le damos un tamaño a esa raiz 
    raiz4.title("Guia De Metodo Newton-Raphson")                           ## Le damos un titulo a esa raiz 
    raiz4.iconbitmap("libro.ico")                                          ## Le colocamos un icono a esa ventana llamada raiz
    raiz4.config(bg="white")                                               ## le colocamos un fondo blanco
    fondoguiame=PhotoImage(file="picasometodo2.gif")                       ## le colocamos una imagen de fondo .gif que va a contener todo lo de esa ventana con toda la informacion
    fondo7 = Label(raiz4, image=fondoguiame).place(x=0,y=0)
    raiz4.mainloop()                                                       ## Cerramos la parte grafica de la ventana guiam

def EntradaD():                                                            ## Creamos la funcion que se va a ejecutar cuando se presione el boton del menu Guia de usuarios - guia entrada de datos
    raiz6 = Toplevel()                                                     ## Creamos una raiz de la ventana
    raiz6.geometry("932x550")                                              ## Le damos un tamaño a esa raiz 
    raiz6.title("Guiar Para Entrada De Los Datos")                         ## Le damos un titulo a esa raiz 
    raiz6.iconbitmap("entradad.ico")                                       ## Le colocamos un icono a esa ventana llamada raiz
    raiz6.config(bg="white")                                               ## le colocamos un fondo blanco

    Titulodatos = Label(raiz6,text="Operadores Matematicos Para La Entrada Del Software", font = ("Comic Sans MS", 13,"bold"))
    Titulodatos.place(x=250,y=0)
    Titulodatos.config(foreground="#fa7014",bg="white")
    Definiciondatos = Label(raiz6,text="En cuanto a los operadores aritméticos, estos permiten realizar las diferentes operaciones aritméticas del álgebra: suma, resta,",font = ("Comic Sans MS", 12))
    Definiciondatos.place(x=0,y=56)
    Definiciondatos.config(bg="white")
    Definiciondatos = Label(raiz6,text="producto, división, …Estos operadores de Python son de los más utilizados. El listado completo es el siguiente:", font = ("Comic Sans MS", 12))
    Definiciondatos.place(x=0,y=80)
    Definiciondatos.config(bg="white")
    fondoentradaD=PhotoImage(file="picasotabla.gif")                             ## le colocamos una imagen de fondo .gif que va a contener todo lo de esa ventana con toda la informacion
    fondo6 = Label(raiz6, image=fondoentradaD).place(x=140,y=129)
    raiz6.mainloop()                                                             ## Cerramos la parte grafica de la ventana entradad

def AnalisisD():                                                                 ## Creamos la funcion que se va a ejecutar cuando se presione el boton del menu Guia de usuario - analisis de resultados 
    raiz7 = Toplevel()                                                           ## Creamos una raiz de la ventana
    raiz7.geometry("1200x675")                                                   ## Le damos un tamaño a esa raiz 
    raiz7.title("Analisis De Los Resultados")                                    ## Le damos un titulo a esa raiz 
    raiz7.iconbitmap("libro.ico")                                                ## Le colocamos un icono a esa ventana llamada raiz
    fondoanalisisd=PhotoImage(file="picasodatosm.gif")                             ## le colocamos una imagen de fondo .gif que va a contener todo lo de esa ventana con toda la informacion
    fondo6 = Label(raiz7, image=fondoanalisisd).place(x=0,y=0)
    raiz7.mainloop()                                                               ## Cerramos la parte grafica de la ventana analisisd

contacmenu = Menu(menubar, tearoff=0)
                                                               ## Cerramos la parte grafica de la ventana datosr
def DatosCor():                                                                         ## Creamos la funcion que se va a ejecutar cuando se presione el boton del menu contacto - correo
    raiz12 = Toplevel()                                                                 ## Creamos una raiz de la ventana
    raiz12.geometry("720x500")                                                          ## Le damos un tamaño a esa raiz 
    raiz12.title("Datos De Correo")                                                     ## Le damos un titulo a esa raiz 
    raiz12.iconbitmap("libro.ico")                                                      ## Le colocamos un icono a esa ventana llamada raiz

    fondodesa=PhotoImage(file="picasocorreo.gif")                                       ## le colocamos una imagen de fondo .gif que va a contener todo lo de esa ventana con toda la informacion
    fondo4 = Label(raiz12, image=fondodesa).place(x=0,y=0)
    raiz12.mainloop()                                                                   ## Cerramos la parte grafica de la ventana datoscor
contacmenu.add_command(label="Correo",command=DatosCor)
menubar.add_cascade(label="Archivo", menu=filemenu)                                      ## Se crea el boton de archivo en el menu 
menubar.add_cascade(label="Editar", menu=editmenu)                                       ## Se crea el boton de Editar en el menu 
menubar.add_cascade(label="Guia Usuarios", menu=guiamenu)                                ## Se crea el boton de Guia de usuarios en el menu 
menubar.add_cascade(label="Ayuda", menu=helpmenu)                                        ## Se crea el boton de Ayuda en el menu 
    
raiz.mainloop()