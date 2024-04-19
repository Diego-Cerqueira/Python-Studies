# Times baseados na data 19/04/2024
time = ('Flamengo','Internacional','Juventude','Bragantino','Cruzeiro',
        'Fortaleza','Athletico-PR','Grêmio','Vasco da Gama','Bahia',
        'Botafogo','Palmeiras','Criciúma','Atlético Mineiro','Fliminense'
        'Corinthians','Vitória','São Paulo','Atlético Goiano','Cuiabá')

print(f'Os cinco primeiros são: \n\n{time[0:4]}')
print(f'\nOs quatro últimos são: \n\n{time[-1:-5:-1]}')
print(f'\nEm ordem Alfabética ficam: \n\n{sorted(time)}\n')

for elemento in time:
    if 'Chapecoense' in elemento:
        print(f'O Chapecoense esta na posição {elemento}')
        break
    else:
        print('Chapecoense não esta entre os 20 colocados')
        break
