from random import randrange as rand
n1 = rand(0,99)
n2 = rand(0,99)
n3 = rand(0,99)
n4 = rand(0,99)
n5 = rand(0,99)
tupla = (n1, n2, n3, n4, n5)

print(f'Dos valores {tupla}\nO menor valor é {min(tupla)}\nO maior valor é:{max(tupla)}')