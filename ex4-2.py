# Escreva um conjunto de funções adequadamente geral que possa desenhar flores

import turtle
from ex4 import arc


def petola(t, r, angle):
    ''' Desenha uma petola
    t: turtle
    r: radius
    angle: angulo''' 
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flor(t, n, r, angle):
    '''Desenha flor com N lados
    t: Turtle
    n: numero de petolas
    r: raio do arc
    angle: angulo'''
    for i in range(n):
        petola(t, r, angle)
        t.lt(360.0 / n)


def move(t, length):
    '''move turtle para frente sem deixar rastoros
    abaixa caneta'''
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

move(bob, -100)
flor(bob, 7, 60, 60)

move(bob, 100)
flor(bob, 10, 40, 80)

move(bob, 100)
flor(bob, 20, 140, 20)

bob.hideturtle()
turtle.mainloop()
