print('-='*5,'Gerador de PA','=-'*5)
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
count = 0
ponto = termo
c = 0
while count < 10:
    print(f'{ponto} →', end=' ')
    count+=1
    ponto += razao
    c +=1
    termo = 1
while termo != 0:
    print('Pausa')
    count = 0
    termo = int(input('Quantos termos você quer comprar mais? '))
    while count < termo:
        print(f'{ponto} →', end=' ')
        count +=1
        ponto += razao
        c +=1
print(f'Progressão finalizada com {c} termos mostrados')