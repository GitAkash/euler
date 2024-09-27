def isInteger(n):
    string_value = str(n)
    i = string_value.find('.')
    decimal = string_value[i+1::]
    if int(decimal) == 0:
        return n
    else:
        False

def diophatene(d, y):
    return (1+d*y**2)**0.5

def main():
    max = 0
    for d in range(614, 1, -1):
        y = 1
        while True:
            x = diophatene(d, y)
            if isInteger(x):
                if x > max:
                    max = x
                    print(f"For D = {d}: A minimal x is obtained, x = {x}", y)
                    break
                else:
                    print(f"For D = {d}: No increase in x, x = {x}")
                    break
            else:
                y += 1
    return max

main()
# print(diophatene(797,43101167))
