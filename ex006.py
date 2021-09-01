from math import sqrt
numero = int(input('Digite um número inteiro: '))
dobro = 2 * numero
triplo = 3 * numero
print(f'Analizando o número {numero}, temos que:')
print(f'Seu dobro é {dobro},')
print(f'Seu triplo é {triplo},')
if numero < 0:
    print(f'Este número não possui raiz quadrada real.')
else:
    raizquad = sqrt(numero)
    print(f'Sua raiz quadrada é {raizquad}.')
