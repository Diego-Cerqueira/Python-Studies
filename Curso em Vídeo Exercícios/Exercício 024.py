cidade = input('Digite o nome de sua cidade: ').upper()
nome = cidade.split()[0]
check = nome == 'SANTO' or nome == 'SAO' or nome == 'SÃO'
print(check)