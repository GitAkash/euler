'''
Open primefnder from P7.
'''
def prime(q):
    n = 2
    primes = [2] 
    while (primes[-1] < q):
        if any(n % i == 0 for i in primes):
            n += 1
        else:
            if n > q:
                break
            else:
                primes.append(n)
                n += 1

    print(primes, sum(primes))

prime(2e6)

'''
Okay this was reaaaallly slow :-(
'''
