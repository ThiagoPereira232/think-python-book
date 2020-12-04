''' 1. Escreva uma função chamada square que receba um parâmetro chamado t,
que é um turtle. Ela deve usar o turtle para desenhar um quadrado.
Escreva uma chamada de função que passe bob como um argumento para o square e
então execute o programa novamente.
2. Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para
que o comprimento dos lados seja length e então altere a chamada da função
para fornecerum segundo argumento. Execute o programa novamente. Teste o
seu programa com uma variedade de valores para length.
3. Faça uma cópia do square e mude o nome para polygon. Acrescente outro
parâmetro chamado n e altere o corpo para que desenhe um polígono regular
de n lados Dica: os ângulos exteriores de um polígono regular de n
lados são 360/n graus.
4. Escreva uma função chamada circle que use o turtle, t e um raio r como
parâmetros e desenhe um círculo aproximado ao chamar polygon com um
comprimento e número de lados adequados. Teste a sua função com uma
série de valores de r.
Dica: descubra a circunferência do círculo e certifique-se de que length * n =
circumference.
5. Faça uma versão mais geral do circle chamada arc, que receba um parâmetro
adicional de angle, para determinar qual fração do círculo deve ser desenhada.
angle está em unidades de graus, então quando angle=360, o arc deve desenhar
um círculo completo.'''

import turtle
import math


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, length, n):
    angle = 360 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    arc(t, r, 360)


if __name__ == '__main__':
    bob = turtle.Turtle()

    length = 100
    n = 5
    radius = 100
    bob.pu()  # tira a caneta
    bob.fd(radius)  # anda isso
    bob.lt(90)  # aponta pra cima
    bob.pd()  # coloca caneta

    circle(bob, radius)

    turtle.mainloop()
