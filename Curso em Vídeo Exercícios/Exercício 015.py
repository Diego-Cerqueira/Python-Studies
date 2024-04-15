print('-'*15,'ALUGUEL DE CARRO','-'*15)
dia = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos KMs o carro rodou?'))
valor = (dia*60) + (km*.15)
print('O carro que rodou {}km e {} dias, tem to valor total de R${:.2f}'.format(km, dia, valor))
                 