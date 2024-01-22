#!/bin/python3

from collections import Counter


#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


def make_anagram(string_one: str, string_two: str):
    a_mappings = Counter(string_one)
    b_mappings = Counter(string_two)
    final_set = set(string_one + string_two)
    count = 0
    for i in final_set:
        count += abs(a_mappings.get(i, 0) - b_mappings.get(i, 0))
    return count


if __name__ == '__main__':
    fptr = open("test.txt", 'w')
    a = input()
    b = input()
    res = make_anagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
