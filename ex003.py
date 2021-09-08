from tkinter import *


def bt_soma():
    if str(num1.get()).isnumeric() and str(num2.get()).isnumeric():
        n1 = float(num1.get())
        n2 = float(num2.get())
        soma = n1 + n2
        label_resposta["text"] = f'{soma:.2f}'
    else:
        label_resposta["text"] = 'Erro!'


# Janela
janela = Tk()
janela.title("ex003")
janela.geometry("250x200+20+20")
# Variáveis
# Valor 1
label_num1 = Label(janela, text="Valor 1: ")
label_num1.place(x=30, y=20)
num1 = Entry(janela, width=20)
num1.place(x=80, y=20)
# Valor 2
label_num2 = Label(janela, text="Valor 2:")
label_num2.place(x=30, y=50)
num2 = Entry(janela, width=20)
num2.place(x=80, y=50)
# Botão
bt = Button(janela, text="SOMAR", width=10, bg="green", command=bt_soma)
bt.place(x=100, y=80)
# Resposta
label_titulo = Label(janela, text="Resultado:")
label_titulo.place(x=32, y=120)
label_resposta = Label(janela, text=" ", width=11, borderwidth=1, relief="solid")
label_resposta.place(x=100, y=120)
janela.mainloop()
