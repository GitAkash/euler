def multiples(n):
    l = []
    while n != 1:
        if n % 3 == 0 or n % 5 == 0:
            l.append(n)
            n -= 1
            print(l)
        else:
            n -= 1
    return print(sum(l))

multiples(999)
