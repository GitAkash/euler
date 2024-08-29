def fact(n):
    c = 1
    while n > 1:
        c *= n
        n -= 1
    return c

def routes(n):
    return fact(2 * n) / (fact(n)*fact(n))

print(routes(20))

