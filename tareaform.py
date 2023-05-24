import tkinter
import tkinter as tk
from tkinter import ttk
import customtkinter
import mysql.connector


root_tk = tk.Tk()
root_tk.geometry("900x720")
root_tk.title("Codigo de Barras")
root_tk.config(bg="#000")

def guardar_nombre():
    return

def cargar_tabla(event):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="persona"
    )

    mycursor = mydb.cursor()
    #falta cambiar el select por un select like
    mycursor.execute("SELECT id,cedula,apellido,nombre,edad,Nacionalidad FROM personas")
    filas = mycursor.fetchall()
    #falta limpiar la tabla antes de cargar
    for fila in filas:
        tabla.insert("", tk.END, values=(fila[0],fila[1]))

labelt1 = ttk.Label(root_tk,text="Formulario Complicado",background="#000",foreground="#fff")
labelt2 = ttk.Label(root_tk,text="Ejemplo",background="#000",foreground="#fff")
labelt3 = ttk.Label(root_tk,text="2023",background="#000",foreground="#fff")
labelCedula = ttk.Label(root_tk,text="Cedula",background="#000",foreground="#fff")
labelApeNom = ttk.Label(root_tk,text="Apellido y Nombre",background="#000",foreground="#fff")
labelEdad = ttk.Label(root_tk,text="Edad",background="#000",foreground="#fff")
labelNacionalidad = ttk.Label(root_tk,text="Nacionalidad",background="#000",foreground="#fff")

cajaCedula = customtkinter.CTkEntry(master= root_tk,width=120,height=25)
cajaApe = customtkinter.CTkEntry(master= root_tk,width=120,height=25)
cajaNom = customtkinter.CTkEntry(master= root_tk,width=120,height=25)
cajaEdad = customtkinter.CTkEntry(master=root_tk,width=120,height=25)
cajaNcl = customtkinter.CTkEntry(master=root_tk,width=120,height=25)

buttonLimpiar = customtkinter.CTkButton(master = root_tk,corner_radius= 10,text= "Limpiar",command= guardar_nombre)
buttonGuardar = customtkinter.CTkButton(master = root_tk,corner_radius= 10,text= "Guardar",command= guardar_nombre)
buttonBorrar = customtkinter.CTkButton(master = root_tk,corner_radius= 10,text= "Borrar",command= guardar_nombre)
buttonSalir = customtkinter.CTkButton(master = root_tk,corner_radius= 10,text= "Salir",command= root_tk.destroy)


labelt1.grid( column=0,row=0, columnspan=2, sticky="nsew")
labelt2.grid( column=2,row=0, columnspan=1, sticky="nsew")
labelt3.grid( column=3,row=0, columnspan=1, sticky="nsew")
labelCedula.grid( column=0,row=1, columnspan=1,  sticky="nsew")
labelApeNom.grid( column=0,row=2, columnspan=1,  sticky="nsew")
labelEdad.grid( column=0,row=3, columnspan=1,  sticky="nsew")
labelNacionalidad.grid( column=2,row=3, columnspan=1, sticky="nsew")

cajaCedula.grid( column=1,row=1,padx=10, pady=50, sticky="nsew")
cajaApe.grid( column=1,row=2,padx=10, pady=50, sticky="nsew")
cajaNom.grid( column=2,row=2,padx=10, pady=50, sticky="nsew")
cajaEdad.grid( column=1,row=3, padx=10, pady=50, sticky="nsew")
cajaNcl.grid( column=3,row=3, padx=10, pady=50, sticky="nsew")

buttonLimpiar.grid(column=0, row=4,padx=10, pady=20,sticky="nsew")
buttonGuardar.grid(column=1, row=4,padx=10, pady=20,sticky="nsew")
buttonBorrar.grid(column=2, row=4,padx=10, pady=20,sticky="nsew")
buttonSalir.grid(column=3, row=4,padx=10, pady=20, sticky="nsew")



columns = ('id', 'Cedula','Apellido','Nombre','Edad','Nacionalidad')
tabla = ttk.Treeview(root_tk, columns=columns, show='headings')
tabla.heading('codigo', text='Codigo')
tabla.heading('producto', text='Producto')

tabla.grid(row=5,column=0, columnspan=2,padx=10, rowspan=8,pady=10, sticky="nsew")

root_tk.mainloop()