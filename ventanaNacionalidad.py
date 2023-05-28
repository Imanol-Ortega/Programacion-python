import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter

import mysql.connector


def ventanasecundaria(Texto):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="persona"
    )

    mycursor = mydb.cursor()

    def on_key_typed(event):
        for i in tabla.get_children():
            tabla.delete(i)
        tecla = event.char
        tecla_presionada = cajaNacionalidad.get()
        tecla_presionada = tecla_presionada + tecla
        print("tecla: ", tecla_presionada)
        cargar_tabla(tecla_presionada)

    def borrar():
        brr = str(cajaNacionalidad.get())
        mycursor.execute(
            "DELETE FROM nacionalidad WHERE descripcion = %s", [brr])
        mydb.commit()

    def guardar():
        grd = str(cajaNacionalidad.get())
        mycursor.execute(
            "INSERT INTO nacionalidad (descripcion) VALUES(%s)", [grd])
        mydb.commit()

    def cargar_tabla(tecla):
        mycursor.execute(
            "SELECT id, descripcion FROM nacionalidad WHERE descripcion LIKE %s", ['%'+tecla+'%'])
        filas = mycursor.fetchall()
        for fila in filas:
            tabla.insert("", tk.END, values=(fila[0], fila[1]))
    print(Texto)  # dfdfd
    frm2 = tk.Toplevel()
    frm2.geometry("1000x500")
    frm2.title("Nacionalidades")
    frm2.config(bg="#000")
    labelt2 = ttk.Label(frm2, text="Ingrese la Nacionalidad",
                        background="#000", foreground="#fff")
    labelt2.grid(column=0, row=1, sticky="nsew")
    cajaNacionalidad = customtkinter.CTkEntry(
        master=frm2, width=120, height=25)
    cajaNacionalidad.grid(column=1, row=1, sticky="nsew")
    cajaNacionalidad.bind('<Key>', on_key_typed)
    buttonGuardar = customtkinter.CTkButton(
        master=frm2, corner_radius=10, text="Guardar", command=guardar)
    buttonGuardar.grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
    buttonBorrar = customtkinter.CTkButton(
        master=frm2, corner_radius=10, text="Borrar", command=borrar)
    buttonBorrar.grid(column=1, row=3, padx=20, pady=20, sticky="nsew")
    buttonSalir = customtkinter.CTkButton(
        master=frm2, corner_radius=10, text="Salir", command=frm2.destroy)
    buttonSalir.grid(column=2, row=3, padx=20, pady=20, sticky="nsew")

    columns = ('Id', 'Nacionalidad')
    tabla = ttk.Treeview(frm2, columns=columns, show='headings')
    tabla.heading('Id', text='Id')
    tabla.heading('Nacionalidad', text='Nacionalidad')

    tabla.grid(row=5, column=0, columnspan=6,
               padx=20, rowspan=4, sticky="nsew")
    cargar_tabla('')
