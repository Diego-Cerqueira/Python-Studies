from random import randrange as rand
from time import sleep
print('-='*5,'JOGO PAR OU IMPAR','=-'*5)
count = 0
sleep(1)
while True:
    jogador = int(input('[1] Par\n[2] Impar'))
    sleep(.5)
    if jogador == 1:
        computador = 2
    elif jogador == 2:
        computador = 1
    else:
        print('Escolha inválida!')
    numero = rand(1,3)
    sleep(.5)
    if jogador == numero:
        print('Você acertou!!')
        count +=1
    else:
        print('computador acertou')
        break
sleep(.5)
print(f'Você Acertou {count} consecutivas!!')
sleep(.5)
print('Finalizando programa...')