def findSubArr(binaryNum):
    prevSum = dict()
    currSum = 0
    maxLen = 0
    for index, digit in enumerate(binaryNum):
        if digit==0:
            currSum -= 1
        else:
            currSum += 1
        
        if currSum == 0:
            maxLen = index + 1
            continue
        
        if currSum in prevSum:
            if maxLen < (index-prevSum[currSum]):
                maxLen = index-prevSum[currSum]
        else:
            prevSum[currSum] = index
            
    return maxLen

binaryNum = list(map(int, input().split()))
largestSubArr = findSubArr(binaryNum)
print(largestSubArr)
                                                                                                                            