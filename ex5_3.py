'''
1. Escreva uma função chamada is_triangle que receba três números inteiros como
argumentos, e que imprima “Yes” ou “No”, dependendo da possibilidade de formar
ou não um triângulo de gravetos com os comprimentos dados.
2. Escreva uma função que peça ao usuário para digitar três comprimentos de
gravetos, os converta em números inteiros e use is_triangle para verificar
se os gravetos com os comprimentos dados podem formar um triângulo.
'''


def is_triangle(x, y, z):
    if x < y + z and y < x + z and z < x + y:
        print('YES')
    else:
        print('NO')


x = float(input('Digite o primeiro valor:\n'))
y = float(input('Digite o segundo valor:\n'))
z = float(input('Digite o terceiro valor:\n'))

is_triangle(x, y, z)
