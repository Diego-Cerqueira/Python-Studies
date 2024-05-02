#Funções

def ficha(nome = '<Desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols}(s) no campeonato')

#Programa Principal
n = input('Nome do jogador: ')
g = input('gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)