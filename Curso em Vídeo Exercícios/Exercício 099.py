def descobre_maior(*num):
    lista = [num]
    lista.sort
    print('=-'*25)
    print(f'Analisando os Valores passados...' )
    for c in lista[0]:
        print(c, end=' ')
    print(f'Foram informados {len(lista[0])} ao todo')
    print(f'O maior valor foi {max(lista[0])}')

descobre_maior(1,5,4,6,55,47,45,521,1,4,362)
descobre_maior(2,5,4,33,21,4,5)
descobre_maior(5)