import tkinter as tk
from tkinter import *
import math, time
import metodos;
class PlanoCartesiano:

    """Docstring for planoCartesiano. """
    window = tk.Tk()

    def __init__(self, WIDTH:int, HEIGHT:int, LENGTH:int, title:str):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.LENGTH = LENGTH
        self.title = title
        self.size = HEIGHT
        self.interface(WIDTH, HEIGHT, LENGTH, title)
    
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
            self.canva.create_text(i,zero, text=str(x), fill="blue")
            x=x+scala
        x=-1*(zero)
        for i in range(0, size+1, scala):
            self.canva.create_line(i, 0, i, size, fill="gray")
            self.canva.create_text(zero,i, text=str(-1*x),fill="blue")
            x=x+scala

        calcPanel = PanedWindow(orient="vertical")

        input = Entry(calcPanel, font=("Arial", 20))
        input.pack(side = TOP)
        calcPanel.add(input)

        method = StringVar();
        method.set("Linear")

        methodList=OptionMenu(calcPanel, method, "Linear", "Quadratic", "Cubic");
        methodList.pack(side = TOP)
        calcPanel.add(methodList)

        goButton = Button(calcPanel, text ="Calculate", command = lambda: self.graph(input.get()))
        goButton.pack(side = TOP)
        calcPanel.add(goButton)

        calcPanel.pack(fill = BOTH, expand = FALSE)
        self.window.title(title)
        self.window.mainloop()
    def graph(self, fx:str):
        points = metodos.fxpoints(fx, math.floor((-1)*self.size/2), math.floor(self.size/2))

        for i in range(0, len(points)):
            print(i, " => ", points[i])
            self.canva.create_oval(points[i]*self.size/2,i,points[i]*self.size/2,i, fill="red")
            #time.sleep(0.1)


