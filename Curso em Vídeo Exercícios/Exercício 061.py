from time import sleep
print('-='*5,'Gerador de PA','=-'*5)
termo = int(input('Primeiro termo: '))
rasao = int(input('Razão: '))
count = 0
ponto = termo
while count < 10:
    sleep(1)
    print(f'{ponto} →', end=' ')
    count += 1
    ponto += rasao
print('FIM')