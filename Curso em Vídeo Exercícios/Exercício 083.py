#Titulo

print('||| Verificador de Expressão |||')

#Váriável e coleteta de dados

lista = []
expressao = input('Digite a expressão: ')

#Tratametno de dados

for s in expressao:
    if s == '(':
        lista.append(s)
    elif s == ')':
        if len(lista) > 0:
            lista.pop() #Eliminando o conteudo da lista até 0
        else:
            lista.append(')') #Adicionando elemento, em caso de ter a mais o ')' do que '(' ele fica em 1
            break

#Apresentação
if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')

#Finalização

print('Programa sendo encerrado....')
