def fact(n):
    '''
    Calculate 1*2*...*n

    print(fact(1))
    1
    print(fact(10))
    ?
    print(fact(-1))
    ?
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
