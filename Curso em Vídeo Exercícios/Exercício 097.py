#Função

def texto(texto):
    tamanho = len(texto)+4
    print('~'*tamanho)
    print(f'{texto:^{tamanho}}')
    print('~'*tamanho)

texto('Diego Cerqueira da Silva')

texto('Olá Mundo!!')

texto('Testando 123')    

texto('DEV')