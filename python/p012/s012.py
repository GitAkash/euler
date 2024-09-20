'''
Way too suboptimal.. 
Should read the question before computing it the other way around!?
Needs a super fast extreme fast computer, this algorithm is like n^3489274
'''


def triangle(n):
    c = 0
    sumlist = []
    if c > n:
        tempsum = []
        for i in range(c+1):
            tempsum.append(i)
        sumlist.append(sum(tempsum))
        c+=1
    return sumlist

def factorize(n):
    factors = []
    for i in range(1,int((n+1)**0.5)):
        if n % i == 0:
            factors.append(i)
            if n / i != i:
                factors.append(n/i)
    return factors 

def factortriangle(n, divisors):
    finalfactors = []
    values = triangle(n)
    #print(values)
    for i in values:
        factorizednumb = factorize(i)
        finalfactors.append((i, factorizednumb, len(factorizednumb))) 
        if len(factorizednumb) > divisors:
            print(i, len(factorizednumb))
    return (finalfactors)

print(factortriangle(1000000000, 5))

