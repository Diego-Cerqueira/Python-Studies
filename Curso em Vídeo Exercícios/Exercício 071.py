print('-='*5, 'CAIXA ELETRONICO','=-'*5)
saldo = int(input('Qual o valor a ser sacado?'))
total = saldo
totced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}')
            totced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        if total == 0:
            break
