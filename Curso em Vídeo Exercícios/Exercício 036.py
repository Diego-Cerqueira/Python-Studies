print('-'*15,'APROVANDO EMPRÉSTIMO','-'*15)
casa = float(input('Digite o valor da casa R$:'))
salario = float(input('Digite o salário R$:'))
periodo = int(input('Quantos anos de financiamento: '))
parcelas = casa/(periodo*12)
if parcelas > (salario*0.3):
    print('''
Para pagar uma casa de {} em {} anos, o valor das parcelas será de R${:.2f}
Emprestimo NEGADO!!!'''.format(casa, periodo, parcelas))
else:
    print('Para pagar uma casa de {} em {} anos, o valor das parcelas será de R${:.2f}\nEmprestimo APROVADO!!!'.format(casa, periodo, parcelas))