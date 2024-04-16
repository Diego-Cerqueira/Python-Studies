nome = input('Digite seu nome completo: ')
total_char = sum(1 for char in nome if char != ' ')
p_nome = nome.split()[0]
print(f'''
Analisando seu código...
Seu nome em maiuscúlo é {nome.upper()}
Seu nome em mínusculo é {nome.lower()}
Seu nome tem um total de {total_char} caracteres
Seu primeiro nome tem {len(p_nome)} letras
''')