import time
data = time.localtime()
ano_atual = data.tm_year
ano = int(input('Digite o ano de nascimento: '))
idade = ano_atual-ano
if idade <= 9:
    print('A categoria é MIRIM')
elif idade > 9 and idade<=14:
    print('A categoria é INFANTIL')
elif idade >14 and idade <=19:
    print('A categoria pe JUINOR')
elif idade > 19 and idade <= 25:
    print('A categoria é SENIOR')
else:
    print('A categoria é MASTER')