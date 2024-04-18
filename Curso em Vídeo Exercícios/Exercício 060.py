from time import sleep
print('-'*15,'CAUCULO E FATORIAL','-'*15)
f = int(input('Digite o numero:'))
count = 1
print(f'{f}! ', end=' ')
while f > 1:
    sleep(1)
    print(f'{f} x', end=' ')
    count *= f
    f-=1
sleep(1)
print(f'1 = {count}')
