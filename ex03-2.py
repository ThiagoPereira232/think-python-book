# 1. Digite este exemplo em um script e teste-o

'''
def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')
    do_twice(print_spam)


do_twice(print_spam)
'''

'''
2. Altere do_twice para que receba dois argumentos,
um objeto de função e um valor, e
chame a função duas vezes, passando o valor como um argumento.
'''


def do_twice(f, arg):
    f(arg)
    f(arg)


'''
def print_spam():
    print('spam')


do_twice(print, 'spam')
'''

'''
3. Copie a definição de print_twice que aparece anteriormente neste capítulo no seu
script.

4. Use a versão alterada de do_twice para chamar print_twice duas vezes,
passando 'spam' como um argumento.

'''


def print_twice(arg):
    print(arg)
    print(arg)


# do_twice(print_twice, 'spam')


''' 5. Defina uma função nova chamada do_four que receba um objeto de função e um
valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve
haver só duas afirmações no corpo desta função, não quatro.'''


def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)


do_twice(print, 'spam')
print('')

do_four(print, 'spam')
