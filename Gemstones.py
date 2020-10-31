#!/bin/python3

import math
import os
import random
import re
import sys

# Counter module helps us to count occurances of letters.
from collections import Counter 

# Complete the gemstones function below.
def gemstones(arr):
    letterDict = {} # a complete dictionary to keep all letters and total occurances.
                    #  ({'a':0, 'b':0 ....})
    for word in arr:
        # Add a letter dictionary of that word to the complete letter dictionary.
        # The counter helps us to sum of the occurance of a letter when we merge two 
        # dictionaries into one.
        # word1 = {'a': 1, 'b': 1}
        # word2 = {'b': 1, 'c': 1}
        # letterDict = {a': 1, 'b': 2, 'c': 1}
        letterDict = Counter(letterDict) + Counter(dict.fromkeys(word,1))
    # return number of letters which exists in all words.    
    return Counter(letterDict.values())[len(arr)] 
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
