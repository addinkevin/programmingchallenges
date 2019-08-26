import unittest

"""
You are given a list of n numbers, and you must return the most
repeated one. If there is more than one, then return the smallest
one.
"""
from collections import defaultdict


def updateMinElement(countDic, element, mostRepElem):
    if mostRepElem is None:
        return element

    countElement = countDic[element]
    countMostRepElem = countDic[mostRepElem]

    if countElement > countMostRepElem:
        return element
    elif countElement == countMostRepElem:
        if element < mostRepElem:
            return element
        return mostRepElem
    else:
        return mostRepElem


def getMostRepeatedElement(array):
    countDic = defaultdict(int)
    mostRepElem = None

    for element in array:
        countDic[element] += 1
        mostRepElem = updateMinElement(countDic, element, mostRepElem)

    return mostRepElem


class MyTestCase(unittest.TestCase):
    def check(self, array, expectedOutput):
        self.assertEqual(expectedOutput, getMostRepeatedElement(array))

    def test0(self):
        array = [1, 2, 3, 3]
        expectedOutput = 3
        self.check(array, expectedOutput)

    def test1(self):
        array = [1, 2, 3, 1, 2, 3, 4, 2, 3]
        expectedOutput = 2
        self.check(array, expectedOutput)

    def test2(self):
        array = [0, 0, 1, 1, 2]
        expectedOutput = 0
        self.check(array, expectedOutput)


if __name__ == '__main__':
    unittest.main()
