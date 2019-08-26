import unittest

"""
Given a list of integers L and a value K, return the number of pairs
whose elements sum to less than K.
"""


def countPairsBruteForce(array, k):
    count = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] < k:
                count += 1

    return count


def countPairs(array, k):
    array.sort()
    i = 0
    j = len(array) - 1
    count = 0
    while i < j:
        if array[i] + array[j] < k:
            count += (j - i)
            i += 1
        else:
            j -= 1

    return count


class MyTestCase(unittest.TestCase):
    def test0(self):
        array = [3, 7, 2, 8]
        k = 10
        self.assertEqual(2, countPairs(array, k))

    def test1(self):
        array = [9, 47, 46, 24, 31, 25, 18, 21, 49, 10]
        k = 56
        self.assertEqual(countPairsBruteForce(array, k), countPairs(array, k))


if __name__ == '__main__':
    unittest.main()
