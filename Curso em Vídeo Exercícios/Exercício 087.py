#Titulo
print(f'{"Matrizes 2.0":+^30}')

#Variáveis
lista = [[],[],[]]
totp = 0
tot3c = 0

#Coleta de Dados

for n in range(0,3):
    for c in range(0,3):
        numero = int(input(f'Digite um valor para {[n,c]}'))
        lista[n].append(numero)

#Cálculo das solicitações pedidas:
    
for l in lista:
    for n in l:
        if n % 2 == 0: #Verifica se é Par e soma em totp
            totp += n 
    tot3c += l[2]  #Soma o segundo intem de cada lista em lista(coluna do meio)
tot2l = sum(lista[1]) #soma todos os itens da terceira lista(3° linha)

#Apresentação Matriz:

for l in lista:
    for c in l:
        print(f'[{c:^5}]', end=' ')
    print('')

#Apresentação

print(f'''
A soma de todos pares é: {totp}   
A soma dos números da terceira coluna é: {tot3c}
A soma dos números da segunda Linha é: {tot2l}''')        

#Encerramento

print('Programa sendo finalizado')

