def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y
def fibonacci_multiplos(n):
    fibs = []
    a, b = 0, 1
    while a < n:
        if (a%5)==0:
            fibs.append(a)
        a, b = b, a+b
    return fibs
