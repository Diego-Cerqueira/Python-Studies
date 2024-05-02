#Bibliotecas
import time

#Funções

def voto(Ano):
    Data = time.localtime()
    Ano_atual = Data.tm_year 
    idade = Ano_atual - Ano
    if idade < 16:
        print('Negado')
    elif idade >= 18 and idade <=70:
        print('Obrigatório')
    else:
        print('Opcional')


#Titulo

print(f'{"Situação de Voto":-^30}')

#Ativação
nascimento = int(input('Ano de nascimento: '))
voto(nascimento)