max = 0
for i in range(100, 1001):
    for j in range(100, 1001):
        if str(i*j) == str(i*j)[::-1]:
            if i*j > max:
                max = i * j

print(max)
