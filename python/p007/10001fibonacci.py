def prime(q):
    n = 2
    primes = [] 
    while len(primes) < q:
        if any(n % i == 0 for i in primes):
            n += 1
        else:
            primes.append(n)
            n += 1
    primes.insert(0, 1)
    print(primes[q])
