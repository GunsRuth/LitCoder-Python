def check(digit, k):
    for times in range(1, 11):
        temp = (k*times) % 10
        if temp==digit:
            return times
    return -1

def getCount(num, k):
    digit = num % 10
    times = check(digit, k)

    if times==-1:
        return -1
    if num >= (times * k):
        return times
        
    return -1

num = int(input())
k = int(input())
result = getCount(num, k)
print(result)
                                                                                                                            