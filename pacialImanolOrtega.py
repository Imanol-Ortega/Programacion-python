import tkinter
import customtkinter

root_tk = tkinter.Tk()

root_tk.geometry("700x500")

root_tk.title("Contabilidad")
root_tk.config(bg="#000")

#v_balance quiere decir variable de balance y lo mismo para estado

tot_ingreso = 0
tot_egreso = 0
cant_ingreso = 0
cant_egreso = 0
v_balance = 0
v_estado = 0


#Funciones de los botones
def ingreso():
    global tot_ingreso,cant_ingreso,v_balance,v_estado
    lbl_informe.configure(text = "")
    tot_ingreso += int(monto.get())
    cant_ingreso = cant_ingreso + 1
    v_balance = tot_ingreso - tot_egreso
    if v_balance <= -10000000:
        lbl_estado.configure(text = "ESTADO: En quiebra")
    elif v_balance >= - 9999999 and v_balance<0:
        lbl_estado.configure(text = "ESTADO: balance negativo")
    elif v_balance == 0:
        lbl_estado.configure(text = "ESTADO: Neutro")
    elif v_balance>0 and v_balance<10000000:
        lbl_estado.configure(text = "ESTADO: Balance Positivo")
    elif v_balance>=10000000:
        lbl_estado.configure(text = "ESTADO: Superávit")
    
    lbl_total_egresos.configure(text = "Total egreso: " + str(tot_egreso))
    lbl_total_ingresos.configure(text = "Total ingreso: "+str(tot_ingreso))
    lbl_cantidad_egresos.configure(text = "cantidad egreso: "+str(cant_egreso))
    lbl_cantidad_ingresos.configure(text = "cantidad ingreso: "+str(cant_ingreso))
    lbl_balance.configure(text = "Balance: "+str(v_balance))

def egreso():
    global tot_egreso,cant_egreso,v_balance,v_estado
    lbl_informe.configure(text = "")
    tot_egreso += int(monto.get())
    cant_egreso = cant_egreso + 1
    v_balance = tot_ingreso - tot_egreso
    if v_balance <= -10000000:
        lbl_estado.configure(text = "ESTADO: En quiebra")
    elif v_balance >= - 9999999 and v_balance<0:
        lbl_estado.configure(text = "ESTADO: balance negativo")
    elif v_balance == 0:
        lbl_estado.configure(text = "ESTADO: Neutro")
    elif v_balance>0 and v_balance<10000000:
        lbl_estado.configure(text = "ESTADO: Balance Positivo")
    elif v_balance>=10000000:
        lbl_estado.configure(text = "ESTADO: Superávit")

    lbl_total_egresos.configure(text = "Total egreso: " + str(tot_egreso))
    lbl_total_ingresos.configure(text = "Total ingreso: "+str(tot_ingreso))
    lbl_cantidad_egresos.configure(text = "cantidad egreso: "+str(cant_egreso))
    lbl_cantidad_ingresos.configure(text = "cantidad ingreso: "+str(cant_ingreso))
    lbl_balance.configure(text = "Balance: "+str(v_balance))

def reinicio():
    global tot_egreso,tot_ingreso,cant_egreso,cant_ingreso,v_balance,v_estado
    if cant_ingreso == 0:
        lbl_informe.configure(text = "Se acaban de reiniciar los valores")
    else:
        monto.delete(0,tkinter.END)
        tot_ingreso = 0
        tot_egreso = 0
        cant_ingreso = 0
        cant_egreso = 0
        v_balance = 0
        v_estado = 0
        lbl_estado.configure(text = "ESTADO: Neutro")
        lbl_total_egresos.configure(text = "Total egreso: 0" )
        lbl_total_ingresos.configure(text = "Total ingreso: 0")
        lbl_cantidad_egresos.configure(text = "cantidad egreso: 0")
        lbl_cantidad_ingresos.configure(text = "cantidad ingreso: 0")
        lbl_balance.configure(text = "Balance: 0")

#DEFINICION y configuracion DE BOTONES, LABELS Y ENTRYS
btn_ingreso = customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Ingreso",
                                 command = ingreso)
btn_egreso = customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Egreso",
                                 command = egreso)
btn_reinicio = customtkinter.CTkButton(master = root_tk,
                                 corner_radius= 10,
                                 text= "Reinicio",
                                 command = reinicio)

monto = customtkinter.CTkEntry(master = root_tk,
                                    width=200,
                                    height=28,
                                    corner_radius=10,
                                    fg_color="#fff",
                                    text_color="#000")
lbl_monto = customtkinter.CTkLabel(master=root_tk,
                               text="Monto: ",
                               width=80,
                               height=25,
                               corner_radius=10)
lbl_total_ingresos = customtkinter.CTkLabel(master=root_tk,
                               text="Total ingreso: 0",
                               width=120,
                               height=25,
                               corner_radius=10)
lbl_cantidad_ingresos = customtkinter.CTkLabel(master=root_tk,
                               text="Cantidad ingreso: 0",
                               width=120,
                               height=25,
                               corner_radius=10)
lbl_total_egresos= customtkinter.CTkLabel(master=root_tk,
                               text="Total egreso: 0",
                               width=120,
                               height=25,
                               corner_radius=10)
lbl_cantidad_egresos = customtkinter.CTkLabel(master=root_tk,
                               text="Cantidad egreso: 0",
                               width=120,
                               height=25,
                               corner_radius=10)
lbl_balance = customtkinter.CTkLabel(master=root_tk,
                               text="Balance: 0",
                               width=120,
                               height=25,
                               corner_radius=10)
lbl_estado = customtkinter.CTkLabel(master=root_tk,
                               text="Estado: Neutro",
                               width=120,
                               height=25,
                               corner_radius=10)

lbl_informe = customtkinter.CTkLabel(master=root_tk,
                               text="a",
                               width=200,
                               height=25,
                               corner_radius=10)

monto.place(relx=0.5, rely = 0.1, anchor = tkinter.CENTER)

btn_ingreso.place(relx=0.2, rely = 0.3, anchor = tkinter.CENTER)
btn_egreso.place(relx=0.5, rely = 0.3, anchor = tkinter.CENTER)
btn_reinicio.place(relx=0.8, rely = 0.3, anchor = tkinter.CENTER)

lbl_monto.place(relx=0.3, rely = 0.1, anchor = tkinter.CENTER)
lbl_total_ingresos.place(relx=0.2, rely = 0.45, anchor = tkinter.CENTER)
lbl_cantidad_ingresos.place(relx=0.2, rely = 0.55, anchor = tkinter.CENTER)
lbl_total_egresos.place(relx=0.8, rely = 0.45, anchor = tkinter.CENTER)
lbl_cantidad_egresos.place(relx=0.8, rely = 0.55, anchor = tkinter.CENTER)
lbl_balance.place(relx=0.2, rely = 0.65, anchor = tkinter.CENTER)
lbl_estado.place(relx=0.8, rely = 0.65, anchor = tkinter.CENTER)
lbl_informe.place(relx=0.5, rely = 0.9, anchor = tkinter.CENTER)

root_tk.mainloop()