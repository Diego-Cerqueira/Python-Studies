
numero = int(input('Digite um número: '))
tot = numero
cont = 0
while numero != 999:
    numero = int(input('Digite outro número [999 Para]: '))
    tot = tot + numero
    cont +=1
tot = tot-999
print('Foram digitados {} números e o total deles foi de {}'.format(cont, tot))