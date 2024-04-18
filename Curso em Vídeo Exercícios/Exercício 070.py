total = 0
mbarato = ''
totcaro = 0
barato = 1000000

while True:
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite valor do produto R$:'))
    
    if valor < barato:
        mbarato = nome
        barato = valor
    if valor >= 1000:
        totcaro += 1
    total += valor
    
    continuar = input('deseja continuar? tecle S')
    if continuar.upper() != 'S':
        break
print('''
A compra total foi de R${:.2f}      
{} produtos custam mais de R$1000.00
{} é o produto mais barato!'''.format(total, totcaro, mbarato))
        