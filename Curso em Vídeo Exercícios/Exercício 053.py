print('-'*15, 'Detector de Palíndromo','-'*15)
palavra = input('Digite uma palavra: ')
poli = palavra[-1::-1]
print(f'A palavra {palavra} ao contrario fica {poli} portanto', end=' ')
if palavra == poli:
    print('é um Palíndromo')
else:
    print('não é um Palíndromo')
