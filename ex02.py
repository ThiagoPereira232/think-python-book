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
