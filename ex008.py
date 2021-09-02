medida = float(input('Digite uma medida em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f'A medida de {medida:.2f} m corresponde a:')
print(f'{mm}mm')
print(f'{cm}cm')
print(f'{dm}dm')
print(f'{dam}dam')
print(f'{hm}hm')
print(f'{km}km')
