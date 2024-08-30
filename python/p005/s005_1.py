n = 1
c = 0


while True:
    for i in range (1,21):
        if n % i == 0:
            c += 1
            if c == 20:
                print(n)
                break
        else:
            n += 1
            c = 0
