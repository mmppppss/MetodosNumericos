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
    try:
        for i in range(inicioX, finX+1):
            x=i;
            if not(mathError(fx) and (x<=0)) :
                points.append(eval(evaluate(fx)))
    except Exception as e:
        print("[#] ERROR: ",e)
    return points

def evaluate(fx:str):
    """
    Evalua un string "funcion" en lenguaje natural y
    la convierte a lenguaje python 
    """
    fxfinal = fx.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan").replace("sqrt", "math.sqrt").replace("log","math.log10").replace("ln","math.log").replace("e^","math.exp")
    return fxfinal

def mathError(fx):
    return  fx.__contains__("ln") or fx.__contains__("sqrt") or fx.__contains__("log") 


