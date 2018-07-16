def square(x, y=2):
    '''
    Squares a number and returns the result:
    >>> square(2)
    4
    >>> square(4)
    8
    '''
    return x*y

if __name__ == '__main__':
    import doctest, this
    doctest.testmod(this)