import tkinter
import customtkinter

ims = 0
imn = 0
x = 0

def mas():
    global ims
    global x
    x=x+1
    if x>10:
        ims=ims+1
        x=0
    print(x)
    label2.configure(text = x)
    label3.configure(text = ims)

def menos():
    global imn
    global x
    x=x-1
    if x<-10:
        imn=imn+1
        x=0
    print(x)
    label2.configure(text = x)
    label1.configure(text = imn)

root_tk = tkinter.Tk()

root_tk.geometry("800x450")

root_tk.title("Si")
root_tk.config(bg="#000")

button_mas= customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "+",
                                 command= mas)
button_menos= customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "-",
                                 command= menos)
label1 = customtkinter.CTkLabel(master=root_tk,
                               text="0",
                               width=120,
                               height=25,
                               corner_radius=10,
                               fg_color="#000")
label2 = customtkinter.CTkLabel(master=root_tk,
                                text="0",
                               width=120,
                               height=25,
                               corner_radius=10)
label3 = customtkinter.CTkLabel(master=root_tk,
                                text="0",
                               width=120,
                               height=25,
                               corner_radius=10)

button_mas.place(relx=0.5, rely = 0.2, anchor = tkinter.CENTER)
button_menos.place(relx=0.5, rely = 0.8, anchor = tkinter.CENTER)
label1.place(relx=0.2, rely = 0.5, anchor = tkinter.CENTER)
label2.place(relx=0.5, rely = 0.5, anchor = tkinter.CENTER)
label3.place(relx=0.8, rely = 0.5, anchor = tkinter.CENTER)

root_tk.mainloop()