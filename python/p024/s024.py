app = [0,1,2,3,4,5,6,7,8,9]

def swap(list):
    if len(list) == 2:
        newlist = []
        newlist.append(list[0])
        newlist.append(list[1])
        yield newlist
        newlist = []
        newlist.append(list[1])
        newlist.append(list[0])
        yield newlist

    else:
        dimension = 0
        for i in range(len(list)):
            list_copy = list[:]
            removed_numb = list_copy.pop(i)
            for j in swap(list_copy):
                dimension += 1
                j.insert(0, removed_numb)
                # print(dimension, j)
                yield j

# for x in swap(app):
    # print(x)
c = 0
for x in swap(app):
    c +=1
    if c == 1000000:
        print(x)
