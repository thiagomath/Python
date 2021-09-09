from tkinter import *


def tabuada():
    if str(num.get()).isnumeric():
        n = int(num.get())
        label_tabuada["text"] = f'''{0} X {n} = {0 * n}
{1} X {n} = {1 * n}
{2} X {n} = {2 * n}
{3} X {n} = {3 * n}
{4} X {n} = {4 * n}
{5} X {n} = {5 * n}
{6} X {n} = {6 * n}
{7} X {n} = {7 * n}
{8} X {n} = {8 * n}
{9} X {n} = {9 * n}
{10} X {n} = {10 * n}'''
    else:
        label_tabuada["text"] = 'ERRO!'


# Janela
janela = Tk()
janela.title("Tabuada")
janela.geometry("200x260")
# Variáveis
label_num = Label(janela, text="Digite um valor: ")
label_num.place(x=20, y=20)
num = Entry(janela, width=8)
num.place(x=120, y=20)
# Botão
bt_tabuada = Button(janela, text="VER TABUADA", width=15, bg="green", command=tabuada)
bt_tabuada.place(x=40, y=50)
# Resposta
label_tabuada = Label(janela, text=" ")
label_tabuada.place(x=60, y=80)
janela.mainloop()
