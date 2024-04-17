sexo = input('Digite seu sexo [M/F]').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Valor inválido, por facor digite M ou F: ').upper()
print('Sexo é {}, Obrigado por validar'.format(sexo))
    