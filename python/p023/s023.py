def divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def abundant_number(n):
    sum_div = sum(divisors(n))
    if sum_div > n:
        return n        

def func():
    abundant_numbers = set()
    sums = set()
    total = 0
    for n in range(1, 28123):
        if abundant_number(n):
            abundant_numbers.add(n)
    print(abundant_numbers)    
    for i in range(1, 28123):
        for j in range(i, 28123):
            summ = i + j
            if summ not in abundant_numbers:
                if summ <= 28123:
                    if summ not in sums:
                        total += summ
                    sums.add(summ)
    return total
297575970

# # print(abundant_number(28))
# def func():
#     abundant_numbers = set()
#     sums = set()
#     total = 0
#     for n in range(1, 28124):
#         if abundant_number(n):
#             abundant_numbers.add(n)
#     print(abundant_numbers)    

    # for i in abundant_numbers:
    #     for j in abundant_numbers:
    #         summ = i + j
    #         if summ not in sums:
    #             total += summ
    #         sums.add(summ)
        
    # return total

print(func())
