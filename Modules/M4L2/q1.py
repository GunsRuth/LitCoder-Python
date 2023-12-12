'''
To query index Kth Smallest Trimmed Numbers
'''
from typing import List

def indexofkthsmallest(nums:List[str], k:int, trim:int)->int:
    '''
    finds index of Kth smallest from trimmed numbers
    '''
    temp = list()
    
    for i, num in enumerate(nums):
        temp.append((int(num[-trim:]), i))
        
    temp.sort()
    return temp[k-1][1]
    
if __name__=="__main__":
    nums = input().split()
    count = int(input())
    
    for _ in range(count):
        k, trim = map(int, input().split())
        result = indexofkthsmallest(nums, k, trim)
        print(result, end=" ")
                                                                                                                            