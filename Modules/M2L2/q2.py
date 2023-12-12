def countWays(n, m):
    MOD = 10**9+7
    rowComb = [1, 1, 2, 4]
    
    while len(rowComb) <= m:
        rowComb.append(sum(rowComb[-4:]) % MOD)
    
    total = [pow(c, n, MOD) for c in rowComb]
    
    unstable = [0, 0]
    for width in range(2, m+1):
        f = lambda j: (total[j] - unstable[j]) * total[width-j]
        result = sum(map(f, range(1, width)))
        unstable.append(result % MOD)
        
    return (total[m] - unstable[m]) % MOD
    
n = int(input())
m = int(input())
ways = countWays(n, m)
print(ways)
                                                                                                                            