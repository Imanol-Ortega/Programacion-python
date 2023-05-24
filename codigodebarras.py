import tkinter as tk

def enter_presionado():
    textoLeido = cajatexto.get()
    print("Texto: ",textoLeido)

root_tk = tk.Tk()
root_tk.geometry("200x23")
cajatexto = tk.Entry(root_tk)
cajatexto.pack()

cajatexto.bind('<Return>',enter_presionado)
root_tk.mainloop()


###
# ###