import math

def biseccion(xl:float, xu:float, fx:str, es:float):
    """
    Encuentra la raiz de una ecuacion con el metodo de la biseccion
    Args:
        xl (float): Limite inferior
        xu (float): Limite superior
        fx (str): Funcion
        es (int): Error permitido
    """
    list=[(str("XL"),str("XU"),str("FX(XL)"),str("FX(XU)"),str("XR"),str("EA"))]
    xr=(xl+xu)/2
    ea=100
    while ea>es:
        if solve(fx, xl)*solve(fx, xr)<0:
            xu=xr
        else:
            xl=xr
        xr=(xl+xu)/2
        ea=abs((xr-xl)/xr)*100
        print(round(xl, 3), "\t", round(xu, 3), "\t", round(solve(fx, xl), 3), "\t", round(solve(fx, xu), 3), "\t", round(xr,3),"\t", round(ea, 3))
        li=(str(round(xl, 3)), str(round(xu, 3)), str(round(solve(fx, xl), 3)), str(round(solve(fx, xu), 3)), str(round(xr,3)), str(round(ea, 3)))
        list.append(li)
    return list


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

def solve(fx, x):
    return eval(evaluate(fx))

def evaluate(fx:str):
    """
    Evalua un string "funcion" en lenguaje natural y
    la convierte a lenguaje python 
    """
    fxfinal = fx.replace("sin", "math.sin")\
            .replace("cos", "math.cos")\
            .replace("tan", "math.tan")\
            .replace("sqrt", "math.sqrt")\
            .replace("log","math.log10")\
            .replace("ln","math.log")\
            .replace("e^","math.exp")\
            .replace("^","**")\
            .replace("sec","1/math.cos")\
            .replace("cosec","1/math.sin")\
            .replace("cot","1/math.tan")
    return fxfinal

def mathError(fx):
    return  fx.__contains__("ln") or fx.__contains__("sqrt") or fx.__contains__("log") 


