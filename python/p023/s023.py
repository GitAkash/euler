def divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            i += 1
        else:
            i += 1
    return divisors

def abundant_number(n):
    sum_div = sum(divisors(n))
    if sum_div > n:
        return n        

def func():
    abundant_numbers = []
    for n in range(1, 28124//2):
        if abundant_number(n):
            abundant_numbers.append(n)

    for i in abundant_numbers:
        for j in abundant_numbers:

print(func())
        
