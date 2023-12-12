def findLongestSS(string):
    lastIndex = dict()
    maxLen = 0
    startIndex = 0
    for index, char in enumerate(string):
        if char in lastIndex:
            startIndex = max(startIndex, lastIndex[char]+1)
        maxLen = max(maxLen, index-startIndex+1)
        lastIndex[char] = index
    return maxLen
    
string = input()
result = findLongestSS(string)
print(result)
                                                                                                                            