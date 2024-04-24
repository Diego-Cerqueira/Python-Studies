import banco
  #Váriáveis de funcionamento:
extrato = []
saldo = float(0)
NUM_SAQUE = 0
lista_usuario = []
lista_conta = []
   #Programa rodando
while True:
    
    #Menu
    escolha = input("""
-=-=-=-=-=-=-=-=-=-=-=-=-
         MENU
-=-=-=-=-=-=-=-=-=-=-=-=-
[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Cadastro
[0] - Sair
-=-=-=-=-=-=-=-=-=-=-=-=-
Opção: """)
    
    #Deposito
    if escolha == '1':
        deposito = float(input('Digite o valor a depoistar.\nR$: '))
        saldo = banco.deposito(saldo, deposito)
        extrato =  banco.extrato(deposito, Extrato = 'Deposito',extrato_list = extrato)
    
    #Saque    
    elif escolha == '2':
        saque = float(input('Digite o valor a Sacar\nR$:'))
        saldo,NUM_SAQUE = banco.saque(saldo = saldo,NUM_SAQUE= int(NUM_SAQUE) , val_saque = saque)
        extrato = banco.extrato(saque , Extrato = 'Saque',extrato_list = extrato)
    
    #extrato
    elif escolha == '3':
        banco.historico_extrato(extrato,saldo)
   
   #cadastros 
    elif escolha == '4':       
        Menu_C = input(f'{"MENU CADASTRO":*^30}\n[1]Para Cliente\n[2]Para conta\n[0]Voltar\n{"":*^30}\n')
        if Menu_C == '1':
            lista_usuario = banco.cadastro_usuario(lista_usuario, input('Digite o nome: '),
                                   banco.dt_nascimento(int(input('Dia: ')),
                                                        int(input('Mês: ')),
                                                        int(input('Ano: '))),
                                                   (input('Digite o CPF:')),
                                                   banco.CEP(input('Rua:'),
                                                             input('Bairro:'),
                                                             input('Cidade: '),
                                                             input('Estado:').upper()))

    #Cadastros de Contas:
        elif Menu_C == '2':
            CPF = (input('Digite o CPF de cadastro:'))
            lista_conta = banco.cadastro_conta(lista_usuario, CPF, lista_conta)
        
    #sair
    elif escolha =='0':
        break
    
   #Error 
    else:
        print('Opção Inválida!!')
print(saldo)