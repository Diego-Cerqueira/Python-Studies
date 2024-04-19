#Titulo
print('''
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        Cadastro de números
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ''')

#Váriável
lista =[]
#Inicio

for c in range (0,5):
    numero = int(input('Digite um número: '))
    inserido = False 
    for indice, n in enumerate(lista): #Verificação de posições
        if numero <=n:
            lista.insert(indice, numero) #inserindo na lista (posição , valor)
            inserido = True
            break
    if not inserido: #Se esta sem número adiciona o número
        lista.append(numero)

#Apresentação
print(f'A os números digitados em ordem numpérica é:\n {lista}')