import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacion = opcion.get()
        
        if operacion == 1:
            resultado = num1 + num2
        elif operacion == 2:
            resultado = num1 - num2
        elif operacion == 3:
            resultado = num1 * num2
        elif operacion == 4:
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero")
                return
            resultado = num1 / num2
        else:
            messagebox.showwarning("Advertencia", "Selecciona una operación")
            return
        
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")
        
# Crear ventana principal 
ventana = tk.Tk()
ventana.title("Calculadora con Radiobotones")
ventana.geometry("350x300")

# Etiquetas y entradas
tk.Label(ventana, text="Primer número:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Segundo número:").pack(pady=5)
entrada2 = tk.Entry(ventana) 
entrada2.pack()

opcion = tk.IntVar()

tk.Label(ventana, text="Selecciona la operación:").pack(pady=10)

tk.Radiobutton(ventana, text="Sumar", variable=opcion, value=1).pack()
tk.Radiobutton(ventana, text="Restar", variable=opcion, value=2).pack()
tk.Radiobutton(ventana, text="Multiplicación", variable=opcion, value=3).pack()
tk.Radiobutton(ventana, text="División", variable=opcion, value=4).pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()

ventana.mainloop()
