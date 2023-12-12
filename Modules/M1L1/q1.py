def count(inString):
    countArr = [0, 0, 0, 0]
    for char in inString:
        if char.isupper():
            countArr[0] += 1
        elif char.islower():
            countArr[1] += 1
        elif char.isdigit():
            countArr[2] += 1
        else:
            countArr[3] += 1
    return countArr

inputString = input()    
countArr = count(inputString)
tlen = len(inputString)

for count in countArr:
    print(f"{count/tlen*100:0.3f}%")
                                       