nome = str(input('Digite seu nome: '))
print(f'É um prazer te conhecer {nome}!')
idade = int(input('Qual é a sua idade? '))
if idade <= 25:
    print('Tá novo ainda!')
elif 25 < idade <= 40:
    print('Tá ficando velhinho!')
else:
    print('Aproveta a vida chefe!')
    