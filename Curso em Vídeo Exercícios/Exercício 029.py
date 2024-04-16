vel = int(input('Digite a velocidade do Carro: '))
if vel > 80:
    multa = (vel-80)*7
    print('A multa vai ser de R$:{:.2f}'.format(multa))
else:
    print('Dentro da velocidade permitida')