
import math
ang = float(input('Digite o ângulo que deseja: '))
sen = math.sin(math.radians(ang))
con = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'''
O angulo {ang} tem o SENO de {sen:.2f}      
O angulo {ang} tem o COSSENO de {con:.2f}  
O angulo {ang} tem o TANGENTE de {tan:.2f} 
      ''')