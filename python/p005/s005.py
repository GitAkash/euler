n = 1

while True:
    if n % 19 == 0 and n % 17 == 0 and n % 13 == 0 and n % 11 == 0 and n % 7 == 0 and n % 5 == 0 and n % 3 == 0 and n % 15 == 0 and n % 9 == 0 and n % 2 == 0:
        print(n)
        break
        
    else: 
        n += 1
