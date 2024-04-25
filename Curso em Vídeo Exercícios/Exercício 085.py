#Titulo

print(f'{"ORGANIZADOR PAR/INPAR":-^30}')

#variáveis

lista = [[],[]]


#Coleta de dados

for c in range(0,7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

#Apresetação

print(f'Os números pares digitados foram: {sorted(lista[0])}\n Os números impares foram: {sorted(lista[1])}')

#Encerramento

print('Programa sendo encerrado...')