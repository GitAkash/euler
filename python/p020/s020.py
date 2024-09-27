def factorial(n):
    c = 1
    for i in range(1, n+1):
        c *= i
    return c

factorial(10)
def func(n):
    c = 0
    fac = factorial(n)
    splitted_fac = str(fac)
    for i in splitted_fac:
        c += int(i)
    return c

print(func(100))
