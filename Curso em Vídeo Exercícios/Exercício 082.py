#Titulo
print('#_'*5,'SEPARANDO LISTAS','_#'*5)

#Váriável
lista = []

#Adquirindo Dados

while True:
    numero = int(input('Digite um número:'))
    lista.append(numero)
    
 #Validação de continuidade   
    continuar = input('Deseja continuar?[S/N]: ').upper()
    if continuar not in ['S','N']: #Se valor não for S ou N
         continuar = input('VALOR INCORRETO digite [S ou N]: ').upper()
    if continuar == 'N': # Se valor for N sai do Loop
        break    
    
#Manipulação de Dados
listpar = []
listimpar = []

for n in lista:
    if n%2 == 0:
        lis

    