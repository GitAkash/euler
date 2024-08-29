"""
One - 3
Two - 3
Three - 5
Four - 4
Five - 4
Six - 3
Seven - 5
Eight - 5
Nine - 4
Ten - 3
Eleven - 6
Twelve - 6
Thirteen - 8
Fourteen - 8
Fifteen - 7
Sixteen - 7
Seventeen - 9
Nineteen - 8
Twenty - 6
Thirty - 6
Forty - 5
Fifty - 5
Sixty - 5
Seventy - 7
Eighty - 6
Ninety - 6
Hundred - 7
Thousand - 8
"""

firstnineteen = 3+3+5+4+4+3+5+5+4+3+6+6+8+8+7+7+9+8
one_to_nine = 3+3+5+4+4+3+5+5+4

twenties = 6*10 + one_to_nine
thirties = 6*10 + one_to_nine
forties = 5*10 + one_to_nine
fifties = 5*10 + one_to_nine
sixties = 5*10 + one_to_nine
seventies = 7*10 + one_to_nine
eighties = 6*10 + one_to_nine
nineties = 6*10 + one_to_nine


firstninetynine = firstnineteen+twenties+thirties+forties+fifties+sixties+seventies+eighties+nineties


hundredamounts = one_to_nine * 100 #One (Hundred).. Two (Hundred)
hundreds = (3 + 7) * (900-9) + 7 * 9 #Hundred and.. Dont include exact hundred (They dont need "and")

totalhunderds = hundredamounts+hundreds+firstninetynine*9

total = 11 + totalhunderds + firstninetynine

"""
One Hundred Bla bla bla = Two Hundred Bla Bla Bla 
"""

print(firstninetynine, totalhunderds, firstnineteen, one_to_nine)
print(total)
