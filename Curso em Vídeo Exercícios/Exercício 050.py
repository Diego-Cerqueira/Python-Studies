tot = 0
for c in range (1,7):
    num = int(input('Digite um numero inteiro: '))
    if num%2 == 0 :
        tot += num
print ('O total dos números pares foi {}'.format(tot))