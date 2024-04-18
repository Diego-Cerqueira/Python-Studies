continuar = False
maior = 0
menor = 100000000000
tot = 0
while continuar != True:
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    tot = tot + numero
    continuar = bool(input('Para continuar digite Enter: '))
print(f'Dos números citados {maior} foi o maior {menor} foi o menor e a soma total foi de {tot}')