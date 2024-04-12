SAQ_DAY = int(0)
Extrato = []
saldo = float(0)
while True:
    escolha = input("""
--------------Menu-------------
[0]Depositar
[1]Sacar
[2]Extrato
[3]Sair
-------------------------------             
           """)
    if escolha == '0':
        val_dep = float(input('Quanto vai depositar?'))
        if val_dep < 0:
            print('VALOR INVÁLIDO!!!')
        else:
            saldo += val_dep
            Extrato.append('Foi depositado R$:{:.2f}'.format(val_dep))
    elif escolha == '1':
        val_saq = float(input('Quanto vai sacar?'))
        if SAQ_DAY > 2:
            print('''              
           BLOQUEADO!!!
 Limite de saque 3 vezes por dia Excedido
                  ''')    
        elif val_saq < 0:
            print('VALOR INVÁLIDO!!!')
        elif val_saq > 500:
            print('Valor máximo R$500,00')
        elif val_saq > saldo:
            print('Saldo insuficiente!! Você tem R$:{:.2f}'.format(saldo))
        else:
            saldo -= val_saq
            SAQ_DAY += 1
            Extrato.append('Foi sacado R$:{:.2f}'.format(val_saq))
    elif escolha =='2':
        for i in (Extrato):
            print(i)
        print(f'Seu saldo é {saldo}')
    elif escolha == '3':
        break
    else:
        print('Escolha inválida')
print(f'''
------Programa encerrado-------
Saldo Atual R$:{saldo}
-------------------------------
Ogbrigado pela Preferência
      ''')