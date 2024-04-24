from random import randint as rand
def saque(saldo = None, NUM_SAQUE = 0 , val_saque = None): #Função Saque

    if val_saque is None or val_saque <= 0:                  #Validador 1
        print('VALOR INVÁLIDO!!!')
    elif val_saque > saldo:             #Validador 2
        print(f'SALDO INSUFICIENTE!!\n Seu saldo é de R$:{saldo}')
    elif NUM_SAQUE >= 3:                 #Validador 3
        print('Limite de 3 saques diários excedido!!')
    else:                               #Validado adiciona ao saldo

        saldo -= val_saque
        NUM_SAQUE += 1

    return saldo, NUM_SAQUE


def deposito(saldo, val_deposito): #função depósito  
 
   if val_deposito <=0:            #Validador 1
        print('VALOR INVÁLIDO!!!')
        val_deposito = float(input('Quanto deseja depositar?\nR$:'))
   else:
        saldo += val_deposito #adição de saldo

   return saldo
    
    
def extrato(saldo, Extrato = 'None',extrato_list = None):
    if extrato_list is None:
        extrato_list = []
    transacao = (f'Foi feito um {Extrato} de R${saldo:.2f}')
    extrato_list.append(transacao)
    return extrato_list

def historico_extrato(lista,saldo):
    for transacao in lista:
        print(transacao)
    print(f'Saldo R$:{saldo:.2f}')

def cadastro_usuario(lista_usuario, nome: str ,nascimento: list,cpf: int,endereco: list):
 
    #Validação de cpf existente
    for usuario in lista_usuario:
        if usuario[2] == cpf:
            raise ValueError('CPF já cadastrado') 

    #adicionando cadastro
    novo_usuario = [nome, nascimento, cpf, endereco]
    lista_usuario.append(novo_usuario)
    print('Usuário cadastrado com sucesso')
    return lista_usuario

def dt_nascimento (d,m,a):
    return (f'{d}/{m}/{a}')

def CEP(Rua,Bairro,Cidade,Estado):
    e_disponivel = ["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"]
    while Estado not in e_disponivel:
        print('Estado inválido')
        Estado = input('Digite estado: ').upper()
    return[Rua,Bairro,Cidade,Estado]    

def cadastro_conta(lista_usuario, usuario, lista_conta):
    # Verificação de existência de usuários na lista
    if len(lista_usuario) == 0:
        raise ValueError('Nenhum usuário cadastrado')
    
    # Procurando o usuário na lista
    for user in lista_usuario:
        if usuario == user[2]:
            agencia = '0001'
            n_conta = rand(1000000, 9999999)
            while n_conta in lista_conta:
                n_conta = rand(1000000, 9999999)
                
            # Cadastro de conta caso o usuário exista
            lista_conta.append((agencia, n_conta, usuario))
            return lista_conta
    
    # Retorno de exceção caso o usuário não seja encontrado
    raise ValueError('Usuário Inexistente')