import tkinter
import customtkinter


def suma():
    print("Suma")
    e_text = int(entry1.get()) + int(entry2.get())
    label2.configure(text = e_text)
def resta():
    print("Resta")
    e_text = int(entry1.get()) - int(entry2.get())
    label2.configure(text = e_text)
def muLtiplicacion():
    print("Multiplicacion")
    e_text = int(entry1.get()) * int(entry2.get())
    label2.configure(text = e_text)
def division():
    print("Division")
    e_text = int(entry1.get()) / int(entry2.get())
    label2.configure(text = e_text)

root_tk = tkinter.Tk()

root_tk.geometry("800x450")

root_tk.title("Si")
root_tk.config(bg="#000")

button_sum = customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Sumar",
                                 command= suma)
button_res= customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Restar",
                                 command= resta)
button_mult = customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Multiplicar",
                                 command= muLtiplicacion)
button_div = customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Dividir",
                                 command= division)
entry1 = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)
entry2 = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)

label = customtkinter.CTkLabel(master=root_tk,
                               text="Concatenacion",
                               width=120,
                               height=25,
                               corner_radius=10)
label2 = customtkinter.CTkLabel(master=root_tk,
                                text="",
                               width=120,
                               height=25,
                               corner_radius=10)


button_sum.place(relx=0.2, rely = 0.8, anchor = tkinter.CENTER)
button_res.place(relx=0.4, rely = 0.8, anchor = tkinter.CENTER)
button_mult.place(relx=0.6, rely = 0.8, anchor = tkinter.CENTER)
button_div.place(relx=0.8, rely = 0.8, anchor = tkinter.CENTER)
entry1.place(relx=0.5, rely = 0.3, anchor = tkinter.CENTER)
entry2.place(relx=0.5, rely = 0.5, anchor = tkinter.CENTER)
label.place(relx=0.5, rely = 0.1, anchor = tkinter.CENTER)
label2.place(relx=0.5, rely = 0.9, anchor = tkinter.CENTER)

root_tk.mainloop()