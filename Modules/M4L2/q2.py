'''
Module containing code to find egyptian fraction
'''
from fractions import Fraction
from typing import List

def egyptian_fraction(num:Fraction)->List[int]:
    '''
    Returns an array of unit fractions that sum upto given fraction
    '''
    denom_array = list()
    
    while num.numerator != 1:
        i = 2
        while Fraction(1, i)>num:
            i += 1
        denom_array.append(i)
        num -= Fraction(1, i)
    
    denom_array.append(num.denominator)
    return denom_array
    
if  __name__=="__main__":
    num, den = map(int, input().split())
    result = egyptian_fraction(Fraction(num, den))
    print(*result)
                                                                                                                            