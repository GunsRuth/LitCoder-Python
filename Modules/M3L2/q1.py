def getNSmallest(numbers, bracketSize, nIndex):
    NSmallest = list()
    for starti in range(len(numbers)-bracketSize+1):
        temp = numbers[starti:starti+bracketSize]
        temp.sort()
        NSmallest.append(temp[nIndex-1])
    return NSmallest

numbers = list(map(int, input().split()))
bracketSize = int(input())
nIndex = int(input())
NSmallest = getNSmallest(numbers, bracketSize, nIndex)
print(*NSmallest)
                                                                                                                            