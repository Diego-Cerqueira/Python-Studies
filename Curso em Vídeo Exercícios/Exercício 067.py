from time import sleep
print('-='*5,'Tabuada V.3','=-'*5)
numero = int(input('Digite um número: '))
while True:
    if numero > 0:
        for c in range(1,11):
            print(f'{c}x{numero} = {c*numero}')
            sleep(.5)
    else:
        break
    numero = int(input('Deseja continuar? (negativo encerra)'))
print('Programa Encerrando...')