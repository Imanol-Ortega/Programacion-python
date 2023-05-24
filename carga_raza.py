import tkinter
import customtkinter
import mysql.connector

root_tk = tkinter.Tk()
root_tk.title("Combo Ejemplo")
root_tk.geometry("450x300")
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

mycursor = mydb.cursor()

def guardar_raza():
    raza = str(entry.get())
    mycursor.execute("INSERT INTO raza (tipo_raza) VALUES(%s)",[raza])
    mydb.commit()

label = customtkinter.CTkLabel(master=root_tk,
                               text="Ingrese raza: ",
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
                                 command= guardar_raza)


button.place(relx=0.3, rely = 0.3, anchor = tkinter.CENTER)
entry.place(relx=0.4, rely = 0.2, anchor = tkinter.CENTER)
label.place(relx=0.1, rely = 0.2, anchor = tkinter.CENTER)

root_tk.mainloop()