def fibonacci():
    a = 0
    b = 1
    i = 1
    
    while True:
        c = a + b        
        
        if len(str(c)) == 1000:
            return print(c, i)
        
        b = a
        a = c
        i += 1
        

fibonacci()
