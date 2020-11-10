'''
File Name : Gemstones.py
Author : Mukaddes Altuntas

Created On : 10/10/2020

Version : Pyhton 3.7.5

Copyright (c) 2020 Mukaddes Altuntas. All rights reserved.

Description : This program finds the number of the substring '010' in given string.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.

# Pythonic way of the function 
def beautifulBinaryString2(b):
    return b.count('010')

# Primitive way of the function
def beautifulBinaryString(b):
    i = 0
    count = 0

    while i in range(len(b)-2):
    	# Keep going through until you see '0' 
        if b[i] != '0':
            i+=1
        # When you see '0', check '10' exists or not.
        else:
            if (b[i+1] == '1' and b[i+2] == '0'):
                count += 1
                i+=3
            else:
                i+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
