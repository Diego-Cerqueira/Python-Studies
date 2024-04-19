tupla = ( 'Manjericao','Alface', 'Tomate', 'Rucula', 'Almeirao')

for p in tupla:
    print(f'Na Palavra {p} temos:', end=' ')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')
    print('')