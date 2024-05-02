from random import randrange as rand
#Funções
def sortear(lista = None):
    lista = []
    for c in range(0,5):
        lista.append(rand(1,21))
    return lista

def somar_par(lista):
    total = 0
    for c in lista:
        if c%2 == 0:
            total += c
    print(f'Somando os valores pares da lista {lista} temos {total}')

#Testando
lista = sortear()
somar_par(lista)