#Bibliotecas
from random import randrange as rand

#Titulo

print(f'{"Palpites da Mega Sena":*^30}')
print('-='*17)


#Variáveis

lista = []
jogos = int(input('Quantos jogos você quer que eu sorteie? '))


#Gerando o programa:
    
for jogo in range(0,jogos):
    game = []
    #gerar o jogo de 6 numeros
    while len(game) < 6:
        num = rand(1,60)
        if num not in game:
            game.append(num)
            
    #adicionar a lista e organizar
    game.sort()
    lista.append(game)
    
#Apresentação dos resultados
print('-='*17)
for i, j in enumerate(lista):
    print(f'Jogo {i+1}: {j}')
print('-='*17)