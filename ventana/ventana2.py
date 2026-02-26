import tkinter as tk

#creamos la ventana principal
ventana = tk.Tk()
#le damos un titulo ala ventana
ventana.title("Mi primera applicacion")
#le damos un tamaño ala ventana
ventana.geometry("400x300")

#creamos una etiqueta
etiqueta = tk.Label(ventana, text="Hola Mundo",font=("Arial", 16,"bold"))
etiqueta.pack(pady=20)
#mostramos la etiqueta en la ventana
ventana.mainloop() 