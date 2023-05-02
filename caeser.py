#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    encrypted_string=""
    for c in s:
        if c.isalpha():
            ascii_offset=65 if c.isupper() else 97
            shift=chr((ord(c)+k-ascii_offset)%26 +ascii_offset)
            encrypted_string+=shift
        else:
            encrypted_string+=c
    return encrypted_string



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
