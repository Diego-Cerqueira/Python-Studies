mais = 0
menos = 1000
for p in range(1,6):
    peso = float(input('Digite o peso da pessoa(kg): '))
    if peso > mais:
        mais = peso
    elif peso < menos:
        menos = peso
    else:
        print('Valor inválido')
print(f'O mais pesado pesa {mais} e o mais leve pesa {menos}')    