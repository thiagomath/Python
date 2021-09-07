from tkinter import *


def bt_click():
    if str(peso.get()).isnumeric() and str(altura.get()).isnumeric():
        p = float(peso.get())
        a = float(altura.get())

        label_IMC["text"] = p / a**2
    elif "." in peso.get() or altura.get():
        p = float(peso.get())
        a = float(altura.get())

        label_IMC["text"] = p / a ** 2
    else:
        label_IMC["text"] = "Valores inválidos!"


# janela
janela = Tk()
janela.geometry("250x200+50+50")
janela.title("T-Force")
# variáveis
# Peso
label_peso = Label(janela, text="Peso (kg): ")
label_peso.place(x=20, y=20)
peso = Entry(janela, width=20)
peso.place(x=90, y=20)
# Altura
label_altura = Label(janela, text="Altura (m): ")
label_altura.place(x=20, y=50)
altura = Entry(janela, width=20)
altura.place(x=90, y=50)
# Botão
bt = Button(janela, text="Calcular IMC", width=16, command=bt_click)
bt.place(x=90, y=80)
# Resultado IMC
label_IMC = Label(janela, text=f" ")
label_IMC.place(x=90, y=120)
janela.mainloop()
