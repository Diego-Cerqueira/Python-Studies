('-'*15,'ANALISANDO TRIÂNGULOS','-'*15)
l1 = float(input('Digite medida do primeiro lado: '))
l2 = float(input('Digite mediade do segundo lado: '))
l3 = float(input('Digite medida do terceiro lado: '))
if l1 + l2 >= l3 and l2 + l3 >= l1 and l3 + l1 >= l2: 
    if l1 ==l2 == l3:
        print('É um triângulo EQUILÁTERO')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('É um triângulo ISÓCELES')
    elif l1 != l2 != l3:
        print('É um triângulo ESCALENO')
else:
    print('Não é um triângulo')