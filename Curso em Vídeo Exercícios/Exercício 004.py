variavel = input('Digite algo: ')
print ('Qual o tipo? {}'.format(type(variavel)))
print ('Só tem espaços? {}'.format(variavel.isspace()))
print ('É um número? {}'.format(variavel.isnumeric()))
print ('É alfabetico? {}'.format(variavel.isalpha()))
print ('É Alfanumérico? {}'.format(variavel.isalnum()))
print ('Esta em Maiusculas?{}'.format(variavel.isupper()))
print ('Esta em Minúsculas?{}'.format(variavel.islower()))
print ('Esta captalizado? {}'.format(variavel.istitle()))