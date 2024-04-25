# Título

print(f'{"MATRIZ":+^30}')

#Variáveis
    
lista = [[],[],[]]

#Coleta de dados:
    
for n in range(0,3):
    for c in range(0,3):
        numero = int(input(f'Digite um valor para {[n,c]}'))
        lista[n].append(numero)
        

#Apresentação

for l in lista:
    for c in l:
        print(f'[{c:^5}]', end=' ')
    print('')
    
#Encerramento
print('Obrigado por participar')