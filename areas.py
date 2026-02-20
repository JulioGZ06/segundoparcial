import os
import math

def menu():
    print("===== AREAS =====")
    print("1.- CUADRADO")
    print("2.- RECTANGULO")
    print("3.- TRIANGULO")
    print("4.- CIRCULO")
    print("5.- TRAPECIO")
    print("6.- SALIR")

def CUADRADO():
    lado = float(input("Lado: "))
    print("Resultado:", lado * lado)
    input("Presiona ENTER para continuar...")

def RECTANGULO():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print("Resultado:", base * altura)
    input("Presiona ENTER para continuar...")

def TRIANGULO():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    print("Resultado:", base * altura / 2)
    input("Presiona ENTER para continuar...")

def CIRCULO():
    radio = float(input("Radio: "))
    print("Resultado:", math.pi * radio ** 2)
    input("Presiona ENTER para continuar...")

def TRAPECIO():
    baseM = float(input("Base mayor: "))
    basem = float(input("Base menor: "))
    altura = float(input("Altura: "))
    print("Resultado:", (baseM + basem) * altura / 2)
    input("Presiona ENTER para continuar...")

opcion = 0

while opcion != 6:
    os.system("cls")
    menu()
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        CUADRADO()
    elif opcion == 2:
        RECTANGULO()
    elif opcion == 3:
        TRIANGULO()
    elif opcion == 4:
        CIRCULO()
    elif opcion == 5:
        TRAPECIO()
    elif opcion == 6:
        print("Saliendo del programa...")
    else:
        print("Opción no válida")
        input("Presiona ENTER para continuar...")
