"""
Las funciones en py son bloques de codigos reutilizables que
realizan una tarea especifica.
sirven para organizar , reutilizar y hacer mas claro el codigo

para que sirve?
-evitan repetir codigo
-permiten dividir un problema grande en partes pequeñas
-hacen el programa mas facil de manter
-mejoran la legibilidad

En python se definen con la palabra clave def:

def nombre_funcion(parametros):
    #bloque de codigo
    return valor
"""

def nombre():
    print("Hola mundo")
nombre()

def suma():
    a=6
    print("dentro de la funcion :",a)
    b=7
    c=a+b
    
    return c
print("la suma es : ",suma())

a=3
print("fuera de la fucion :",a)
b=7
c=a+b

def multiplicacion(a,b):
    return a*b
print("La multiplicacion es : ",multiplicacion(a,b))


