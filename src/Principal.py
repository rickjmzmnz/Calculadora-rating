from Formula import *
from Tabla import *
from Tkinter import *
import os
import types

class Interfaz(Frame):

    """
    Constructor de la clase
    Crea la ventana principal
    Las cajas de texto, etiquetas y botones
    """
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.pack(fill=BOTH, expand=True)
        self.creaContenido()
        self.oponentes()

    """
    Funcion para crear las cajas de texto para introducir los datos necesarios para calcular el rating
    Las etiques que indican que valores introducir y los botones
    """
    def creaContenido(self):
        w = Label(self, text="Calculemos tu rating:",font=10)
        w.place(x=170,y=10)

        ganados = IntVar()
        w = Label(self, text="Numero de partidas ganadas:")
        w.place(x=0,y=60)
        self.gan = Entry(self, textvariable=ganados)
        self.gan.place(x=230,y=60)

        totales = IntVar()
        w = Label(self, text="Numero de partidas jugadas:")
        w.place(x=0,y=90)
        self.tot = Entry(self, textvariable=totales)
        self.tot.place(x=230,y=90)

        ratingJ = IntVar()
        w = Label(self, text="Tu rating actual:")
        w.place(x=0,y=120)
        self.jug = Entry(self, textvariable=ratingJ)
        self.jug.place(x=230,y=120)

        ratingP = IntVar()
        w = Label(self, text="El rating promedio de tus contrincates")
        w.place(x=0,y=150)
        self.prom = Entry(self, textvariable=ratingP)
        self.prom.place(x=230,y=150)

        """
        Opciones para escoger constante
        """
        k = IntVar()
        w = Label(self, text="Constante actual:")
        w.place(x=0,y=180)

        op1 = Radiobutton(self, text="10", variable=k, value=10)
        op1.place(x=220,y=180)
        op2 = Radiobutton(self, text="15", variable=k, value=15)
        op2.place(x=260,y=180)        
        op3 = Radiobutton(self, text="25", variable=k, value=25)
        op3.place(x=300,y=180)

        button = Button(self, text="Calcular rating", command= lambda: self.calculaRating(ganados,totales,ratingJ,ratingP,k))
        button.place(x=390,y=60)

        limpiar = Button(self, text="Limpiar", command = self.limpiarDatos)
        limpiar.place(x=390, y=100)

        salir = Button(self,text="Salir", command= self.salir)
        salir.place(x=390,y=140)

        w = Label(self, text="------------------------------------------------------------------------------------------------------------------------------")
        w.place(x=0,y=210)

        w = Label(self,text="Rating nuevo:")
        w.place(x=0,y=230)
        self.nuevo = Label(self)
        self.nuevo.place(x=100,y=230)

        w = Label(self,text="Diferencia:")
        w.place(x=0,y=260)
        self.dife = Label(self)
        self.dife.place(x=100,y=260)
        
        w = Label(self,text="Performance:")
        w.place(x=0,y=290)
        self.perfo = Label(self)
        self.perfo.place(x=100,y=290)

        w = Label(self, text="------------------------------------------------------------------------------------------------------------------------------")
        w.place(x=0,y=310)

    """
    Funcion para construir las cajas de texto para introducir el rating de los oponentes
    Con el fin de hacer el rating promedio
    """
    def oponentes(self):
        
        """
        Rating de los oponentes del torneo para obtener el promedio
        """
        w = Label(self, text="Ratings de los oponentes",font=10)
        w.place(x=150,y=330)

        j1 = IntVar()
        w = Label(self, text="1)")
        w.place(x=0,y=370)
        self.je1 = Entry(self, textvariable=j1,width=5)
        self.je1.place(x=25,y=370)

        j2 = IntVar()
        w = Label(self, text="2)")
        w.place(x=0,y=400)
        self.je2 = Entry(self, textvariable=j2,width=5)
        self.je2.place(x=25,y=400)

        j3 = IntVar()
        w = Label(self, text="3)")
        w.place(x=0,y=430)
        self.je3 = Entry(self, textvariable=j3,width=5)
        self.je3.place(x=25,y=430)

        j4 = IntVar()
        w = Label(self, text="4)")
        w.place(x=0,y=460)
        self.je4 = Entry(self, textvariable=j4,width=5)
        self.je4.place(x=25,y=460)

        j5 = IntVar()
        w = Label(self, text="5)")
        w.place(x=80,y=370)
        self.je5 = Entry(self, textvariable=j5,width=5)
        self.je5.place(x=105,y=370)

        j6 = IntVar()
        w = Label(self, text="6)")
        w.place(x=80,y=400)
        self.je6 = Entry(self, textvariable=j6,width=5)
        self.je6.place(x=105,y=400)

        j7 = IntVar()
        w = Label(self, text="7)")
        w.place(x=80,y=430)
        self.je7 = Entry(self, textvariable=j7,width=5)
        self.je7.place(x=105,y=430)

        j8 = IntVar()
        w = Label(self, text="8)")
        w.place(x=80,y=460)
        self.je8 = Entry(self, textvariable=j8,width=5)
        self.je8.place(x=105,y=460)

        j9 = IntVar()
        w = Label(self, text="9)")
        w.place(x=160,y=370)
        self.je9 = Entry(self, textvariable=j9,width=5)
        self.je9.place(x=185,y=370)

        j10 = IntVar()
        w = Label(self, text="10)")
        w.place(x=160,y=400)
        self.je10 = Entry(self, textvariable=j10,width=5)
        self.je10.place(x=185,y=400)

        j11 = IntVar()
        w = Label(self, text="11)")
        w.place(x=160,y=430)
        self.je11 = Entry(self, textvariable=j11,width=5)
        self.je11.place(x=185,y=430)

        j12 = IntVar()
        w = Label(self, text="12)")
        w.place(x=160,y=460)
        self.je12 = Entry(self, textvariable=j12,width=5)
        self.je12.place(x=185,y=460)

        j13 = IntVar()
        w = Label(self, text="13)")
        w.place(x=240,y=370)
        self.je13 = Entry(self, textvariable=j13,width=5)
        self.je13.place(x=265,y=370)

        j14 = IntVar()
        w = Label(self, text="14)")
        w.place(x=240,y=400)
        self.je14 = Entry(self, textvariable=j14,width=5)
        self.je14.place(x=265,y=400)

        j15 = IntVar()
        w = Label(self, text="15)")
        w.place(x=240,y=430)
        self.je15 = Entry(self, textvariable=j15,width=5)
        self.je15.place(x=265,y=430)

        j16 = IntVar()
        w = Label(self, text="16)")
        w.place(x=240,y=460)
        self.je16 = Entry(self, textvariable=j16,width=5)
        self.je16.place(x=265,y=460)

        j17 = IntVar()
        w = Label(self, text="17)")
        w.place(x=320,y=370)
        self.je17 = Entry(self, textvariable=j17,width=5)
        self.je17.place(x=345,y=370)

        j18 = IntVar()
        w = Label(self, text="18)")
        w.place(x=320,y=400)
        self.je18 = Entry(self, textvariable=j18,width=5)
        self.je18.place(x=345,y=400)

        j19 = IntVar()
        w = Label(self, text="19)")
        w.place(x=320,y=430)
        self.je19 = Entry(self, textvariable=j19,width=5)
        self.je19.place(x=345,y=430)

        j20 = IntVar()
        w = Label(self, text="20)")
        w.place(x=320,y=460)
        self.je20 = Entry(self, textvariable=j20,width=5)
        self.je20.place(x=345,y=460)

        j21 = IntVar()
        w = Label(self, text="21)")
        w.place(x=400,y=370)
        self.je21 = Entry(self, textvariable=j21,width=5)
        self.je21.place(x=425,y=370)

        button = Button(self, text="Promedio", command= lambda: self.calculaPromedio(j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20,j21))
        button.place(x=400,y=412)

        limpiar = Button(self, text="Limpiar", command = self.limpiarRatings)
        limpiar.place(x=400,y=452)

    """
    Calcula el promedio de los oponentes 
    Solo calcula los valores distintos de cero 
    """
    def calculaPromedio(self,j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20,j21):
        promedio = 0
        sumaPromedio = 0
        j1 = j1.get()
        j2 = j2.get()
        j3 = j3.get()
        j4 = j4.get()
        j5 = j5.get()
        j6 = j6.get()
        j7 = j7.get()
        j8 = j8.get()
        j9 = j9.get()
        j10 = j10.get()
        j11 = j11.get()
        j12 = j12.get()
        j13 = j13.get()
        j14 = j14.get()
        j15 = j15.get()
        j16 = j16.get()
        j17 = j17.get()
        j18 = j18.get()
        j19 = j19.get()
        j20 = j20.get()
        j21 = j21.get()

        if(j1 == 0):
            pass
        else:
            sumaPromedio += j1
            promedio += 1

        if(j2 == 0):
            pass
        else:
            sumaPromedio += j2
            promedio += 1

        if(j3 == 0):
            pass
        else:
            sumaPromedio += j3
            promedio += 1

        if(j4 == 0):
            pass
        else:
            sumaPromedio += j4
            promedio += 1
        
        if(j5 == 0):
            pass
        else:
            sumaPromedio += j5
            promedio += 1
        
        if(j6 == 0):
            pass
        else:
            sumaPromedio += j6
            promedio += 1

        if(j7 == 0):
            pass
        else:
            sumaPromedio += j7
            promedio += 1

        if(j8 == 0):
            pass
        else:
            sumaPromedio += j8
            promedio += 1

        if(j9 == 0):
            pass
        else:
            sumaPromedio += j9
            promedio += 1
        
        if(j10 == 0):
            pass
        else:
            sumaPromedio += j10
            promedio += 1

        if(j11 == 0):
            pass
        else:
            sumaPromedio += j11
            promedio += 1

        if(j12 == 0):
            pass
        else:
            sumaPromedio += j12
            promedio += 1

        if(j13 == 0):
            pass
        else:
            sumaPromedio += j13
            promedio += 1

        if(j14 == 0):
            pass
        else:
            sumaPromedio += j14
            promedio += 1
        
        if(j15 == 0):
            pass
        else:
            sumaPromedio += j15
            promedio += 1
        
        if(j16 == 0):
            pass
        else:
            sumaPromedio += j16
            promedio += 1

        if(j17 == 0):
            pass
        else:
            sumaPromedio += j17
            promedio += 1

        if(j18 == 0):
            pass
        else:
            sumaPromedio += j18
            promedio += 1

        if(j19 == 0):
            pass
        else:
            sumaPromedio += j19
            promedio += 1
        
        if(j20 == 0):
            pass
        else:
            sumaPromedio += j20
            promedio += 1

        if(j21 == 0):
            pass
        else:
            sumaPromedio += j21
            promedio += 1

        ratingP = sumaPromedio/promedio
        self.prom.delete(0,END)
        self.prom.insert(0,ratingP)

    """
    Ventana emergente 
    Aparece si algun valor de las cajas de texto es igual a cero
    """
    def valoresCero(self):
        top = Toplevel()

        w = Label(top, text="No puedes dejar valores en cero", font=15)
        w.pack()

    """
    Ventana emergente
    Aparece si el numero de partidas ganadas es mayor al total de partidas
    """
    def noEsPosible(self):
        top = Toplevel()

        w = Label(top, text="No es posible que hayas ganado mas de lo que jugaste", font=15)
        w.pack()

    """
    Ventana emergente 
    Aparece si el rating es menor a 1000 o mayor a 3000
    """
    def ratingInvalido(self):
        top = Toplevel()

        w = Label(top, text="Ese rating es invalido", font=15)
        w.pack()

    """
    Funcion para poner en cero todos los valores de los datos para calcular el rating nuevo
    """
    def limpiarDatos(self):
        self.gan.delete(0,END)
        self.tot.delete(0,END)
        self.jug.delete(0,END)
        self.prom.delete(0,END)

    """
    Funcion para poner todos los valores en cero de las cajas de texto de los ratings de los oponentes
    """
    def limpiarRatings(self):
        self.je1.delete(0,END)
        self.je2.delete(0,END)
        self.je3.delete(0,END)
        self.je4.delete(0,END)
        self.je5.delete(0,END)
        self.je6.delete(0,END)
        self.je7.delete(0,END)
        self.je8.delete(0,END)
        self.je9.delete(0,END)
        self.je10.delete(0,END)
        self.je11.delete(0,END)
        self.je12.delete(0,END)
        self.je13.delete(0,END)
        self.je14.delete(0,END)
        self.je15.delete(0,END)
        self.je16.delete(0,END)
        self.je17.delete(0,END)
        self.je18.delete(0,END)
        self.je19.delete(0,END)
        self.je20.delete(0,END)
        self.je21.delete(0,END)

        self.je1.insert(0,0)
        self.je2.insert(0,0)
        self.je3.insert(0,0)
        self.je4.insert(0,0)
        self.je5.insert(0,0)
        self.je6.insert(0,0)
        self.je7.insert(0,0)
        self.je8.insert(0,0)
        self.je9.insert(0,0)
        self.je10.insert(0,0)
        self.je11.insert(0,0)
        self.je12.insert(0,0)
        self.je13.insert(0,0)
        self.je14.insert(0,0)
        self.je15.insert(0,0)
        self.je16.insert(0,0)
        self.je17.insert(0,0)
        self.je18.insert(0,0)
        self.je19.insert(0,0)
        self.je20.insert(0,0)
        self.je21.insert(0,0)
        
    """
    A partir de los valores dados en las cajas de texto
    Calcula el rating nuevo, la diferencia y el performance
    """
    def calculaRating(self,ganados,totales,ratingJ,ratingP,constante):
        ganados = ganados.get()
        totales = totales.get()
        ratingJ = ratingJ.get()
        ratingP = ratingP.get()
        k = constante.get()

        if (ganados == 0 or totales == 0 or ratingJ == 0 or ratingP == 0 or k == 0):

            self.valoresCero()

        elif (ganados > totales):

            self.noEsPosible()

        elif (ratingJ < 1000 or ratingJ > 3000 or ratingP < 1000 or ratingP > 3000):

            self.ratingInvalido()

        else:
            
            we = puntosEsperados(ganados,totales,ratingJ,ratingP)

            n = formulaRating(ratingJ,k,we)
            nuevo = str(n)
            self.nuevo.config(text=nuevo)

            d = ratingJ - ratingP
            dife = str(d)
            self.dife.config(text=dife)
        
            p = calculaDesempeno(ratingP,ganados,totales)
            perfo = str(p)
            self.perfo.config(text=perfo)
    
    def salir(self):
        os._exit(0)

"""
Funcion main
Se crea un objeto de la clase Tk
Le ponemos titulo a la ventana
Creamos un objeto de nuestra clase Filtros
Y se ejecuta el programa
"""        
if __name__  == "__main__":
    root = Tk()
    root.geometry("500x500")
    root.title("Calculadora de Rating")
    root.wm_state("normal")
    app = Interfaz(root)
    root.mainloop()

