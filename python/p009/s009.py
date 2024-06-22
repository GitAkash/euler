'''
Calculations
a < b < c in natural
a + b + c = 1000
c^2 = a^2 + b^2
c = 1000 - (a + b)
c = (a**2 + b**2)**0.05

Assumed I can check for this. Doesn't work due to float thingies?
1000 - (a + b) = (a**2 + b**2)**0.05

So rewrote it so i can use this, and check by hand..
a = (-1000000 + 2000b)/(-2000+2b)
'''

for b in range(1000):
    a = (-1000000 + 2000*b)/(-2000+2*b)
    if abs(a) < abs(b) and a > 0:
        print(a, b)
        # Returns Short list, check myself for integers.
        # Seems to be 200 and 375

        # c must be 1000 - 375 - 200
c = 1000 - 375 - 200
print(c * 375 * 200)
