import tkinter
import customtkinter



root_tk = tkinter.Tk()

root_tk.geometry("600x400")

root_tk.title("Conversor")
root_tk.config(bg="#000")

radio_var = tkinter.StringVar(value="1")

def calculo():
    entry_resultado.delete(0,tkinter.END)
    result = 0
    if radio_var.get() == "1":
        result = int(entry1.get()) + int(entry2.get())
    elif radio_var.get() == "2":
        result = int(entry1.get()) - int(entry2.get())
    elif radio_var.get() == "3":
       result = round(float(entry1.get()) / float(entry2.get()),2)
    else:
       result = int(entry1.get()) * int(entry2.get())

    entry_resultado.insert(0, result)

label_entry1 = customtkinter.CTkLabel(master=root_tk,
                                text="Numero 1",
                               width=120,
                               height=25,
                               corner_radius=10,
                               text_color="#fff")
label_entry2 = customtkinter.CTkLabel(master=root_tk,
                                text="Numero 2",
                               width=120,
                               height=25,
                               corner_radius=10,
                               text_color="#fff")
resultado = customtkinter.CTkLabel(master=root_tk,
                                text="Resultado",
                               width=200,
                               height=25,
                               corner_radius=10,
                               text_color="#fff") 
entry_resultado = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)                  
entry1 = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)
entry2 = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)
calcular = customtkinter.CTkButton(master = root_tk,
                                  corner_radius= 10,
                                  text= "Calcular",
                                  command = calculo)

sumar = customtkinter.CTkRadioButton(master=root_tk, 
                                    text="SUMAR",
                                    variable= radio_var, 
                                    value=1)
restar = customtkinter.CTkRadioButton(master=root_tk, 
                                    text="RESTAR",
                                    variable= radio_var, 
                                    value=2)
dividir = customtkinter.CTkRadioButton(master=root_tk, 
                                    text="DIVIDIR",
                                    variable= radio_var, 
                                    value=3)
multiplicar= customtkinter.CTkRadioButton(master=root_tk, 
                                    text="MULTIPLICAR",
                                    variable= radio_var, 
                                    value=4)

entry1.place(relx=0.4, rely = 0.1, anchor = tkinter.CENTER)
entry2.place(relx=0.4, rely = 0.25, anchor = tkinter.CENTER)
label_entry1.place(relx=0.2, rely = 0.1, anchor = tkinter.CENTER)
label_entry2.place(relx=0.2, rely = 0.25, anchor = tkinter.CENTER)
resultado.place(relx=0.2, rely = 0.4, anchor = tkinter.CENTER)
entry_resultado.place(relx=0.4, rely = 0.4, anchor = tkinter.CENTER)
calcular.place(relx=0.4, rely = 0.7, anchor = tkinter.CENTER)
sumar.place(relx=0.2, rely = 0.5, anchor = tkinter.CENTER)
restar.place(relx=0.4, rely = 0.5, anchor = tkinter.CENTER)
dividir.place(relx=0.6, rely = 0.5, anchor = tkinter.CENTER)
multiplicar.place(relx=0.8, rely = 0.5, anchor = tkinter.CENTER)

root_tk.mainloop()