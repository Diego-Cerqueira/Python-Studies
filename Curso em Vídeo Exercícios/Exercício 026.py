frase = str(input('Digite uma Frase:\n').lower())
print('A letra A parece {} na frase'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('a')))