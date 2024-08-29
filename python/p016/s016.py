def solve(n):
    c = 0
    numb = str(2**n)
    for i in numb:
        c += int(i)
    return c

print(solve(1000))
