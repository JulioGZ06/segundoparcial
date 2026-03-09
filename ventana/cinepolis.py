import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

PRECIO_BOLETO = 12

def procesar():
    try:
        personas = int(entry_personas.get())
        boletos = int(entry_boletos.get())
        cineco = var_cineco.get()

        if personas <= 0:
            messagebox.showerror("Error", "Debe haber al menos 1 persona")
            return

        limite = personas * 7

        if boletos > limite:
            messagebox.showerror("Error", "Excede el límite de boletos")
            return

        if boletos <= 0:
            messagebox.showerror("Error", "Cantidad inválida")
            return

        subtotal = boletos * PRECIO_BOLETO

        if boletos >= 6:
            subtotal = subtotal - (subtotal * 0.15)
        elif boletos >= 3:
            subtotal = subtotal - (subtotal * 0.10)

        if cineco == 1:
            subtotal = subtotal - (subtotal * 0.10)

        total = round(subtotal, 2)

        label_total.config(text="Total a pagar: $" + str(total))
        messagebox.showinfo("Compra", "Compra realizada")

    except:
        messagebox.showerror("Error", "Datos incorrectos")


ventana = tk.Tk()
ventana.title("Cinepolis")
ventana.geometry("550x450")

# imagen
imagen = Image.open("CINE.png")
imagen = imagen.resize((550,450))
fondo = ImageTk.PhotoImage(imagen)

label_fondo = tk.Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# titulo
tk.Label(ventana, text="Cinepolis", font=("Arial",16)).grid(row=0,column=0,columnspan=2,pady=10)

# nombre
tk.Label(ventana, text="Nombre").grid(row=1,column=0,padx=10,pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1,column=1,padx=10,pady=5)

# personas
tk.Label(ventana, text="Cantidad Compradores").grid(row=2,column=0,padx=10,pady=5)
entry_personas = tk.Entry(ventana)
entry_personas.grid(row=2,column=1,padx=10,pady=5)

# boletos
tk.Label(ventana, text="Cantidad de Boletos").grid(row=3,column=0,padx=10,pady=5)
entry_boletos = tk.Entry(ventana)
entry_boletos.grid(row=3,column=1,padx=10,pady=5)

# tarjeta
var_cineco = tk.IntVar()
tk.Checkbutton(ventana,text="Tarjeta Cineco",variable=var_cineco).grid(row=4,column=0,columnspan=2,pady=5)

# total
label_total = tk.Label(ventana,text="Total a pagar: $0")
label_total.grid(row=5,column=0,columnspan=2,pady=10)

# botones
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=6,column=0,columnspan=2,pady=10)

tk.Button(frame_botones,text="Procesar",command=procesar).grid(row=0,column=2,padx=10)
tk.Button(frame_botones,text="Salir",command=ventana.quit).grid(row=0,column=3,padx=10)

ventana.mainloop()
