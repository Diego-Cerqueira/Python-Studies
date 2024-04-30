#Titulo

print(f'{"Cadastro de Pessoas":-^50}')

#Variáveis
cadastros = []
media = 0
Mulheres = []
maiores = []
#Coleta e Manipulação de Dados

while True:
    pessoa = {'Nome': 'Nome', 'Sexo': 'S', 'Idade': 0}#para limpar variável
    
    pessoa['Nome'] = str(input('Nome:'))
    
    val_sex = str(input('Sexo [F/M]:').upper())#validador se é F ou M
    while val_sex != 'F' and val_sex != 'M':
        val_sex = input('Inválido F ou M para Sexo: ').upper()
    pessoa['Sexo'] = val_sex
    
    pessoa['Idade'] = int(input('Idade: '))
    cadastros.append(pessoa)
    print(pessoa)
    #validador de continuidade
    continuar = input('Deseja continuar?[S/N]').upper()
    while continuar != 'N' and continuar != 'S':
        continuar = input('Valor incorreto [S/N]').upper()
    if continuar == 'N':
        break
    
#Manipulação de Dados

#Mulheres e cálculod e média
for p in cadastros:
    if p['Sexo'] == 'F':
        Mulheres.append(p['Nome'])
    media += p['Idade']
    
#Media
media = media/len(cadastros)

#Maiores da Média
for p in cadastros:
    if p['Idade'] > media:
        maiores.append(p)

#Apresentação

print('-='*25)
print(f'''
A) Pessoas cadastradas fora: {len(cadastros)}
B) Média de Idade é de :{media:.2f} anos   
C) Mulheres cadastradas foram: {Mulheres} 
D) Mais velhos que a média foram:''')
    
for p in maiores:
    print(f'     Nome = {p["Nome"]} Sexo = {p["Sexo"]} Idade = {p[""]}')
    

   