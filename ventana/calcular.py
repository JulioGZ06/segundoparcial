import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2 
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa numeros validos")
        
ventana = tk.Tk()
ventana.title("CALCULAR")
ventana.geometry("300x200")

tk.Label(ventana, text="Numero 1:").grid(row=0, column=0, padx=5, pady=5)
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Numero 2:").grid(row=1, column=0, padx=5, pady=5)
entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1, padx=5, pady=5)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

tk.Button(ventana, text="Calcular", command=sumar).grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()
