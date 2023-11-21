import math
def evaluate(fx:str):
    """
    Evalua un string "funcion" en lenguaje natural y lo convierte a 
    lenguaje python
    """
    fxfinal = fx.replace("ln", "math.log").replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan").replace("sqrt", "math.sqrt")
    return fxfinal;
