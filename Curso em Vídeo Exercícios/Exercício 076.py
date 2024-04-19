#Título
print('''
-------------------------------------
          LISTA DE PRODUTOS
-------------------------------------''')

#Produtos
tupla = ('Lapiz', 1.00,
            'Caderno', 15.45,
            'Borracha', 0.50,
            'Caneta', 1.50,
            'Estojo', 5.50)

#Execução
for u in range(0,len(tupla)):
    if u % 2 == 0:
        print(f'{tupla[u]:.<30} R${tupla[u + 1]:.2f}')