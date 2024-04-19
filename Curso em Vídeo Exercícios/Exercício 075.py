n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
tupla = (n1, n2, n3, n4)

print(f'A quantidade de números 9 digitados é: {tupla.count(9)}')
if 3 in tupla:
    print(f'A primiera posição do 3 digitado é: {tupla.index(3)+1}')
print('Os números pares digitados foram:', end=' ')

#Verificação e apresentação de pares
for n in tupla:
    if n%2 == 0:
        print(n, end= ' ')
