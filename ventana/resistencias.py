import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# valores de colores
colores = {
    "negro": 0,
    "cafe": 1,
    "rojo": 2,
    "naranja": 3,
    "amarillo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "gris": 8,
    "blanco": 9
}

# multiplicadores 
multiplicador = {
    "negro": 1,
    "cafe": 10,
    "rojo": 100,
    "naranja": 1000,
    "amarillo": 10000,
    "verde": 100000,
    "azul": 1000000,
    "violeta": 10000000,
    "gris": 100000000,
    "blanco": 1000000000
}

def calcular():

    c1 = combo1.get()
    c2 = combo2.get()
    c3 = combo3.get()

    v1 = colores[c1]
    v2 = colores[c2]
    mult = multiplicador[c3]

    valor = (v1 * 10 + v2) * mult

    if tolerancia.get() == "oro":
        tol = valor * 0.05
    else:
        tol = valor * 0.10

    maximo = valor + tol
    minimo = valor - tol

    lbl_valor.config(text=f"Valor ohm: {valor}")
    lbl_max.config(text=f"Valor maximo: {int(maximo)}")
    lbl_min.config(text=f"Valor minimo: {int(minimo)}")


ventana = tk.Tk()
ventana.title("Calculadora de Resistencias")
ventana.geometry("300x550")

titulo = tk.Label(ventana, text="Calcular valor de resistencia", font=("Arial",12))
titulo.pack(pady=10)

# ----- IMAGEN -----
imagen = Image.open("resistencias.png")
imagen = imagen.resize((250,150))
foto = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(ventana, image=foto)
label_imagen.pack(pady=5)

# ------------------

combo1 = ttk.Combobox(ventana, values=list(colores.keys()))
combo1.set("Selecciona el color")
combo1.pack(pady=5)

combo2 = ttk.Combobox(ventana, values=list(colores.keys()))
combo2.set("Selecciona el color")
combo2.pack(pady=5)

combo3 = ttk.Combobox(ventana, values=list(multiplicador.keys()))
combo3.set("Selecciona el color")
combo3.pack(pady=5)

tolerancia = tk.StringVar()
tolerancia.set("oro")

tk.Label(ventana,text="Tolerancia").pack()

tk.Radiobutton(ventana,text="Oro",variable=tolerancia,value="oro").pack()
tk.Radiobutton(ventana,text="Plata",variable=tolerancia,value="plata").pack()

btn = tk.Button(ventana,text="Calcular",command=calcular)
btn.pack(pady=10)

lbl_valor = tk.Label(ventana,text="Valor ohm:")
lbl_valor.pack()

lbl_max = tk.Label(ventana,text="Valor maximo:")
lbl_max.pack()

lbl_min = tk.Label(ventana,text="Valor minimo:")
lbl_min.pack()

ventana.mainloop()