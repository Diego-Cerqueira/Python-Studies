n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
escolha = 0
while escolha != 5:
    if escolha == 0:
        escolha = int(input('''
=-=-=-=-=MENU=-=-=-=-=
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do Pograma
'''))
        if escolha ==1:
            print(f'O resultado é {n1+n2}')
            escolha = 0
        elif escolha ==2:
            print(f'O resultado é {n1*n2}')
            escolha = 0
        elif escolha ==3:
            if n1 > n2:
                print(f'{n1} é maior')
                escolha = 0
            elif n2 > n1:
                print(f'{n2} é maior')
                escolha = 0
            else:
                print('Os dois são iguais')
                escolha = 0
        elif escolha == 4:
            n1 = float(input('Digite um número:'))
            n2 = float(input('Digite outro número:'))
            escolha = 0
        elif escolha == 5:
            print('Obrigado por participar')
        else:
            escolha = 0
