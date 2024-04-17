from random import randrange as rand
from time import sleep
print('-'*15,'JO KEN PO','-'*15)
jogador = int(input('''
Escolha uma Opção:
[1]Pedra 
[2]Papel
[3]Tesoura
'''))
sleep(1)
print('-_'*10)
sleep(1)
computador = rand(1,4)
if jogador == 1:
    print('Jogador jogou Pedra')
elif jogador ==2:
    print('jogador jogou Papel')
elif jogador == 3:
    print('jogador jogou Tesoura')
else:
    print('Jogada invalida')
sleep(1)
if computador == 1:
    print('Maquina Jogou Pedra')
elif computador ==2:
    print('Maquina Jogou Papel')
else:
    print('Maquina Jogou Tesoura')
sleep(1)
if jogador == computador:
    print('Empate')
elif jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
    print('Jogador ganhou')
else:
    print('Computador ganhou')
