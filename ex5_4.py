def recurse(n, s):
    '''Se n for 0 print s
    senão soma ns com 2 e n diminui 1 e fica assim ate n ser == 0
    n >= 0'''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(3, 0)
