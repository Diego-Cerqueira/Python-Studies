from time import sleep
print('''
==============================
      10 termos de uma PA
==============================      
      ''')
termo = int(input('Digite o termo: '))
razao = int(input('Digite razão: '))
for c in range (1,11):
    print (termo, end=' → ')
    termo += razao
    sleep(1)
print('ACABOU!!')