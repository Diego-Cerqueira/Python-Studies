#Tilulo

print(f'{"-="*15}\n{"CADASTRO PESO":^30}\n{"=-"*15}')

#Variáveis

pesol = 1000
pesop = 0
pessoas = []
pessoas_pesadas = []
pessoas_leves = []

#Coleta de dados

while True:
    nome = input('Digite o nome da pessoa: ')
    peso = float(input('Digite o peso da pessoa(kg): '))

#Tratamento de dados
    pessoas.append([nome,peso])

    if peso > pesop:
        pesop = peso
    if peso < pesol:
        pesol = peso
#Validação de continuidade
    continuar  = input('Deseja continuar [S/N]: ').upper()
    while continuar not in ['S','N']:
        continuar = input('Valor inválido digite S ou N: ').upper()
    if continuar == 'N':
        break

#Organizando dados em lista
for pessoa in pessoas:
    if pessoa[1] == pesop:
        pessoas_pesadas.append(pessoa[0])
    if pessoa[1] == pesol:
        pessoas_leves.append(pessoa[0])

#Apresentação
print(f'''
Foram cadastradas {len(pessoas)}
As mais pesadas tem {pesop}Kg estas são: {pessoas_pesadas}
As mais leves tem {pesol}Kg estas são: {pessoas_leves}
''')

#Finalização
print('Programa sendo encerrado...')

