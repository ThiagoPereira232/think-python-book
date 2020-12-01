# 1. O volume de uma esfera com raio r é 4/3.pi.r³.
# Qual é o volume dee uma esfera com raio = a 5?

pi = 3.141592653589793
print(f'{4/3 * pi * 5 ** 3}')

'''
2. Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%.
O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavo para cada exemplar adicional.
Qual é o custo total de atacado para 60 cópias?
'''

p = 24.95 * 40/100
t = 0.75
pf = (p * 60) + 3 + (t * 59)
print(f'O preço final é {pf}')

''' 3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo
(8min15s porquilômetro), então 3 quilômetros a um passo mais rápido
(7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar,
que horas chego em casa para o café da manhã? '''

import datetime

ti = 60 * 60 * 6 + 52 * 60
t1 = ti + 8 * 60 + 15
t2 = t1 + 3 * (7 * 60 + 12)
t3 = t2 + (8 * 60 + 15)

print(f'Hora: {str(datetime.timedelta(seconds=t3))}')
