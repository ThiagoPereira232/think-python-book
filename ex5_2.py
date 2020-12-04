'''
O último teorema de Fermat diz que não existem números inteiros a, b e c tais
que a**n + b**n == c**n para quaisquer valores de n maiores que 2.
1. Escreva uma função chamada check_fermat que receba quatro parâmetros – a, b,
c e n – e verifique se o teorema de Fermat se mantém. Se n for maior que 2
e a**n + b**n == c**n o programa deve imprimir,“Holy smokes, Fermat was wrong!”
Senão o programa deve exibir “No, that doesn’t work.”
2. Escreva uma função que peça ao usuário para digitar valores para a, b, c
e n, os converta em números inteiros e use check_fermat para verificar se
violam o teorema de Fermat
'''


def check_fermat(a, b, c, n):
    if n > 2 and (a ** n + b ** 2 == c ** 2):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesnt work.')


a = int(input('Digite a:\n'))
b = int(input('Digite b:\n'))
c = int(input('Digite c:\n'))
n = int(input('Digite n:\n'))

check_fermat(a, b, c, n)
