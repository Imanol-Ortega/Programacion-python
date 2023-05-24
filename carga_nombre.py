import tkinter
from tkinter import ttk
import customtkinter
import mysql.connector

root_tk = tkinter.Tk()
root_tk.title("Combo Ejemplo")
root_tk.geometry("450x400")
root_tk.title("Si")
root_tk.config(bg="#000")
# Diccionario
datos = {}

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="animales"
    )

def cargar_combo():
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT tipo_raza,id_raza FROM raza")
    filas = mycursor.fetchall()

    for fila in filas:
        llave = str(fila[1])+"-"+fila[0]
        valor = fila[1]
        datos[llave] = valor
        combobox['values'] = list(datos.keys())


def guardar_nombre():
    nombre = str(entry.get())
    val_sel = label2.cget("text")
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO perro (nombre,raza) VALUES (%s,%s)",(nombre,val_sel))
    mydb.commit()
    

label = customtkinter.CTkLabel(master=root_tk,
                               text="Nombre: ",
                               width=120,
                               height=25,
                               corner_radius=10)
label2 = customtkinter.CTkLabel(master=root_tk,
                               text="",
                               width=120,
                               height=25,
                               corner_radius=10)
entry = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)
button = customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Guardar",
                                 command= guardar_nombre)
                                 

def seleccioncombo(event):
    llaveselecionada = combobox.get()
    seleccionado = datos.get(llaveselecionada)
    label2.configure(text=seleccionado)

combobox = ttk.Combobox(root_tk, state="readonly")
combobox.bind("<<ComboboxSelected>>", seleccioncombo)
combobox.place(relx=0.3, rely = 0.4, anchor = tkinter.CENTER)



button.place(relx=0.3, rely = 0.3, anchor = tkinter.CENTER)
entry.place(relx=0.4, rely = 0.2, anchor = tkinter.CENTER)
label.place(relx=0.2, rely = 0.2, anchor = tkinter.CENTER)
label2.place(relx=0.2, rely = 0.5, anchor = tkinter.CENTER)

cargar_combo()

root_tk.mainloop()