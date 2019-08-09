"""
Sherlock and Cost

https://www.hackerrank.com/challenges/sherlock-and-cost/problem
"""
import unittest

MAX_B_VALUE = 100


def sherlockAndCostAlternative(array):
    if len(array) == 1:
        return array[0]

    opt = [[0 for _ in range(MAX_B_VALUE + 1)] for _ in range(len(array))]

    for i in range(1, len(array)):
        for aValueI in range(1, array[i] + 1):
            maxDiff = -1
            for aValuePrev in range(1, array[i - 1] + 1):
                diff = opt[i - 1][aValuePrev] + abs(aValueI - aValuePrev)
                if diff > maxDiff:
                    maxDiff = diff
            opt[i][aValueI] = maxDiff

    return max(opt[-1])


def getDiff(solution):
    diff = 0
    for i in range(1, len(solution)):
        diff += abs(solution[i] - solution[i - 1])

    return diff


def sherlockAndCost(array):
    if len(array) == 1:
        return array[0]

    solution1 = [1 if i % 2 == 0 else array[i] for i in range(len(array))]
    solution2 = [1 if i % 2 == 1 else array[i] for i in range(len(array))]

    diffSolution1 = getDiff(solution1)
    diffSolution2 = getDiff(solution2)
    return max(diffSolution1, diffSolution2)


class SherlockAndCostTest(unittest.TestCase):
    def test0(self):
        inputArray = [10, 1, 10, 1, 10]
        outputExpected = 36
        self.assertEqual(outputExpected, sherlockAndCost(inputArray))


if __name__ == '__main__':
    unittest.main()
