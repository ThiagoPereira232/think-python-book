def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


countdown(3)


def do_n(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print('Hello!')
        do_n(n-1)


do_n(2)
