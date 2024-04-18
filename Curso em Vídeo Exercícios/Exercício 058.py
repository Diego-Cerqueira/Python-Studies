from random import randrange as rand
print('-'*15,'JOGO DE ADIVINHAÇÂO','-'*15)
computador = rand(1,11)
jogador = 0
count = 0
while jogador != computador:
    jogador = int(input('Digite um numero de 1 a 10:'))
    count +=1
print(f'Foram {count} jogadas para adivinhar o número')