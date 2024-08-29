def collatzcount(n):
    c = 1
    while True:
        if n % 2 == 0:
             n /= 2
             c += 1
        else:
             n = n*3 + 1
             c += 1
        if n == 1:
            return(c)
max = 0
for i in range(1,1000000):
    if collatzcount(i) > max:
        max = collatzcount(i)
        print(i, max)
