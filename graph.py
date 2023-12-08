import planoCartesiano as PC
import metodos, math, sympy
#print(str(metodos.fxpoints( "ln(x)", -10, 5)).replace(", ","\n"))
#print(metodos.evaluate("e^(x)-3*x^2"))
#print(str(sympy.diff(metodos.evaluate("e^(x)-3*x^2"))))
#print(metodos.newtonRaphson(1,"-3*x^2",0.1))
"""print(metodos.solve("e^(x)-3*x^2", 5));
print(metodos.solve("ln(x)", 5));
print(metodos.solve("tan(x)", 5));
print(metodos.solve("e^(x)", 5));
print(metodos.solve("sec(x)", 5));"""
a =PC.PlanoCartesiano(800, 500, 10, "Plano Cartesiano")
#metodos.biseccion(1,2,"x**5+4*x**2-10",0.01)
