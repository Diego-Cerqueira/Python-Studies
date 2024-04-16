print('-'*15, 'IMC','-'*15)
altura = float(input('Digite a altura da pessoa(m): '))
peso = float(input('Digite o peso da pessoa (kg): '))
IMC = peso/(altura*altura)
if IMC < 18.5:
    print('IMC {:.2f}, Abaixo do Peso'.format(IMC))
elif IMC >= 18.5 and IMC <=25:
    print('IMC {:.2f}, Peso Ideal'.format(IMC))
elif IMC >25 and IMC <= 30:
    print('IMC {:.2f}, Sobrepeso'.format(IMC))
elif IMC >30 and IMC <= 40:
    print('IMC {:.2f}, Obesidade'.format(IMC))
else:
    print('IMC {:.2f}, Obesidade Morbida'.format(IMC))
    