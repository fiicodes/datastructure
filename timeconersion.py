#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hh,mm,ss_ampm=s.split(":")
    ss=ss_ampm[:2]
    ampm=ss_ampm[2:]
    if ampm=='PM' and hh!='12':
        hh=str(int(hh)+12)
    elif ampm=='AM' and hh=='12':
        hh='00'
    military_time=f"{hh}:{mm}:{ss}"
    return military_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
