import tkinter
import tkinter as tk
from tkinter import ttk
import customtkinter
import mysql.connector


root_tk = tk.Tk()
root_tk.geometry("820x300")
root_tk.title("Codigo de Barras")
root_tk.config(bg="#000")




def tabla(tecla_presionada):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="producto"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT productoId,productoCdigoBarra,productoDescripcion,productoPrecio FROM producto WHERE productoDescripcion LIKE %s ",['%'+tecla_presionada+'%'])
    filas = mycursor.fetchall()
    
    for fila in filas:
        tree.insert("", tk.END, text=fila[0], values=(fila[0],fila[1],fila[2],fila[3]))


def on_key_typed(event):
    for i in tree.get_children():
        tree.delete(i)
    tecla = event.char
    tecla_presionada = cajatexto.get()
    tecla_presionada  = tecla_presionada + tecla
    print("tecla: ",tecla_presionada)
    tabla(tecla_presionada)


cajatexto = tk.Entry(root_tk)
cajatexto.pack()
cajatexto.bind('<Key>',on_key_typed)  



columns = ('Id', 'Codigo','Descripcion','Precio')
tree = ttk.Treeview(root_tk, columns=columns, show='headings')
tree.heading('Id', text='Id')
tree.heading('Codigo', text='Codigo')
tree.heading('Descripcion', text='Descripcion')
tree.heading('Precio', text='Precio')
tree.pack()

tabla('')



root_tk.mainloop()