v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
v3 = int(input('Digite um ultimo número: '))
if v1> v2 and v1 > v3:
    print('{} é o maior'.format(v1))
elif v2>v1 and v2>v3:
    print('{} é o maior'.format(v2))
else:
    print('{} é o maior'.format(v3))