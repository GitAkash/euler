def triangular(n):
    sumlist = [1]
    triangularnumb = 1
    while True:
        sumlist.append(sumlist[-1]+1)
        if len(factorize(triangularnumb)) >= n:
            print(triangularnumb)
            break
        triangularnumb = sum(sumlist)
        
def factorize(n):
    factors = []
    for i in range(1,int((n+1)**0.5)):
        if n % i == 0:
            factors.append(i)
            if n / i != i:
                factors.append(int(n/i))
    return factors 

triangular(500)
