import tkinter as tk

#creamos la ventana principal

def saludo():
    label_resultado.config(text="Hola Alumnos De Python")

ventana = tk.Tk()
#le damos un titulo ala ventana
ventana.title("Mi primera applicacion")
#le damos un tamaño ala ventana
ventana.geometry("400x300")

#creamos el boton
boton=tk.Button(ventana, text="Saludar", command=saludo)
boton.pack(pady=20)

#creamos una etiqueta
label_resultado= tk.Label(ventana, text="",font=("Arial", 16,"bold"))
label_resultado.pack(pady=20)
#mostramos la etiqueta en la ventana
ventana.mainloop() 