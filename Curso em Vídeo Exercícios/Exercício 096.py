#Função

def area(largura,comprimento):
    return largura*comprimento

#Titulo

print('Controle de Terrenos')

#Coleta de dados
largura = float(input('Digite a Largura(m): '))
altura = float(input('Digite a altura(m): '))

#Apresentação com utilização da função
print(f'A área de um terrno de {altura}m de altura e {largura}m de largura é de {area(largura,altura)}m²')


