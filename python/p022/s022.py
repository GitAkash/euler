file = open("names.txt")
names = file.read().replace("\"","").lower().split(",")
names.sort()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def score():
    totval = []
    score = 0
    for name in names:
        for letter in name:
            letterval = alphabet.index(letter)+1
            totval.append(letterval)
        score += sum(totval)*(names.index(name)+1)
        totval = []
    return score

print(score())
