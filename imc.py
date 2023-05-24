import tkinter
import customtkinter


def conversion():
    imc = round(float(peso.get())/((float(altura.get())/100)*(float(altura.get())/100)),2)
    result.configure(text = imc)
    

root_tk = tkinter.Tk()

root_tk.geometry("600x400")

root_tk.title("Conversor")
root_tk.config(bg="#000")

button = customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Convertir",
                                 command = conversion)


peso = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)
altura = customtkinter.CTkEntry(master = root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)

result = customtkinter.CTkLabel(master=root_tk,
                               text="",
                               width=120,
                               height=25,
                               corner_radius=10)

label1 = customtkinter.CTkLabel(master=root_tk,
                               text="PESO",
                               width=120,
                               height=25,
                               corner_radius=10)
label2 = customtkinter.CTkLabel(master=root_tk,
                                text="ALTURA",
                               width=120,
                               height=25,
                               corner_radius=10)



button.place(relx=0.3, rely = 0.4, anchor = tkinter.CENTER)
peso.place(relx=0.2, rely = 0.2, anchor = tkinter.CENTER)
altura.place(relx=0.4, rely = 0.2, anchor = tkinter.CENTER)
result.place(relx=0.2, rely = 0.5, anchor = tkinter.CENTER)
label1.place(relx=0.2, rely = 0.1, anchor = tkinter.CENTER)
label2.place(relx=0.4, rely = 0.1, anchor = tkinter.CENTER)




root_tk.mainloop()