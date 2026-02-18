import os

os.system("cls")

def menu():
    print("=== OPERACIONES BÁSICAS ===")
    print("1.- SUMA")
    print("2.- RESTA")
    print("3.- MULTIPLICACION")
    print("4.- DIVISION")
    print("5.- SALIR")


def suma():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("Resultado:", a + b)
    input("Presiona ENTER para continuar...")


def resta():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("Resultado:", a - b)
    input("Presiona ENTER para continuar...")


def multiplicar():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("Resultado:", a * b)
    input("Presiona ENTER para continuar...")


def dividir():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("Resultado:", a / b)
    input("Presiona ENTER para continuar...")

opcion = 0

while opcion != 5:
    os.system("cls")
    menu()
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicar()
    elif opcion == 4:
        dividir()
    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida")
        input("Presiona ENTER para continuar...")

