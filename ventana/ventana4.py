import tkinter as tk
from tkinter import ttk

def mostrar_texto():
    texto=entrada.get() 
    label_resultado.config(text=f"Escribiste: {texto}")

ventana = tk.Tk()
#le damos un titulo ala ventana
ventana.title("Ejemplo con Entry")
#le damos un tamaño ala ventana
ventana.geometry("400x300")

# creamos una entrada de texto
entrada= tk.Entry(ventana, font=("Arial",14))
entrada.pack(pady=20)

boton=tk.Button(ventana, text="Enviar", command=mostrar_texto)
boton.pack()

label_resultado= ttk.Label(ventana, text="")
label_resultado.pack(pady=10)

ventana.mainloop()