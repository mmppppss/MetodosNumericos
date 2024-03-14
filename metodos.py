import math

def biseccion(xl:float, xu:float, fx:str, es:float):
    """
    Encuentra la raiz de una ecuacion con el metodo de la biseccion
    Args:
        xl (float): Limite inferior
        xu (float): Limite superior
        fx (str): Funcion
        es (int): Error permitido
    return: lista con las iteraciones
    """
    i=1
    list=[(str("i"),str("XL"),str("XU"),str("FX(XL)"),str("FX(XU)"),str("XR"),str("EA"))]
    xr=(xl+xu)/2
    ea=100
    while ea>es:
        if solve(fx, xl)*solve(fx, xr)<0:
            xu=xr
        else:
            xl=xr
        xr=(xl+xu)/2
        ea=abs((xr-xl)/xr)*100
        #print(round(xl, 3), "\t", round(xu, 3), "\t", round(solve(fx, xl), 3), "\t", round(solve(fx, xu), 3), "\t", round(xr,3),"\t", round(ea, 3))
        li=(str(i),str(round(xl, 8)), str(round(xu, 8)), str(round(solve(fx, xl), 8)), str(round(solve(fx, xu), 8)), str(round(xr,8)), str(round(ea, 8)))
        list.append(li)
        i+=1
    return list

def falsaPosicion(xl:float, xu:float, fx:str, es:float):
    """
    Encuentra la raiz de una ecuacion con el metodo de la falsa posicion
    Args:
        xl (float): Limite inferior
        xu (float): Limite superior
        fx (str): Funcion
        es (int): Error permitido
    return: lista con las iteraciones
    """
    i=1
    list=[(str("i"),str("XL"),str("XU"),str("f(xl)"),str("f(xu)"),str("xr"),str("EA(%)"))]
    xr=(xl*solve(fx, xu)-xu*solve(fx, xl))/(solve(fx, xu)-solve(fx, xl))
    ea=100
    while ea>es:
        if solve(fx, xl)*solve(fx, xr)<0:
            xu=xr
        else:
            xl=xr
        xr=(xl*solve(fx, xu)-xu*solve(fx, xl))/(solve(fx, xu)-solve(fx, xl))
        ea=abs((xr-xl)/xr)*100
        li=(str(i),str(round(xl, 8)), str(round(xu, 8)), str(round(solve(fx, xl), 8)), str(round(solve(fx, xu), 8)), str(round(xr,8)), str(round(ea, 8)))
        list.append(li)
        i+=1
    return list

def newtonRaphson(xi:float, fx:str, dx:str, es:float):
    """
    Encuentra la raiz de una ecuacion con el metodo de la newton-raphson
    Args:
        x0 (float): Punto inicial
        fx (str): Funcion
        es (int): Error permitido
    return: lista con las iteraciones
    """
    i=1
    list=[(str("i"),str("xi"),str("EA(%)"))]
    #dx=str(sympy.diff(evaluate(fx)))
    ea=100
    while ea>es:
        xi1=xi-(solve(fx,xi)/solve(dx,xi))
        ea=abs((xi1-xi)/xi1)*100
        li=(str(i),str(round(xi, 8)), str(round(ea, 8))+"%")
        list.append(li)
        xi=xi1
        i+=1
    return list

def secante(xi:float, xi1:float, fx:str, es:float):
    """
    Encuentra la raiz de una ecuacion con el metodo de la secante
    Args:
        xi (float): Punto inicial
        xi1 (float): Punto secundario
        fx (str): Funcion
        es (int): Error permitido
    return: lista de tuplas con las iteraciones
    """
    i=1
    list=[(str("i"),str("xi"),str("f(xi)"),str("f(xi+1)"),str("xi+1"),str("EA(%)"))]
    ea=100
    while ea>es:
        xipri=xi
        xiseg=xi1
        xinew=xiseg-((solve(fx,xiseg)*(xipri-xiseg))/(solve(fx,xipri)-solve(fx,xiseg)))
        ea=abs((xi1-xi)/xi1)*100
        li=(str(i),str(round(xi, 8)), str(round(solve(fx, xi), 8)), str(round(solve(fx, xi1), 8)), str(round(xi1,8)), str(round(ea, 8)))
        list.append(li)
        xi1=xinew
        xi=xiseg
        i+=1
    return list

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
            #.replace("exp","math.exp")\
    return fxfinal

def mathError(fx):
    return  fx.__contains__("ln") or fx.__contains__("sqrt") or fx.__contains__("log") 


