from tkinter import *


def conversor():
    if str(valor.get()).isnumeric():
        v = float(valor.get())
        d = v / 5.25
        label_resultado["text"] = f'$ {d:.2f}'
    elif '.' in valor.get():
        v = float(valor.get())
        d = v / 5.25
        label_resultado["text"] = f'$ {d:.2f}'
    else:
        label_resultado["text"] = 'Erro!'


# Janela
janela = Tk()
janela.title("Conversor")
janela.geometry("250x200")
# Variáveis
label_valor = Label(text="Quanto dinheiro você tem na carteira?")
label_valor.place(x=20, y=30)
label_valor1 = Label(text="R$:")
label_valor1.place(x=80, y=60)
valor = Entry(janela, width=8)
valor.place(x=110, y=60)
# Botão
bt_conversor = Button(janela, text="Converter para dolar", width=20, bg="red", command=conversor)
bt_conversor.place(x=60, y=90)
# Resposta
label_resultado = Label(janela, text=" ")
label_resultado.place(x=110, y=130)
janela.mainloop()
