def divide(n):
    nominator = 1
    remainder = 0
    listi = []
    i = 0
    while i < 400:
        i += 1
        if n > nominator:
            nominator *= 10
            # print(nominator)
        else:
            how_many_fits = nominator % n
            left_over = nominator - how_many_fits
            nominator -= left_over
            decimal = left_over // n
            # print(nominator*10, left_over, how_many_fits, decimal)
            listi.append(decimal)
    return listi
