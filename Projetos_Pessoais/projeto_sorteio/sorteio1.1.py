from tkinter import *

# janela:
janela = Tk()
janela.title('Sorteio T-force')

# texto de boas vindas:
texto_de_boas_vindas = Label(janela, text='BEM VINDO!')
texto_de_boas_vindas.grid(column=0, row=0, padx=20, pady=10)

# texto de orientação:
texto_de_orientacao = Label(janela, text='O que você deseja fazer? ')
texto_de_orientacao.grid(column=0, row=1, padx=10, pady=5)

# botões
botao1 = Button(janela, text="Cadastrar pessoa.")
botao1.grid(column=0, row=2, padx=10, pady=5)
botao2 = Button(janela, text="Mostrar pessoas cadastradas.")
botao2.grid(column=0, row=3, padx=10, pady=5)
botao3 = Button(janela, text="Sortear.")
botao3.grid(column=0, row=4, padx=10, pady=5)
janela.mainloop()
