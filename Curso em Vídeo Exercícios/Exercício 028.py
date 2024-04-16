from random import randrange as rand
num_maquina = rand(1,6)
print('-'*15, 'DESCUBRA O NÚMERO', '-'*15)
numero = int(input('Escolha um número de 1 a 5: '))
if numero == num_maquina:
    print('Voce acertou!!!')
else:
    print ('Você Errou o número foi {}'.format(num_maquina))