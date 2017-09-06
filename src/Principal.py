from Formula import *
from Tabla import *
from Tkinter import *
import os
import types

class Interfaz(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.pack(fill=BOTH, expand=True)
        self.creaContenido()
        self.oponentes()

    def creaContenido(self):
        w = Label(self, text="Calculemos tu rating:",font=10)
        w.place(x=170,y=10)

        ganados = IntVar()
        w = Label(self, text="Numero de partidas ganadas:")
        w.place(x=0,y=60)
        gan = Entry(self, textvariable=ganados)
        gan.place(x=230,y=60)

        self.totales = IntVar()
        w = Label(self, text="Numero de partidas jugadas:")
        w.place(x=0,y=90)
        tot = Entry(self, textvariable=self.totales)
        tot.place(x=230,y=90)

        self.ratingJ = IntVar()
        w = Label(self, text="Tu rating actual:")
        w.place(x=0,y=120)
        jug = Entry(self, textvariable=self.ratingJ)
        jug.place(x=230,y=120)

        self.ratingP = IntVar()
        w = Label(self, text="El rating promedio de tus contrincates")
        w.place(x=0,y=150)
        self.prom = Entry(self, textvariable=self.ratingP)
        self.prom.place(x=230,y=150)

        """
        Opciones para escoger constante
        """
        self.k = IntVar()
        w = Label(self, text="Constante actual:")
        w.place(x=0,y=180)

        op1 = Radiobutton(self, text="10", variable=self.k, value=10)
        op1.place(x=220,y=180)
        op2 = Radiobutton(self, text="15", variable=self.k, value=15)
        op2.place(x=260,y=180)        
        op3 = Radiobutton(self, text="25", variable=self.k, value=25)
        op3.place(x=300,y=180)

        button = Button(self, text="Calcular rating", command= lambda: self.calculaRating(ganados,self.totales,self.ratingJ,self.ratingP,self.k))
        button.place(x=390,y=60)

        salir = Button(self,text="Salir", command= self.salir)
        salir.place(x=390,y=100)

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

    def oponentes(self):
        
        """
        Rating de los oponentes del torneo para obtener el promedio
        """
        w = Label(self, text="Ratings de los oponentes",font=10)
        w.place(x=150,y=330)

        self.j1 = IntVar()
        w = Label(self, text="1)")
        w.place(x=0,y=370)
        self.je1 = Entry(self, textvariable=self.j1,width=5)
        self.je1.place(x=25,y=370)

        self.j2 = IntVar()
        w = Label(self, text="2)")
        w.place(x=0,y=400)
        je2 = Entry(self, textvariable=self.j2,width=5)
        je2.place(x=25,y=400)

        self.j3 = IntVar()
        w = Label(self, text="3)")
        w.place(x=0,y=430)
        je3 = Entry(self, textvariable=self.j3,width=5)
        je3.place(x=25,y=430)

        self.j4 = IntVar()
        w = Label(self, text="4)")
        w.place(x=0,y=460)
        je4 = Entry(self, textvariable=self.j4,width=5)
        je4.place(x=25,y=460)

        self.j5 = IntVar()
        w = Label(self, text="5)")
        w.place(x=80,y=370)
        je5 = Entry(self, textvariable=self.j5,width=5)
        je5.place(x=105,y=370)

        self.j6 = IntVar()
        w = Label(self, text="6)")
        w.place(x=80,y=400)
        je6 = Entry(self, textvariable=self.j6,width=5)
        je6.place(x=105,y=400)

        self.j7 = IntVar()
        w = Label(self, text="7)")
        w.place(x=80,y=430)
        je7 = Entry(self, textvariable=self.j7,width=5)
        je7.place(x=105,y=430)

        self.j8 = IntVar()
        w = Label(self, text="8)")
        w.place(x=80,y=460)
        je8 = Entry(self, textvariable=self.j8,width=5)
        je8.place(x=105,y=460)

        self.j9 = IntVar()
        w = Label(self, text="9)")
        w.place(x=160,y=370)
        je9 = Entry(self, textvariable=self.j9,width=5)
        je9.place(x=185,y=370)

        self.j10 = IntVar()
        w = Label(self, text="10)")
        w.place(x=160,y=400)
        je7 = Entry(self, textvariable=self.j10,width=5)
        je7.place(x=185,y=400)

        self.j11 = IntVar()
        w = Label(self, text="11)")
        w.place(x=160,y=430)
        je11 = Entry(self, textvariable=self.j11,width=5)
        je11.place(x=185,y=430)

        self.j12 = IntVar()
        w = Label(self, text="12)")
        w.place(x=160,y=460)
        je12 = Entry(self, textvariable=self.j12,width=5)
        je12.place(x=185,y=460)

        self.j13 = IntVar()
        w = Label(self, text="13)")
        w.place(x=240,y=370)
        je13 = Entry(self, textvariable=self.j13,width=5)
        je13.place(x=265,y=370)

        self.j14 = IntVar()
        w = Label(self, text="14)")
        w.place(x=240,y=400)
        je14 = Entry(self, textvariable=self.j14,width=5)
        je14.place(x=265,y=400)

        self.j15 = IntVar()
        w = Label(self, text="15)")
        w.place(x=240,y=430)
        je15 = Entry(self, textvariable=self.j15,width=5)
        je15.place(x=265,y=430)

        self.j16 = IntVar()
        w = Label(self, text="16)")
        w.place(x=240,y=460)
        je16 = Entry(self, textvariable=self.j16,width=5)
        je16.place(x=265,y=460)

        self.j17 = IntVar()
        w = Label(self, text="17)")
        w.place(x=320,y=370)
        je17 = Entry(self, textvariable=self.j17,width=5)
        je17.place(x=345,y=370)

        self.j18 = IntVar()
        w = Label(self, text="18)")
        w.place(x=320,y=400)
        je18 = Entry(self, textvariable=self.j18,width=5)
        je18.place(x=345,y=400)

        self.j19 = IntVar()
        w = Label(self, text="19)")
        w.place(x=320,y=430)
        je19 = Entry(self, textvariable=self.j19,width=5)
        je19.place(x=345,y=430)

        self.j20 = IntVar()
        w = Label(self, text="20)")
        w.place(x=320,y=460)
        je20 = Entry(self, textvariable=self.j20,width=5)
        je20.place(x=345,y=460)

        self.j21 = IntVar()
        w = Label(self, text="21)")
        w.place(x=400,y=370)
        je21 = Entry(self, textvariable=self.j21,width=5)
        je21.place(x=425,y=370)

        button = Button(self, text="Promedio", command= lambda: self.calculaPromedio(self.j1,self.j2,self.j3,self.j4,self.j5,self.j6,self.j7,self.j8,self.j9,self.j10,self.j11,self.j12,self.j13,self.j14,self.j15,self.j16,self.j17,self.j18,self.j19,self.j20,self.j21))
        button.place(x=400,y=452)

    def calculaPromedio(self,j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20,j21):
        promedio = 0
        sumaPromedio = 0
        self.j1 = j1.get()
        self.j2 = j2.get()
        self.j3 = j3.get()
        self.j4 = j4.get()
        self.j5 = j5.get()
        self.j6 = j6.get()
        self.j7 = j7.get()
        self.j8 = j8.get()
        self.j9 = j9.get()
        self.j10 = j10.get()
        self.j11 = j11.get()
        self.j12 = j12.get()
        self.j13 = j13.get()
        self.j14 = j14.get()
        self.j15 = j15.get()
        self.j16 = j16.get()
        self.j17 = j17.get()
        self.j18 = j18.get()
        self.j19 = j19.get()
        self.j20 = j20.get()
        self.j21 = j21.get()

        if(self.j1 == 0):
            pass
        else:
            sumaPromedio += self.j1
            promedio += 1

        if(self.j2 == 0):
            pass
        else:
            sumaPromedio += self.j2
            promedio += 1

        if(self.j3 == 0):
            pass
        else:
            sumaPromedio += self.j3
            promedio += 1

        if(self.j4 == 0):
            pass
        else:
            sumaPromedio += self.j4
            promedio += 1
        
        if(self.j5 == 0):
            pass
        else:
            sumaPromedio += self.j5
            promedio += 1
        
        if(self.j6 == 0):
            pass
        else:
            sumaPromedio += self.j6
            promedio += 1

        if(self.j7 == 0):
            pass
        else:
            sumaPromedio += self.j7
            promedio += 1

        if(self.j8 == 0):
            pass
        else:
            sumaPromedio += self.j8
            promedio += 1

        if(self.j9 == 0):
            pass
        else:
            sumaPromedio += self.j9
            promedio += 1
        
        if(self.j10 == 0):
            pass
        else:
            sumaPromedio += self.j10
            promedio += 1

        if(self.j11 == 0):
            pass
        else:
            sumaPromedio += self.j11
            promedio += 1

        if(self.j12 == 0):
            pass
        else:
            sumaPromedio += self.j12
            promedio += 1

        if(self.j13 == 0):
            pass
        else:
            sumaPromedio += self.j13
            promedio += 1

        if(self.j14 == 0):
            pass
        else:
            sumaPromedio += self.j14
            promedio += 1
        
        if(self.j15 == 0):
            pass
        else:
            sumaPromedio += self.j15
            promedio += 1
        
        if(self.j16 == 0):
            pass
        else:
            sumaPromedio += self.j16
            promedio += 1

        if(self.j17 == 0):
            pass
        else:
            sumaPromedio += self.j17
            promedio += 1

        if(self.j18 == 0):
            pass
        else:
            sumaPromedio += self.j18
            promedio += 1

        if(self.j19 == 0):
            pass
        else:
            sumaPromedio += self.j19
            promedio += 1
        
        if(self.j20 == 0):
            pass
        else:
            sumaPromedio += self.j20
            promedio += 1

        if(self.j21 == 0):
            pass
        else:
            sumaPromedio += self.j21
            promedio += 1

        ratingP = sumaPromedio/promedio
        self.prom.delete(0,END)
        self.prom.insert(0,ratingP)
        
    def calculaRating(self,ganados,totales,ratingJ,ratingP,constante):
        ganados = ganados.get()
        totales = totales.get()
        ratingJ = ratingJ.get()
        ratingP = ratingP.get()
        k = constante.get()
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

