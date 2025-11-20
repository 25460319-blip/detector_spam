import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("aviso", "Boton presionado")

ventana = tk.Tk()   #crear la ventana principal
ventana.title("ventana simple") # Le da un titulo

label = tk.Label(ventana, text ="Hola, Mundo")
label.pack(pady=10)

boton = tk.Button(ventana, text="haz clic aqui", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()  #Muestra la Ventana