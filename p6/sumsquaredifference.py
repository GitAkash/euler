def squaredif(n):
    l = []
    g = []
    for i in range(0, n):
       l.append(i**2)
       g.append(i)
    print(sum(g)**2 - sum(l))

squaredif(101)
