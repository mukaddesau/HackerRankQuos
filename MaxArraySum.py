'''
File Name : MaxArraySum.py
Author : Mukaddes Altuntas

Created On : 19/11/2020

Version : Pyhton 3.7.5

Copyright (c) 2020 Mukaddes Altuntas. All rights reserved.

Description : This program finds the max sum value of the group of non-adjacent elements in an array.
              In this program, the code theme of HackerRank for Python is used without changing. 
'''

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    
    '''for each element there are two options:
        1. Add the current element to the sum.
        2. Do not add the current element. Choose the max of the previous sums. Previous sums
        are 'included previous element sum' and 'excluded previous elemen sum'.    '''
        
    excluded_sum = 0 # keeps the sum excluding previous element.
    included_sum = arr[0] # keeps the sum including previous element. 
    
    for i in range(1, len(arr)):
        
        # 1. If we add the current element to the sum, we have to add it 
        #  to 'exluded previous element sum'. It is just because,
        #  we can not add adjacent elements to the sum at the same time.
        new_included_sum = excluded_sum + arr[i]
        
        # 2. If we do not add the current element to the sum,
        #  we choose the max one of the previous sums: 
        # 'excluded previous element sum' or 'included previous element sum'.
        new_excluded_sum = max(excluded_sum, included_sum)
        
        # For the next step, the current sums will be previous sums.
        included_sum = new_included_sum
        excluded_sum = new_excluded_sum
    
        # return max of the sum for the last element included or excluded 
    return (max(included_sum,excluded_sum))
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
