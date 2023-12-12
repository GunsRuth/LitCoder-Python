def hasPrefix(words):
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if len(words[i]) > len(words[j]) and words[i].startswith(words[j]):
                return True
            if len(words[i]) < len(words[j]) and words[j].startswith(words[i]):
                return True
    return False
    
words = input().split()
result = hasPrefix(words)
print("GOOD PASSWORD" if not result else "BAD PASSWORD")
                                                                                                                            