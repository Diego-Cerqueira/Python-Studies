total_idade = 0
H_mais_velhon = ''
H_mais_velhoid = 0
tot_M = 0
for p in range (1,5):
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite idade da pessoa: '))
    sexo = (input('Digite o sexo da pessoa [H/M]: ')).upper()
    if sexo == 'H' or sexo == 'M':
        if sexo == 'H' and idade > H_mais_velhoid:
            H_mais_velhon = nome
            H_mais_velhoid = idade
        if sexo == 'M':
            tot_M +=1
        total_idade += idade
    else:
        ('Opção inválida')
print(''''
A média de idade é: {:.0f}      
O homem mais velho é: {}
O total de mulheres no grupo são:{}'''.format(total_idade /4, H_mais_velhon, tot_M))    