pyramid = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
max = 0
rows = pyramid.splitlines()
intpyramid = []
converted_row = []
for row in rows:
    numbs = row.split(' ')
    for numb in numbs:
        converted_row.append(int(numb)) 
    intpyramid.append(converted_row)
    converted_row = []

max = 0
# print(intpyramid)
# WAAROM DE TERING BEGINT IE NIET BOVEN AAN????????????????????////
for row in range(len(intpyramid)):
    for column in range(len(intpyramid[row])):
        current_number = intpyramid[row][column]
        for l in [0,1]:
            for k in [0, 1]:
                for z in [0, 1]:
                    num2 = 0
                    num3 = 0
                    num4 = 0
                    if row <= 11:
                        if column < len(intpyramid[row])-1:
                            num2 = (intpyramid[row+1][column+l])
                            num3 = (intpyramid[row+2][column+l+k])
                            num4 = (intpyramid[row+3][column+l+k+z])
                            sequence = [current_number, num2, num3, num4]
                            print(sequence)
                            if sum(sequence) > max:
                                max = sum(sequence)
                                print("MAX FOUND",sequence, max)
print(max)
        # print(sequence0, sequence1, sequence2, sequence3, sequence4, sequence5, sequence6, sequence7)
        #Values that are connected to the value above.
        # if row <= 13:
            # next_number0 = intpyramid[row+1][column]
            # next_number1 = intpyramid[row+1][column+1]
        # if row <= 11:
            # next_list_l = [intpyramid[row+i][column] for i in range(4)]
            # if column < len(intpyramid[row])-1:
                # next_list_r = [intpyramid[row+i][column+1]for i in range(4)]
                # print(next_list_l, next_list_r)

        #Check if value is the last row.
        # else:
            # next_number0 = 0
            # next_number1 = 0
        # print(next_number0)    
