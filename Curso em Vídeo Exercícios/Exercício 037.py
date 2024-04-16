numero = int(input('Digite um número inteiro: '))
menu = int(input('''
Escolha uma das opções:
[1]Converter para Binário                 
[2]Converter para Octal
[3]Converter para Hexadecimal              
Sua Opção: '''))
if menu == 1:
    binario = bin(numero)[2:]
    print('O numero em Binário é {}'.format(binario))
elif menu ==2:
    octal = oct(numero)[2:]
    print('O número em Octal é: {}'.format(octal))
elif menu == 3:
    hexadecimal = hex(numero)[2:]
    print('O número em Hexadecimal é: {}'.format(hexadecimal))
else:
    print('Escolha inválida')