import tkinter as tk
from tkinter import *
import math, time
import metodos
class PlanoCartesiano:

    """Docstring for planoCartesiano. """
    window = tk.Tk()
    calcPanel = PanedWindow(orient="vertical")

    def __init__(self, WIDTH:int, HEIGHT:int, LENGTH:int, title:str):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.LENGTH = LENGTH
        self.title = title
        self.size = HEIGHT
        self.createTable(metodos.biseccion(1,2,"x**5+4*x**2-10",0.01))
        self.window.mainloop()
        #self.interface(WIDTH, HEIGHT, LENGTH, title)
    def interface(self, WIDTH:int, HEIGHT:int, LENGTH:int, title:str):
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
        self.window.geometry(str(WIDTH)+"x"+str(HEIGHT))
        self.canva = tk.Canvas(self.window, width=size, height=size, bg="white")
        self.canva.pack(side=tk.LEFT)
        ##draw lines
        self.canva.create_line(zero, 0, zero, size, fill="gray", width=3)
        self.canva.create_line(0, zero, size, zero, fill="gray", width=3)
        x=-1*(zero)
        for i in range(0, size+1, scala):
            self.canva.create_line(0, i, size, i, fill="gray")
            self.canva.create_text(i,zero, text=str(x/(LENGTH/2)), fill="blue")
            x=x+scala
        x=-1*(zero)
        for i in range(0, size+1, scala):
            self.canva.create_line(i, 0, i, size, fill="gray")
            self.canva.create_text(zero,i, text=str(-1*(x/(LENGTH/2))), fill="blue")
            x=x+scala


        input = Entry(self.calcPanel, font=("Arial", 20))
        input.pack(side = TOP)
        self.calcPanel.add(input)

        method = StringVar();
        method.set("Linear")

        methodList=OptionMenu(self.calcPanel, method, "Linear", "Quadratic", "Cubic");
        methodList.pack(side = TOP)
        self.calcPanel.add(methodList)

        goButton = Button(self.calcPanel, text ="Calculate", command = lambda: self.graph(input.get()))
        #goButton = Button(calcPanel, text ="Calculate", command = lambda: self.graphPoint(int(input.get()),int(input.get()),10))
        goButton.pack(side = TOP)
        self.calcPanel.add(goButton)

        self.calcPanel.pack(fill = BOTH, expand = FALSE)
        self.window.title(title)
        self.window.mainloop()

    def graphPoint(self, x, y, weigth):
        x=x+250
        y=(250)-y
        self.canva.create_oval(x-weigth/2,y-weigth/2,x+weigth/2,y+weigth/2, fill="red")

    def graph(self, fx:str):
        points = metodos.fxpoints(fx, math.floor((-1)*self.size/2), math.floor(self.size/2))
        for x in range(0, len(points)):
            self.graphPoint(x, points[x],5)
            #print(i, " => ", points[i])
            #self.canva.create_oval(250+(i*self.LENGTH*self.LENGTH),250+(points[i]*self.LENGTH*self.LENGTH),(i*self.LENGTH*self.LENGTH)+253,250+(points[i]*self.LENGTH*self.LENGTH)+3, fill="red")
            #self.canva.create_oval(points[i]*self.size/2,i,self.size/2+250,i+250, fill="red")
            #time.sleep(0.1)

    def createTable(self, list:list):
        rows = len(list)
        cols = len(list[0])
        for i in range(rows):
            for j in range(cols):
                 
                self.e = Entry(self.window, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, list[i][j]) 
