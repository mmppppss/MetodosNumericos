import tkinter as tk
from tkinter import *
import math

def button(method):
    print(method)

window = tk.Tk()

def Graph(WIDTH:int, HEIGHT:int, LENGTH:int, title:str):
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
    window.geometry(str(WIDTH)+"x"+str(HEIGHT))
    canva = tk.Canvas(window, width=size, height=size, bg="white")
    canva.pack(side=tk.LEFT)
    ##draw lines
    canva.create_line(zero, 0, zero, size, fill="gray", width=3)
    canva.create_line(0, zero, size, zero, fill="gray", width=3)
    x=-1*(zero)
    for i in range(0, size+1, scala):
        canva.create_line(0, i, size, i, fill="gray")
        canva.create_text(i,zero, text=str(x), fill="blue")
        x=x+scala
    x=-1*(zero)
    for i in range(0, size+1, scala):
        canva.create_line(i, 0, i, size, fill="gray")
        canva.create_text(zero,i, text=str(-1*x),fill="blue")
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

    goButton = Button(calcPanel, text ="Calculate", command = lambda: button(method.get()))
    goButton.pack(side = TOP)
    calcPanel.add(goButton)

    calcPanel.pack(fill = BOTH, expand = FALSE)
    window.title(title)
    window.mainloop()



