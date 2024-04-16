import time
data = time.localtime()
ano_atual = data.tm_year
ano = int(input('Digite o ano de nascimento: '))
alistamento = ano_atual-ano
if alistamento < 18:
    print('deve se alistar em {} anos'.format(18-alistamento))
elif alistamento == 18:
    print('Este é o ano de se Alistar')
else:
    print('Esta atrasdo {} anos para o alistamento'.format(alistamento-18))