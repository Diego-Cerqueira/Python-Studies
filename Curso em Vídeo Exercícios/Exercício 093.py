#Titulo
print('=-'*10+'Jogadores'+'-='*10)

#Váriaveis
jogador = {'Nome':'Nome','Gols':[],'Total':0}

#Coleta e manipulação de Dados

jogador['Nome'] = input('Nome: ')#nome
partidas = int(input('jogou quatas partidas? '))#partidas

for p in range(0,partidas): #Coleta de gols por partida
    jogador['Gols'].append(int(input(f'Quantos gols fez na partida {p}: ')))

jogador['Total'] = sum(jogador['Gols'])

#Apresentação
    #Dicionario
print('=-'*25)    
print(jogador)
print('=-'*25)  
  
    #Valores separados
print('=-'*25)    
for k,v in jogador.items():
    print(f'{k} tem o valor {v}')
print('=-'*25)    
    
    #Partidas
for g in range(len(jogador['Gols'])):
    print(f'Na partida {g+1}, fez: {jogador["Gols"][g]} ')
print(f'Foi um total de {jogador["Total"]} gols')