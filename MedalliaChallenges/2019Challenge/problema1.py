import unittest
import math
import os
import random
import re
import sys


# Complete the 'kinderSquare' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def isLastDigit(number, digit):
    return number % 10 == digit


def kinderSquare(arr):
    # Write your code here
    solution = []
    tmpArray = (x ** 2 + 10 for x in arr)
    for x in tmpArray:
        if not (isLastDigit(x, 5) or isLastDigit(x, 6)):
            solution.append(x)

    return solution


class MyTestCase(unittest.TestCase):
    def test0(self):
        arr = [1, 5, 9, 6]
        expectedOutput = [11, 91]
        self.assertListEqual(expectedOutput, kinderSquare(arr))


if __name__ == '__main__':
    unittest.main()
