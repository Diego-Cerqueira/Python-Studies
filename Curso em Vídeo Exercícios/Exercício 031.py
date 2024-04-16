print('-'*15,'CALCULO DE VIAGENS','-'*15)
distancia = int(input('Digite a distância a ser viajada (km): '))
if distancia <= 200:
    print('O valor da viagem será de R${:.2f}'.format(distancia*.5))
else:
    print('O valor da viagem será de R${:.2f}'.format(distancia*.45))