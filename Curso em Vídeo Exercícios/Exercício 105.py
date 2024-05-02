#Funções

def notas(*args, sit = False):
    dicionario = {'Total':0}
    lista = []
    c = 1
    tot = 0
    for n in args:  
        lista.append(n) 
        c +=1 
        tot += n
    dicionario['Total'] = c-1
    dicionario['Maior'] = max(lista)
    dicionario['Menor'] = min(lista)
    dicionario['Média'] = tot/dicionario['Total']
    if sit == True:
        if dicionario['Média'] <= 5:
            dicionario['Situação'] = 'Ruim'
        elif dicionario['Média'] >5 and dicionario['Média'] <=7:
            dicionario['Situação'] = 'Médio'
        elif dicionario['Média'] > 7 and dicionario['Média']< 10:
            dicionario['Situação'] = 'Boa'
        else:
            dicionario['Situação'] = 'Muito Boa'
    print(dicionario)

notas(1.5,7.5,8.5,3.0,6.5,4.4,10, sit=True)