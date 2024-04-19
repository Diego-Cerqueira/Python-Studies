numero  = []

for c in range(0,5):
    numero.append(int(input('Digite um número: ')))

maior = max(numero)
menor = min(numero)

print(f'O maior número digitado foi {maior} na posição {numero.index(maior)+1}')
print(f'I menor número digitado foi {menor} na posição {numero.index(menor)+1}')