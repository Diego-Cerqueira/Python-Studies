print('-'*15,'VERIFICADOR DE DESCONTOS','-'*15)
produto = float(input('Digite o valor do produto R$:'))
fdpagamento = int(input('''
FORMA DE PAGAMENTO                        
[1]DINHEIRO                      
[2]CHEQUE                        
[3]CARTÃO'''))
if fdpagamento == 1 or fdpagamento == 2:
    print('O valor do produto fica {:.2f}'.format(produto*.9))
elif fdpagamento ==3:
    x = int(input('Em quantas vezes? '))
    if x == 1:
        print('O valor do produto fica R${:.2f}'.format(produto*0.95))
    elif x == 2:
        print('O valor do produto fica R$:{:.2f}'.format(produto))
    else:
        print('O valor do produto fica R$:{:.2f}'.format(produto*1.2))
else:
    print('Método de pagamento inválido')