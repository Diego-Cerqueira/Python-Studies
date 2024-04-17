print('-'*25, 'INDENTIFICADOR DE NÚMEROS PRIMOS', '-'*25)
primo = int(input('Digite o número a verificar: '))
tot = 0
for c in range (2,primo+1):
    if primo%c == 0:
        tot +=1
print ('O número {} foi dividido um total de {} vezes '.format(primo,tot))
if tot <=1:
    print('Por isto É NÚMERO PRIMO')
else:
    print('Por isto NÂO É NÚMERO PRIMO')