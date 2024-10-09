def div_list(n):
    divlist = []
    for i in range(1, n):
        if n % (n-i) == 0:
            divlist.append(n-i)
    div_sum = sum(divlist)
    return(div_sum)


def func(n):
    amicable = []
    for i in range(n):
        if div_list((div_list(i))) == i:
            if div_list(i) != div_list(div_list(i)):
                amicable.append(i)
    return (amicable, sum(amicable))
        
print(func(10000))
