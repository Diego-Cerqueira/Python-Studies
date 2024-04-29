#Titulo

print(f'!!{"Boletim":-^30}!!')

#Variáveis
Classe = []
escolha = 0

#Coleta de dados:
    
while True:
    Aluno = []
    nome = input('Aluno: ')
    Aluno.append(nome)
    nota1 = float(input('Nota1: '))
    Aluno.append(nota1)
    nota2 = float(input('Nota2: '))
    Aluno.append(nota2)
    Classe.append(Aluno)
    
    #verificação de continuidade
    
    continuar = input('Deseja continuar?[S/N]: ').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Valor Inválido, Digite [S/N]: ').upper()
    if continuar == 'N':
        break
        
#Apresentação
print('=-'*30+'=')
print(f'{"No. ":<3}{"NOME":<20}{"MÉDIA":<7}')
print('-'*30)
 #Alunos
for c, a in enumerate(Classe):
    media =  (a[1] + a[2]) /2
    media1 = (f'{media:.1f}')
    print(f'{c:<4}{a[0]:<20}{media1:<7}')
    
print('-'*30)

#Checagem de alunos

while escolha != 999:
    escolha = int(input('Mostrar nota de Qual Aluno?(999 interrompe) '))
    if escolha == 999:
        break
    print(f'Notas de {Classe[escolha][0]} são {Classe[escolha][1]} e {Classe[escolha][2]}')


