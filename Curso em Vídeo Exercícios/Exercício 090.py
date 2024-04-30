#Titulo
print (f'{"Médias":-^30}')

#Variáveis

aluno = dict()

#Coleta de Daodos
aluno['Nome'] = str(input('Nome:'))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}:'))

#Manipulação de Dados

if aluno['Media'] > 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Media'] > 5 and aluno['Media'] <=7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
    
#Apresetnação
print('-'*30)
for k,v in aluno.items():
    print(f'{k} é igual a {v}')