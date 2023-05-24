import tkinter
import tkinter as tk
import customtkinter
import mysql.connector


root_tk = tk.Tk()
root_tk.geometry("600x300")
root_tk.title("Codigo de Barras")
root_tk.config(bg="#000")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="productos"
)

mycursor = mydb.cursor()

def enter_presionado(event):
    entryid.delete(0,tk.END)
    entrydesc.delete(0,tk.END)
    entrypre.delete(0,tk.END)
    textoLeido = cajatexto.get()
    mycursor.execute("SELECT productoId,productoDescripcion,productoPrecio FROM producto WHERE productoCodigoBarra = %s",[textoLeido])
    data = mycursor.fetchall()
    print(data[0][0]," ",data[0][1]," ",data[0][2])
    entryid.insert(0, data[0][0])
    entrydesc.insert(0, data[0][1])
    entrypre.insert(0, data[0][2])
    cajatexto.delete(0,tk.END)


cajatexto = tk.Entry(root_tk)
cajatexto.pack()
cajatexto.bind('<Return>',enter_presionado)


labelid = customtkinter.CTkLabel(master=root_tk,
                               text="ID: ",
                               width=120,
                               height=25,
                               corner_radius=10)
entryid = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)
labeldesc = customtkinter.CTkLabel(master=root_tk,
                               text="DESCRIPCION: ",
                               width=120,
                               height=25,
                               corner_radius=10)
entrydesc = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)
labelpre = customtkinter.CTkLabel(master=root_tk,
                               text="PRECIO: ",
                               width=120,
                               height=25,
                               corner_radius=10)
entrypre = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)



labelid.place(relx=0.17, rely = 0.2, anchor = tkinter.CENTER)
entryid.place(relx=0.17, rely = 0.4, anchor = tkinter.CENTER)
labeldesc.place(relx=0.5, rely = 0.2, anchor = tkinter.CENTER)
entrydesc.place(relx=0.5, rely = 0.4, anchor = tkinter.CENTER)
labelpre.place(relx=0.87, rely = 0.2, anchor = tkinter.CENTER)
entrypre.place(relx=0.87, rely = 0.4, anchor = tkinter.CENTER)



root_tk.mainloop()





#def un_key_typed():
#    tecla_presionada = event.chat
#    print("tecla: ",tecla_presionada)
#
#cajatexto.bind('<Key>',on_key_typed)  
