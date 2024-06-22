def primetree(n):
    c = 2
    while n != 1:
        if n % c == 0:
            n /= c
            print(f"{n}, {c}")
        else:
            c += 1

primetree(600851475143)
