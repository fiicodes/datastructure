#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    A.sort()
    operation=0
    while (A[0])<=k:
        if len(A)<2:
            return -1
        first_least=A.pop(0)
        second_least=A.pop(0)
        sweetness=first_least+(2*second_least)
        A.append(sweetness)
        operation+=1
        A.sort()
    if any(i<=k for i in A):
        return -1
    return operation


    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
