import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter
import mysql.connector
import ventanaNacionalidad

root_tk = tk.Tk()
root_tk.geometry("1220x720")
root_tk.title("Personas")
root_tk.config(bg="#000")

datos = {}
# dfsdfsdfsdfsd
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="persona"
)

mycursor = mydb.cursor()


def on_key_typed1(event):
    for i in tree.get_children():
        tree.delete(i)
    tecla = event.char
    tecla_presionada = cajaNom.get()
    tecla_presionada = tecla_presionada + tecla
    print("tecla: ", tecla_presionada)
    cargar_tabla(tecla_presionada,
                 "SELECT id,cedula,apellido,nombre,edad,nacionalidad FROM personas WHERE apellido LIKE")


def on_key_typed2(event):
    for i in tree.get_children():
        tree.delete(i)
    tecla = event.char
    tecla_presionada = cajaNom.get()
    tecla_presionada = tecla_presionada + tecla
    print("tecla: ", tecla_presionada)
    cargar_tabla(tecla_presionada,
                 "SELECT id,cedula,apellido,nombre,edad,nacionalidad FROM personas WHERE nombre LIKE")


def guardar():
    cedula = int(cajaCedula.get())
    nombre = str(cajaNom.get())
    apellido = str(cajaApe.get())
    edad = int(cajaEdad.get())
    nacionalidad = label.cget("text")
    if nacionalidad == '':
        messagebox.showerror(
            message="Solo se puede borrar por numero de cedula", title="Error")
    else:
        mycursor.execute("INSERT INTO personas (nombre,apellido,edad,nacionalidad,cedula) VALUES(%s,%s,%s,%s,%s)",
                         (nombre, apellido, edad, nacionalidad, cedula))
        mydb.commit()


def limpiar():
    cajaNom.delete(0, tk.END)
    cajaCedula.delete(0, tk.END)
    cajaApe.delete(0, tk.END)
    cajaEdad.delete(0, tk.END)


def borrar():
    cedula = int(cajaCedula.get())
    if cajaCedula.get():
        messagebox.showerror(
            message="Solo se puede borrar por numero de cedula", title="Error")
    else:
        mycursor.execute("DELETE FROM personas WHERE cedula = %s", [cedula])
        mydb.commit()


def cargar_combo():
    mycursor.execute("SELECT id,descripcion FROM nacionalidad")
    filas = mycursor.fetchall()

    for fila in filas:
        llave = fila[1]+"-"+str(fila[0])
        valor = fila[1]
        datos[llave] = valor
        combobox['values'] = list(datos.keys())


def cargar_tabla(tecla, sql):
    # falta cambiar el select por un select like
    mycursor.execute(sql+"%s", ['%'+tecla+'%'])
    filas = mycursor.fetchall()
    # falta limpiar la tabla antes de cargar
    for fila in filas:
        tree.insert("", tk.END, values=(
            fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]))


label = ttk.Label(root_tk, text='')
labelt1 = ttk.Label(root_tk, text="Formulario Complicado",
                    background="#000", foreground="#fff")
labelt2 = ttk.Label(root_tk, text="Ejemplo",
                    background="#000", foreground="#fff")
labelt3 = ttk.Label(root_tk, text="2023", background="#000", foreground="#fff")
labelCedula = ttk.Label(root_tk, text="Cedula",
                        background="#000", foreground="#fff")
labelApeNom = ttk.Label(root_tk, text="Apellido y Nombre",
                        background="#000", foreground="#fff")
labelEdad = ttk.Label(root_tk, text="Edad",
                      background="#000", foreground="#fff")
labelNacionalidad = ttk.Label(
    root_tk, text="Nacionalidad", background="#000", foreground="#fff")
labelNacionalidades = ttk.Label(
    root_tk, text="Nacionalidades", background="#000", foreground="#fff")

cajaCedula = customtkinter.CTkEntry(master=root_tk, width=120, height=25)
cajaCedula.insert(0, '0')
cajaApe = customtkinter.CTkEntry(master=root_tk, width=120, height=25)
cajaNom = customtkinter.CTkEntry(master=root_tk, width=120, height=25)
cajaEdad = customtkinter.CTkEntry(master=root_tk, width=120, height=25)
cajaEdad.insert(0, '0')

buttonLimpiar = customtkinter.CTkButton(
    master=root_tk, corner_radius=10, text="Limpiar", command=limpiar)
buttonGuardar = customtkinter.CTkButton(
    master=root_tk, corner_radius=10, text="Guardar", command=guardar)
buttonBorrar = customtkinter.CTkButton(
    master=root_tk, corner_radius=10, text="Borrar", command=borrar)
buttonSalir = customtkinter.CTkButton(
    master=root_tk, corner_radius=10, text="Salir", command=root_tk.destroy)
buttonNacionalidades = customtkinter.CTkButton(
    master=root_tk, corner_radius=10, text="Nacionalidades", command=lambda: ventanaNacionalidad.ventanasecundaria(''))

labelt1.grid(column=0, row=0, pady=20, sticky="nsew")
labelt2.grid(column=2, row=0, pady=20, sticky="nsew")
labelt3.grid(column=3, row=0, pady=20, sticky="nsew")
labelCedula.grid(column=0, row=1,   sticky="nsew")
labelApeNom.grid(column=0, row=2,   sticky="nsew")
labelEdad.grid(column=0, row=3,  sticky="nsew")
labelNacionalidad.grid(column=2, row=3,  sticky="nsew")
labelNacionalidades.grid(column=2, row=1,  sticky="nsew")

cajaCedula.grid(column=1, row=1, sticky="nsew")
cajaApe.grid(column=1, row=2, sticky="nsew")
cajaApe.bind('<Key>', on_key_typed1)
cajaNom.grid(column=2, row=2, sticky="nsew")
cajaNom.bind('<Key>', on_key_typed2)
cajaEdad.grid(column=1, row=3, sticky="nsew")

buttonLimpiar.grid(column=0, row=4, sticky="nsew")
buttonGuardar.grid(column=1, row=4, sticky="nsew")
buttonBorrar.grid(column=2, row=4, sticky="nsew")
buttonSalir.grid(column=3, row=4, sticky="nsew")
buttonNacionalidades.grid(column=3, row=1, sticky="nsew")


columns = ('Id', 'Cedula', 'Apellido', 'Nombre', 'Edad', 'Nacionalidad')
tree = ttk.Treeview(root_tk, columns=columns, show='headings')
tree.heading('Id', text='Id')
tree.heading('Cedula', text='Cedula')
tree.heading('Apellido', text='Apellido')
tree.heading('Nombre', text='Nombre')
tree.heading('Edad', text='Edad')
tree.heading('Nacionalidad', text='Nacionalidad')
tree.grid(row=5, column=0, columnspan=6, padx=10, rowspan=4, sticky="nsew")


def seleccioncombo(event):
    llaveselecionada = combobox.get()
    seleccionado = datos.get(llaveselecionada)
    label.configure(text=seleccionado)
    print(seleccionado)


combobox = ttk.Combobox(root_tk, state="readonly")
combobox.bind("<<ComboboxSelected>>", seleccioncombo)
combobox.grid(column=3, row=3, sticky="nsew")
cargar_combo()
cargar_tabla(
    '', "SELECT id,cedula,apellido,nombre,edad,nacionalidad FROM personas WHERE nombre LIKE")

root_tk.mainloop()
