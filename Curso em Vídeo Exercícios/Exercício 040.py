nome = (input('Digite o nome do aluno: '))
n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a nota do segundo semestre: '))
media = (n1+n2)/2
if media < 5:
    print('A media de {} foi {} esta REPROVADO!!'.format(nome,media))
elif media >= 5 and media < 7:
    print('A media de {} foi {} esta em RECUPERAÇÃO'.format(nome,media))
else:
    print('A média de {} foi {} esta APROVADO!!!'.format(nome,media))