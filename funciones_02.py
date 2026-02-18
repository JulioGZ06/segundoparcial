import os

def suma():
    os.system("cls")
    a=int(input("Num1: "))
    b=int(input("Num2: "))
    res=a+b
    print("La suma es: ",res)
    input()
    
def resta():
    os.system("cls")
    a=int(input("Num1: "))
    b=int(input("Num2: "))
     res=a-b
    print("La resta es: ",res)
    input()
    
def menu():
    op=0
    while op != 5:
        os.system("cls")
        print("1.- +\n 2.- - \n 3.- *\n 4.-/ \n 5.- salir\n")
        op=int(imput("OPCION: "))
        if op==1:
            suma()
        if op==2:
            resta()
if __name__==("__main__")
menu()s
