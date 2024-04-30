#Titulo
print('=-'*10+'Jogadores'+'-='*10)

#Váriaveis
jogadores = []

#Coleta e manipulação de Dados
while True:
    jogador = {'Nome':'Nome','Gols':[],'Total':0}
    jogador['Nome'] = input('Nome: ')#nome
    partidas = int(input('jogou quatas partidas? '))#partidas

    for p in range(0,partidas): #Coleta de gols por partida
        jogador['Gols'].append(int(input(f'Quantos gols fez na partida {p}: ')))

    jogador['Total'] = sum(jogador['Gols'])
    
    jogadores.append(jogador)
    #Validador de Continuidade:
    continuar = input('Deseja continuar?[S/N]:').upper()
    while continuar != 'N'and continuar != 'S':
        continuar = input('Valor inválido!! deseja continuar?[S/N]').upper()
    if continuar == 'N':
        break



#Apresentação
    #Tabela de Jogadores
print('=-'*25)
print('-'*50)
print(f'{"Cod":<5}{"Nome":<15}{"Gols":^20}{"Total":>10}')

i = 0
jg = len(jogadores)
for j in jogadores:
    print(f'{i:<5}{j["Nome"]:<15}{str(j["Gols"]):^20}{j["Total"]:>10}')
    i +=1
print('-'*50)  

while True:
    
    escolha = int(input('Vizualizar dados de qual jogador?(999 para parar):'))
    if escolha == 999:
        break
    if escolha >= jg:
        print('Indisponivel')
        continue
    
    player = jogadores[escolha]
    print('-'*50)
   
    print(f'Levantamento do jogador {player["Nome"]}')
    for partida, gols in enumerate(player['Gols'], 1):
        print(f'Na partida {partida}, fez: {gols}')
    
    print('-'*50) 
#Encerramento

print('Programa encerrando')