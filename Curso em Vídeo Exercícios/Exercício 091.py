# Biblioteca
from random import randrange as rand

#Titulos

print (f'{"Apostadores de dados":-^50}')


#Variável
lista = []

#gerando dados
for c in range(1,5):
    jogo = {'Jogador':f'Jogador{c}','Dado':rand(1,6)}
    lista.append(jogo)

#Organizando dados
lista.sort(key=lambda jogo: jogo['Dado'])


#Apresentação
for c in range(len(lista)):
    print(f'{c+1}° Posição: {lista[c]["Jogador"]} com o Dado {lista[c]["Dado"]}')