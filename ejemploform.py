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
    #falta cambiar el select por un select like
    mycursor.execute("SELECT id, nombre,apellido,nacionalidad,cedula FROM personas")
    filas = mycursor.fetchall()
    #falta limpiar la tabla antes de cargar
    for fila in filas:
        tabla.insert("", tk.END, values=(fila[0],fila[1]))

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Busqueda Incremental").grid(column=0, row=0)
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=1, row=0,padx=20, pady=20, sticky="nsew")

ttk.Label(frm, text="Codigo").grid(column=0, row=1)
caja = ttk.Entry(frm)
caja.grid( column=1,row=0, columnspan=2, padx=20, pady=20, sticky="nsew")
caja.bind('<Key>', cargar_tabla)


columns = ('codigo', 'producto')
tabla = ttk.Treeview(frm, columns=columns, show='headings')
tabla.heading('codigo', text='Codigo')
tabla.heading('producto', text='Producto')

tabla.grid(row=2,column=0, columnspan=2,padx=10, rowspan=8,pady=10, sticky="nsew")




root.mainloop()