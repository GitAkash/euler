'''
Way too suboptimal.. 
Should read the question before computing it the other way around!?
Needs a super fast extreme fast computer, this algorithm is like n^3489274
'''


def triangle(n):
    c = 0
    sumlist = []
    while c < n:
        tempsum = []
        for i in range(c+1):
            tempsum.append(i)
        sumlist.append(sum(tempsum))
        c+=1
    return sumlist

def factorize(n):
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors 

def factortriangle(n):
    finalfactors = []
    values = triangle(n)
    for i in values:
        finalfactors.append((i, factorize(i), len(factorize(i)))) 
        if len(factorize(i)) > 500:
               print(i, len(factorize(i)))
    return (finalfactors)

factortriangle(3000)

