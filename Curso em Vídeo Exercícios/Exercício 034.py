print('-'*15,'REAJUSTE SALÁRIAL','-'*15)
salario = float(input('Digite o salárioR$:'))
if salario >1250:
    print('Com o reajuste o novo salário é de R${:.2f}'.format(salario*1.1))
else:
    print('Com o reajuste o novo salário é de R$:{:.2f}'.format(salario*1.15))