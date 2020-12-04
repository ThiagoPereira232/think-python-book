# Desenhe tortas

import turtle
import math


def desenhar_torta(t, n, r):
    '''Desenha uma torta e depois se move para a direita.
    t: tartaruga
    n: número de segmentos
    r: comprimento dos raios'''
    polypie(t, n, r)
    t.pu()
    t.fd(r * 2 + 10)
    t.pd()


def polypie(t, n, r):
    '''Desenha uma torta dividida em segmentos radiais.
    t: tartaruga
    n: número de segmentos
    r: comprimento dos raios'''
    angle = 360 / n
    for i in range(n):
        isosceles(t, r, angle / 2)
        t.lt(angle)


def isosceles(t, r, angle):
    '''Desenha tirangulos isosceles'''

    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)


bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()

size = 40

desenhar_torta(bob, 5, size)
desenhar_torta(bob, 6, size)
desenhar_torta(bob, 7, size)
desenhar_torta(bob, 8, size)

bob.hideturtle()
turtle.mainloop()

