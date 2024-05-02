#Função

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isdigit():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO!! Valor inválido, Digite um número inteiro válido\033[m]')
        if ok:
            break
    return valor

numero = leiaint('Digite um numero:')
print(f'O numero digitado é: {numero}')