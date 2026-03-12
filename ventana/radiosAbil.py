import tkinter as tk

def deshabilitar():
    radio1.config(state="disabled")
def habilitar():
    radio1.config(state="normal")
    
ventana = tk.Tk()
ventana.title("Control de Radiobutton")
ventana.geometry("300x200")

opcion= tk.IntVar()

radio1 = tk.Radiobutton(ventana, text="opcion1", variable=opcion, value=1)
radio1.pack(pady=10)
var_cineco = tk.IntVar()
tk.Checkbutton(ventana,text="Tarjeta Cineco",variable=var_cineco).grid(row=4,column=0,columnspan=2,pady=5)

tk.Button(ventana, text="Deshabilitar", command=deshabilitar).pack(pady=5)
tk.Button(ventana, text="habilitar", command=habilitar).pack(pady=5)

ventana.mainloop()