print('-'*15,'É TRIÂNGULO?','-'*15)
l1 = float(input('Digite primeiro ládo do triángulo: '))
l2 = float(input('Digite segundo lado do triângulo: '))
l3 = float(input('Digite terceiro lado do triângulo: '))
if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
    print('Não é um triângulo')
else:
    print('É um triângulo')