numero = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
escolha = int(input('Escolha um número de 0 a 20:'))

if escolha >= 0 and escolha <= 20:
    print(f'Você Digitou o número: {numero[escolha]}')
else:
    print('Opção inválida')