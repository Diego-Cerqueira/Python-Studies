#Titulo
print('-='*15)
print(f'{"ORGANIZADOR DE NÙMEROS":^30}')
print('-='*15)

#Variável Extrerna
lista = []

#Entrada de números
while True:
    numero = int(input('Digite um número: '))

#Verificação de números na lista    
    if numero in lista:
        print('Número Já existente')
    else:
        print('Número Registrado com Sucesso!!')
        lista.append(numero)
    continuar  = input('Deseja Continuar [S/N]: ').upper()

#Validação de continuidade    
    while continuar not in ['S', 'N']:
        continuar = input('Valor inválido, Digite S para sim  ou N para não:').upper()        
    if continuar == 'N':
        break
    
#Apresentação Final    
print(f'Em ordem númerica estes foram os valores digitados:\n {sorted(lista)}')
print('Programa sendo encerrado ......')