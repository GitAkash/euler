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


# print(intpyramid)
for row in range(len(intpyramid)):
    for column in range(len(intpyramid[row])):
        sequence0 = []
        sequence1 = []
        sequence2 = []
        sequence3 = []
        sequence4 = []
        sequence5 = []
        sequence6 = []
        sequence7 = []
        current_number = intpyramid[row][column]
        if row <= 11:
        #Possiblities
        
            sequence0.append(intpyramid[row+1][column])
            sequence0.append(intpyramid[row+2][column])
            sequence0.append(intpyramid[row+3][column])

            sequence1.append(intpyramid[row+1][column+1])
            sequence1.append(intpyramid[row+2][column])
            sequence1.append(intpyramid[row+3][column])

            sequence2.append(intpyramid[row+1][column+1])
            sequence2.append(intpyramid[row+2][column+1])
            sequence2.append(intpyramid[row+3][column])
        
            sequence3.append(intpyramid[row+1][column+1])
            sequence3.append(intpyramid[row+2][column])
            sequence3.append(intpyramid[row+3][column+1])
        
            sequence4.append(intpyramid[row+1][column])
            sequence4.append(intpyramid[row+2][column+1])
            sequence4.append(intpyramid[row+3][column])
        
            sequence5.append(intpyramid[row+1][column])
            sequence5.append(intpyramid[row+2][column+1])
            sequence5.append(intpyramid[row+3][column+1])
        
            sequence6.append(intpyramid[row+1][column])
            sequence6.append(intpyramid[row+2][column])
            sequence6.append(intpyramid[row+3][column+1])
        
            sequence7.append(intpyramid[row+1][column+1])
            sequence7.append(intpyramid[row+2][column+1])
            sequence7.append(intpyramid[row+3][column+1])

        if sum(sequence0) + current_number > max:
            max = sum(sequence0) + current_number

        if sum(sequence1) + current_number > max:
            max = sum(sequence1) + current_number

        if sum(sequence2) + current_number > max:
            max = sum(sequence2) + current_number

        if sum(sequence3) + current_number > max:
            max = sum(sequence3) + current_number

        if sum(sequence4) + current_number > max:
            max = sum(sequence4) + current_number

        if sum(sequence5) + current_number > max:
            max = sum(sequence5) + current_number
        
        if sum(sequence6) + current_number > max:
            max = sum(sequence6) + current_number
        
        if sum(sequence7) + current_number > max:
            max = sum(sequence7) + current_number

        print(sequence0, sequence1, sequence2, sequence3, sequence4, sequence5, sequence6, sequence7)
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
