import turtle
bob = turtle.Turtle()
print(bob)

# fd = avance
# bk = mova-se para tras
# lt = virar à esquerda
# rt = virar à direita
# lt e rt são angulos em gruas, bk e fd em pixes

# pu -> caneta para cima
# pd -> caneta para baixo

'''
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
'''

# for i in range(4):
#     print('Hello!')

for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()
