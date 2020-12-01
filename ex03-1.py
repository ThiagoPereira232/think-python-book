''' Escreva uma função chamada right_justify, que receba uma string chamada s como
parâmetro e exiba a string com espaços suficientes à frente para que a última letra da
string esteja na coluna 70 da tela'''


def right_justify(s):
    ns = s
    while len(ns) < 70:
        ns += s
    return ns


print(right_justify('monty'))
