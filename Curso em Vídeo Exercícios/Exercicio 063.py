print('-='*5,'Sequencia Fibonacci','=-'*5)
termo = int(input('Digite o termo:'))
count = 0
atual = 1
anterior = 0
print('0 →', end=' ')
while count < termo-1:
    print(f'{atual} →', end=' ')
    proximo =  atual + anterior
    anterior = atual
    atual = proximo
    count += 1
print('FIM')
