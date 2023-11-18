import tkinter as tk
from tkinter import *

def button(method):
    print(method)

window = tk.Tk()
window.geometry("800x500")

##############
canva = tk.Canvas(window, width=500, height=500, bg="white")
#align the canva in the right of the window
canva.pack(side=tk.LEFT)
canva.create_line(250, 0, 250, 500, fill="gray", width=3)
canva.create_line(0, 250, 500, 250, fill="gray", width=3)
x=-250
for i in range(0, 501, 50):
    canva.create_line(0, i, 500, i, fill="gray")
    canva.create_text(i,250, text=str(x), fill="blue")
    x=x+50
x=-250
for i in range(0, 501, 50):
    canva.create_line(i, 0, i, 500, fill="gray")
    canva.create_text(250,i, text=str(x),fill="blue")
    x=x+50
##############

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
calcPanel.configure(relief = RAISED)

window.title("Graph")
window.mainloop()

