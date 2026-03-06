import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
opciones = ("Mexico", "Colombia", "Peru", "Chile")

combo = ttk.Combobox(root, values=opciones)
combo.pack (pady=20)

def obtener():
    label_resultado.config(text=combo.get())