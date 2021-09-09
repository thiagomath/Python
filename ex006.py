from tkinter import *


def dobro():
    n = float(valor.get())
    d = 2 * n
    label_resposta_dobro["text"] = f'{d:.2f}'


def triplo():
    n = float(valor.get())
    t = 3 * n
    label_resposta_triplo["text"] = f'{t:.2f}'


def raizquad():
    from math import sqrt
    n = float(valor.get())
    rquad = sqrt(n)
    label_resposta_raiz_quad["text"] = f'{rquad:.2f}'


# Janela
janela = Tk()
janela.title("Mini Calculadora")
janela.geometry("230x200")
# Variáveis
# Valor
label_valor = Label(janela, text="Valor:")
label_valor.place(x=30, y=20)
valor = Entry(janela, width=20)
valor.place(x=70, y=20)
# Botão dobro
bt_dobro = Button(janela, text="DOBRO:", width=10, bg="yellow", command=dobro)
bt_dobro.place(x=30, y=50)
label_resposta_dobro = Label(janela, text=" ", width=8, borderwidth=1, relief="solid")
label_resposta_dobro.place(x=120, y=54)
# Botão triplo
bt_triplo = Button(janela, text="TRIPLO:", width=10, bg="green", command=triplo)
bt_triplo.place(x=30, y=80)
label_resposta_triplo = Label(janela, text=" ", width=8, borderwidth=1, relief="solid")
label_resposta_triplo.place(x=120, y=84)
# Botão raiz quadrada
bt_raiz_quad = Button(janela, text="RAIZ QUADRADA:", width=14, bg="red", command=raizquad)
bt_raiz_quad.place(x=30, y=110)
label_resposta_raiz_quad = Label(janela, text=" ", width=8, borderwidth=1, relief="solid")
label_resposta_raiz_quad.place(x=148, y=114)
janela.mainloop()
