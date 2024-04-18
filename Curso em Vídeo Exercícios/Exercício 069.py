maior18 = 0
totH = 0
totM = 0

while True:
    idade = int(input('Digite idade da pessoa:'))
    sexo = input('Digite Sexo da pessoa[M/H]:').upper()    
    while sexo != 'M' and sexo != 'H' and sexo != '':
        sexo = input('VALOR INVÀLIDO digite H ou M: ').upper()        
    if idade >= 18:
        maior18 += 1
    elif sexo == 'M' and idade < 20:
        totM += 1
    elif sexo == 'H':
        totH += 1    
    continuar = input('Deseja continuar? (S/N): ')
    if continuar.upper() != 'S':
        break
    
print(f'''
{maior18} pessoas tem mais de 18      
{totH} são homens      
{totM} mulheres tem menos de 20 anos''')