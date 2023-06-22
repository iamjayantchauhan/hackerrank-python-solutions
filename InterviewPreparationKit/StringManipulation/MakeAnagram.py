#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def makeAnagram(a, b):
    # Write your code here
    return 0


if __name__ == '__main__':
    fptr = open("test.txt", 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
