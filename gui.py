from re import M
import tkinter as tk
from tkinter import *
import math, time

from sympy.plotting.plot import flat
import metodos
class GUI:

    """GUI """
    window = tk.Tk()
    calcPanel = PanedWindow(orient="vertical")
    #plano=Tk() #tk.Tk()
    #plano.title("Plano")
    size=500
    #canva = tk.Canvas() # tk.Canvas(plano, width=size, height=size, bg="white")
    def __init__(self):
        """
        Crea la ventana principal
        """
        self.window.title("Metodos Numericos")
        self.main();
        self.window.mainloop()

    def main(self):
        input = Entry(self.calcPanel, font=("Arial", 20))
        input.pack(side = TOP)
        self.calcPanel.add(input)
        intervalPanel = PanedWindow(self.calcPanel,orient="horizontal") 
        intervalInf = Entry(intervalPanel, font=("Arial", 12),width=10, justify="center")
        intervalInf.insert(0, "0")
        intervalInf.pack(side = "left", expand = FALSE)
        intervalPanel.add(intervalInf)
        intervalSup = Entry(intervalPanel, font=("Arial", 12),width=10, justify="center")
        intervalSup.insert(0, "2")
        intervalSup.pack(side = "right", expand = FALSE)
        intervalPanel.add(intervalSup)
        errorEsperado= Entry(intervalPanel, font=("Arial", 12),width=10, justify="center")
        errorEsperado.insert(0, "0.001")
        errorEsperado.pack(side = "right", expand = FALSE)
        intervalPanel.add(errorEsperado)
        self.calcPanel.add(intervalPanel)
        method = StringVar();
        method.set("Biseccion")

        methodList=OptionMenu(self.calcPanel, method, "Biseccion", "Falsa Posicion", "Newton Raphson", "Secante");
        methodList.pack(side = TOP)
        self.calcPanel.add(methodList)

        rootButton = Button(self.calcPanel, text ="Get Root", command = lambda: self.Table(input.get(), method.get(), float(intervalInf.get()), float(intervalSup.get()), float(errorEsperado.get())));
        goButton = Button(self.calcPanel, text ="Graph", command = lambda: self.graph(input.get()))
        #goButton = Button(calcPanel, text ="Calculate", command = lambda: self.graphPoint(int(input.get()),int(input.get()),10))
        rootButton.pack(side = LEFT)
        goButton.pack(side = TOP)
        self.calcPanel.add(rootButton)
        self.calcPanel.add(goButton)

        self.calcPanel.pack(fill = BOTH, expand = FALSE)
        self.window.mainloop()


    def planoCartesiano(self, canva,WIDTH:int, HEIGHT:int, LENGTH:int):
        """
        Dibuja la interfaz
    
        Args:
            WIDTH (int): Ancho de la ventana
            HEIGHT (int): Alto de la ventana
            LENGTH (int): Cantidad de cuadros
            title (str): Titulo de la ventana
        """
        scala = math.floor(HEIGHT/LENGTH)
        zero=HEIGHT/2
        size=HEIGHT
        canva.pack(side=tk.LEFT)
        ##draw lines
        canva.create_line(zero, 0, zero, size, fill="gray", width=3)
        canva.create_line(0, zero, size, zero, fill="gray", width=3)
        x=-1*(zero)
        for i in range(0, size+1, scala):
            canva.create_line(0, i, size, i, fill="gray")
            canva.create_text(i,zero+8, text=str(int(x/(LENGTH/2)/LENGTH)), fill="blue")
            x=x+scala
        x=-1*(zero)
        for i in range(0, size+1, scala):
            canva.create_line(i, 0, i, size, fill="gray")
            canva.create_text(zero-8,i, text=str(int(-1*(x/(LENGTH/2)/LENGTH))), fill="blue")
            x=x+scala



    def graphPoint(self,canva, x, y, weigth):
        x=x+250
        y=(250)-y
        canva.create_oval(x-weigth/2,y-weigth/2,x+weigth/2,y+weigth/2, fill="red")
    

    def graph(self, fx:str):
        plano=tk.Tk()
        plano.title("Plano Cartesiano")
        canva = tk.Canvas(plano, width=self.size, height=self.size, bg="white")
        self.planoCartesiano(canva,self.size, self.size, 10)

        points = metodos.fxpoints(fx, math.floor((-1)*self.size/2), math.floor(self.size/2))
        for x in range(0, len(points)):
            self.graphPoint(canva,x*50, points[x]*50,5)
            #self.canva.create_line(x*50,points[x]*50,x+50*50,points[x]*50, fill="red")
            #print(i, " => ", points[i])
            #self.canva.create_oval(250+(i*self.LENGTH*self.LENGTH),250+(points[i]*self.LENGTH*self.LENGTH),(i*self.LENGTH*self.LENGTH)+253,250+(points[i]*self.LENGTH*self.LENGTH)+3, fill="red")
            #self.canva.create_oval(points[i]*self.size/2,i,self.size/2+250,i+250, fill="red")
            #time.sleep(0.1)
    

    def Table(self, fx:str, method:str, inf:float, sup:float, errorEsperado:float): 
        list = [()]
        print(method)
        if method == "Biseccion":
            list = metodos.biseccion(inf,sup,fx,errorEsperado)
        elif method == "Newton Raphson":
            list = metodos.newtonRaphson(inf,fx,fx,errorEsperado)
        elif method == "Falsa Posicion":
            list = metodos.falsaPosicion(inf,sup,fx,errorEsperado)
        elif method == "Secante":
            list = metodos.secante(inf,sup,fx,errorEsperado)
        self.createTable(list)
        
    def createTable(self, list:list):
        table=tk.Tk()
        table.title("Calculo de raices")
        rows = len(list)
        cols = len(list[0])
        for i in range(rows):
            for j in range(cols):
                 
                self.e = Entry(table, width=10, fg='blue', justify='center',
                               font=('Arial',11,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, list[i][j]) 
