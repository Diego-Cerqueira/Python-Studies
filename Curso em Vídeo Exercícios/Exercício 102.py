#Função

def fatorial(numero,show = True):
    count = 1
    if show == True:
        while numero > 1:
            print(f'{numero} x', end=' ')
            count *= numero
            numero-=1
        print(f'1 = {count}')
    else:
        while numero > 1:
            count *= numero
            numero-=1
        print(count)  

#Ativando o programa
fatorial(5)