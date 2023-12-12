def maxSS(text, pattern):
    leftTotal = rightTotal = normal = 0
    for char in text:
        if char == pattern[1]:
            leftTotal += 1
            normal += rightTotal
        if char == pattern[0]:
            rightTotal += 1
    return normal+max(leftTotal, rightTotal)
    
text = input()
pattern = input()
count = maxSS(text, pattern)
print(count)
                                                                                                                            