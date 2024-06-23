def multL(n):
    c = 1
    for i in n:
        c *= i
    return c

def trialDiv(n):
    p = []
    f = 2
    while f**2 <= n:
        if n % f == 0:
            p.append(f)
            n //= f
        else:
            f += 1
    if n != 1:
        p.append(n)
    return p

