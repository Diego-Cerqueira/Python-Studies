#Titulo

print('^v'*30+'\n'+f'{"Cadastro de trabalho":^60}'+'\n'+'^v'*30)

#Váriaveis
cadastro = {'nome': 'nome', 'ano nascimento':0, 'carteira':0 }

#Coleta de Dados

cadastro['Nome'] = input('Nome:')
cadastro['Ano nascimento'] = int(input('Ano de nascimento: '))
cadastro['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))

#Se tiver carteira

if cadastro['Carteira'] != 0:
    cadastro['Ano trabalho'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = 70- (cadastro['Ano trabalho'] - cadastro['Ano nascimento'])
print('-='*30)

#Apresentação resultado
for k, v in cadastro.items():
    print(f'  - {k} tem valor {v}')