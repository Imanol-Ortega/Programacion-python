import tkinter as tk
from tkinter import *
from tkinter import ttk

import mysql.connector


def cargar_tabla(event):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="persona"
    )

    mycursor = mydb.cursor()
    # falta cambiar el select por un select like
    mycursor.execute(
        "SELECT id,nombre,apellido,nacionalidad,cedula FROM personas")
    filas = mycursor.fetchall()
    # falta limpiar la tabla antes de cargar
    for fila in filas:
        tabla.insert("", tk.END, values=(fila[0], fila[1]))


root = Tk()
root.geometry("1000x800")


caja = ttk.Entry(frm)
caja.grid(column=1, row=0, columnspan=2, padx=20, pady=20, sticky="nsew")
caja.bind('<Key>', cargar_tabla)
ttk.Button(frm, text="Salir", command=root.destroy).grid(
    column=0, row=4, padx=20, pady=20, sticky="nsew")


columns = ('codigo', 'producto')
tabla = ttk.Treeview(frm, columns=columns, show='headings')
tabla.heading('codigo', text='Codigo')
tabla.heading('producto', text='Producto')

tabla.grid(row=2, column=0, columnspan=2, padx=10,
           rowspan=8, pady=10, sticky="nsew")


root.mainloop()
