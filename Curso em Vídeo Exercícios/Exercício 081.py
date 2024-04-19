#Importação de biblioteca
from time import sleep

#Título
print('-='*5,'Listando Números','=-'*5)

#Variáveis
lista = []

#Adquirindo Dados
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    continuar = input('Deseja continuar?[S/N]').upper()
    
#validação de continuação
    while continuar not in ['S','N']:
        continuar = input('Valor inválido S ´para sim e N para não').upper()
    if continuar == 'N':
        break

#Tratando os dados adquiridos
    #Contagem de números na lista
totnum = len(lista)
    
    #Lista decrescente
decre = []
for n in lista[-1::-1]:
    decre.append(n)
    
    #Validação de cinco
if 5 in lista:
    check5 = True
else:
    check5 = False
    
#Apresentação
sleep(1)
print(f'\nO total de números digitados foram: {totnum}')
sleep(1)
print(f'\nA lista invertida fica:\n{decre}')
sleep(1)
print(f'\nTem 5 na lista? {check5}')
    