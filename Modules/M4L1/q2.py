def findMax(queries, arraySize):
    temp = [0]*arraySize
    for query in queries:
        start, end, value = map(int, query.split())
        for index in range(start-1, end):
            temp[index] += value
    return max(temp)

arraySize = int(input())
queryCount = int(input())
queries = list()
for _ in range(queryCount):
    queries.append(input())
result = findMax(queries, arraySize)
print(result)
                                                                                                                            