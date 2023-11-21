import math

def newtonRaphson(x0, f, fder, epsilon):
    x = x0
    while True:
        x = x - f(x)/fder(x)
        if abs(f(x)) < epsilon:
            break
    return x
def fxpoints(fx:str, inicioX:int, finX:int):
    """
    Calcula los valores de una funcion y retorna una lista con los valores en y
    """
    points = []
    for i in range(inicioX, finX+1):
        x=i;
        points.append(eval(evaluate(fx)))
    return points

def evaluate(fx:str):
    """
    Evalua un string "funcion" en lenguaje natural y
    lo convierte a lenguaje python 
    """
    fxfinal = fx.replace("ln", "math.log").replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan").replace("sqrt", "math.sqrt").replace("e^x","math.exp(x)")
    return fxfinal;
