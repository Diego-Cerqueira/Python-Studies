count = 0
tot = 0
while True:
    numero = int(input('Digite um número [999 para]:'))
    if numero == 999:
        break
    else:
        tot += numero
        count += 1
print('Foram digitados {} números e a soma deles foi de {}'.format(count, tot))