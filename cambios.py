import tkinter
import customtkinter


def conversion():
    dolar = int(entry.get()) / 7200 
    pesos = int(entry.get()) / 30 
    real = int(entry.get()) / 1700 
    euro = int(entry.get()) / 7800 
    result1.configure(text = round(dolar,2))
    result2.configure(text = round(pesos,2))
    result3.configure(text = round(real,2))
    result4.configure(text = round(euro,2))

root_tk = tkinter.Tk()

root_tk.geometry("600x400")

root_tk.title("Conversor")
root_tk.config(bg="#000")

button = customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Convertir",
                                 command = conversion)


entry = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)

gs = customtkinter.CTkLabel(master=root_tk,
                               text="Guaranies: ",
                               width=120,
                               height=25,
                               corner_radius=10)

label1 = customtkinter.CTkLabel(master=root_tk,
                               text="Dolar: ",
                               width=120,
                               height=25,
                               corner_radius=10)
label2 = customtkinter.CTkLabel(master=root_tk,
                                text="Real: ",
                               width=120,
                               height=25,
                               corner_radius=10)
label3 = customtkinter.CTkLabel(master=root_tk,
                                text="Pesos: ",
                               width=120,
                               height=25,
                               corner_radius=10)
label4 = customtkinter.CTkLabel(master=root_tk,
                                text="Euro: ",
                               width=120,
                               height=25,
                               corner_radius=10)
result1 = customtkinter.CTkLabel(master=root_tk,
                                text="",
                               width=120,
                               height=25,
                               corner_radius=10,fg_color="#333")
result2 = customtkinter.CTkLabel(master=root_tk,
                                text="",
                               width=120,
                               height=25,
                               corner_radius=10,fg_color="#333")
result3 = customtkinter.CTkLabel(master=root_tk,
                                text="",
                               width=120,
                               height=25,
                               corner_radius=10,fg_color="#333")
result4 = customtkinter.CTkLabel(master=root_tk,
                                text="",
                               width=120,
                               height=25,
                               corner_radius=10,fg_color="#333")

button.place(relx=0.4, rely = 0.4, anchor = tkinter.CENTER)
entry.place(relx=0.4, rely = 0.2, anchor = tkinter.CENTER)
gs.place(relx=0.2, rely = 0.2, anchor = tkinter.CENTER)
label1.place(relx=0.2, rely = 0.6, anchor = tkinter.CENTER)
label2.place(relx=0.2, rely = 0.7, anchor = tkinter.CENTER)
label3.place(relx=0.2, rely = 0.8, anchor = tkinter.CENTER)
label4.place(relx=0.6, rely = 0.6, anchor = tkinter.CENTER)
result1.place(relx=0.4, rely = 0.6, anchor = tkinter.CENTER)
result2.place(relx=0.4, rely = 0.7, anchor = tkinter.CENTER)
result3.place(relx=0.4, rely = 0.8, anchor = tkinter.CENTER)
result4.place(relx=0.8, rely = 0.6, anchor = tkinter.CENTER)

root_tk.mainloop()