from tkinter import *


def bt_media():
    if str(nota1.get()).isnumeric() and str(nota2.get()).isnumeric():
        n1 = float(nota1.get())
        n2 = float(nota2.get())
        media = (n1 + n2) / 2
        label_resposta_media["text"] = f'{media:.2f}'
    elif "." in nota1.get() or nota2.get():
        n1 = float(nota1.get())
        n2 = float(nota2.get())
        media = (n1 + n2) / 2
        label_resposta_media["text"] = f'{media:.2f}'
    else:
        label_resposta_media["text"] = 'Erro!'


# Janela
janela = Tk()
janela.title("Média")
janela.geometry("250x200")
# Variáveis
# Nota 1
label_nota1 = Label(janela, text="Nota 1:")
label_nota1.place(x=30, y=20)
nota1 = Entry(janela, width=20)
nota1.place(x=80, y=20)
# Nota 2
label_nota2 = Label(janela, text="Nota 2:")
label_nota2.place(x=30, y=50)
nota2 = Entry(janela, width=20)
nota2.place(x=80, y=50)
# Média
bt_media = Button(janela, text="OK:", width=10, bg="yellow", command=bt_media)
bt_media.place(x=100, y=80)
label_resposta_titulo = Label(janela, text="Média:")
label_resposta_titulo.place(x=30, y=120)
label_resposta_media = Label(janela, text=" ", width=8, borderwidth=1, relief="solid")
label_resposta_media.place(x=80, y=120)
janela.mainloop()
