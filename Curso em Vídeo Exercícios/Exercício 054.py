import time
data = time.localtime()
ano_a = data.tm_year
maioridade = 0
print('-'*15,'Verificador de Maioridade','-'*15)
for p in range(1,8):
    ano = int(input('Digite o ano de nascimento: '))
    idade = ano_a-ano
    if idade >= 18:
        maioridade += 1
print(f'Dos anos de nascimentos adicionados {maioridade} são maior de idade')
