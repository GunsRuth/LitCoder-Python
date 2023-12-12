from heapq import heapify, heappop, heappush

def minSteps(sweets, minS):
    temp = sweets.copy()
    heapify(temp)
    step = 0
    while temp[0] < minS:
        step += 1
        sweet1 = heappop(temp)
        sweet2 = heappop(temp)
        heappush(temp, sweet1 + 2 * sweet2)
    return step

minS = int(input())
sweets = list(map(int, input().split()))
stepsCount = minSteps(sweets, minS)
print(stepsCount)
                                                                                                                            