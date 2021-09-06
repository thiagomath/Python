# Programa para sorteio
from tkinter import *
'''import PySimpleGUI as sg'''
'''
#Layout
layout = [
    [sg.Text('Nome:'), sg.Input()],
    [sg.Button('OK')]
]

#Janela
janela = sg.Window('Janela teste', layout)

#Interação
eventos, valores = janela.Read()

#Mensagem
print(f'Olá {valores[0]}, obrigado por usar PySimpleGUI!')

#Encerramento da janela
janela.close()
'''
'''
cont = 0
participantes = dict()
for cont in range(0, 2):
    participantes["nome"] = str(input('Digite o nome do participante: '))
    participantes["numero"] = int(input('Digite o número do participante: '))
    cont += 1
    print(f'{cont} pessoas concorrendo ao sorteio!')
print(participantes)
'''
'''theme_name_list = sg.theme_list()
print(theme_name_list)'''


def pegar_cotacoes():
    texto = 'xxx'
    texto_cotacoes["text"] = texto


# Sempre inicia com:
janela = Tk()
janela.title('Sorteio T-force')
janela.geometry("400x400")
# Texto de orientação:
texto_de_orientacao = Label(janela, text='Clique no botão para ver as cotações das moedas')
# Posição do texto:
texto_de_orientacao.grid(column=0, row=0, padx=10, pady=10)
# Botão + função
botao = Button(janela, text="Buscar cotações Dólar, Euro e BTC", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)
# Texto das cotações:
texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)
# Sempre termina com:
janela.mainloop()
