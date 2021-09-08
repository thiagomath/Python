from tkinter import *


def bt_click():
    n = nome.get()
    label_resposta["text"] = f'É um prazer te conhecer {n}!'


# Janela
janela = Tk()
janela.title("ex001")
janela.geometry("200x200+10+10")
# Variáveis
label_nome = Label(janela, text="Olá, qual é o seu nome? ")
label_nome.place(x=30, y=20)
nome = Entry(janela, width=20)
nome.place(x=30, y=50)
# Botão
bt = Button(janela, text="OK", width=10, command=bt_click)
bt.place(x=50, y=80)
# Resposta
label_resposta = Label(janela, text=" ")
label_resposta.place(x=20, y=120)
janela.mainloop()
