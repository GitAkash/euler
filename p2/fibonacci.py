def fib():
    total = 0
    a = 0
    b = 1
    c = 0
    while c < 4e6:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            total += c
    return total
