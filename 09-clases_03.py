import os
import math

class Areas:

    def cuadrado(self, lado):
        self.res = lado * lado
        return self.res

    def rectangulo(self, base, altura):
        self.res = base * altura
        return self.res

    def triangulo(self, base, altura):
        self.res = (base * altura) / 2
        return self.res

    def circulo(self, radio):
        self.res = math.pi * radio ** 2
        return self.res

    def trapecio(self, B, b, h):
        self.res = ((B + b) * h) / 2
        return self.res

    def imprimir(self):
        print("El área es:", self.res)


class Menu:

    def mostrar(self):
        print("===== AREAS =====")
        print("1.- CUADRADO")
        print("2.- RECTANGULO")
        print("3.- TRIANGULO")
        print("4.- CIRCULO")
        print("5.- TRAPECIO")
        print("6.- SALIR")


def main():
    objArea = Areas()
    objMenu = Menu()

    op = 0

    while op != 6:
        os.system("cls")
        objMenu.mostrar()
        op = int(input("Opción: "))

        if op == 1:
            lado = float(input("Lado: "))
            objArea.cuadrado(lado)
            objArea.imprimir()
            input()

        elif op == 2:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            objArea.rectangulo(base, altura)
            objArea.imprimir()
            input()

        elif op == 3:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            objArea.triangulo(base, altura)
            objArea.imprimir()
            input()

        elif op == 4:
            radio = float(input("Radio: "))
            objArea.circulo(radio)
            objArea.imprimir()
            input()

        elif op == 5:
            B = float(input("Base mayor: "))
            b = float(input("Base menor: "))
            h = float(input("Altura: "))
            objArea.trapecio(B, b, h)
            objArea.imprimir()
            input()


if __name__ == "__main__":
    main()