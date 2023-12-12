def clumsyFactorial(num):
    stack = []
    index = 0
    stack.append(num)
    num -= 1
    while num:
        if index==0:
            stack[-1] *= num
        elif index==1:
            stack[-1] = int(stack[-1]/num)
        elif index==2:
            stack.append(num)
        else:
            stack.append(-1*num)
        index = (index+1)%4
        num -= 1
    return sum(stack)
    
num = int(input())
result = clumsyFactorial(num)
print(result)
                                                                                                                            