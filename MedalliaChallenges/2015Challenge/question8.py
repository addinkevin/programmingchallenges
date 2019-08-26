import unittest


def getPairs(array):
    pairs = []
    minDiff = float('inf')
    for i in range(1, len(array)):
        diff = abs(array[i] - array[i - 1])
        if minDiff > diff:
            minDiff = diff
            pairs = [(array[i - 1], array[i])]
        elif minDiff == diff:
            pairs.append((array[i - 1], array[i]))

    return pairs


def closestNumbers(array):
    array.sort()
    pairsWithMinDiff = getPairs(array)
    return pairsWithMinDiff


class Question8Test(unittest.TestCase):
    def testCase0(self):
        array = [4, 2, 1, 3]
        expectedOutput = [(1, 2), (2, 3), (3, 4)]
        self.assertListEqual(expectedOutput, closestNumbers(array))


if __name__ == '__main__':
    unittest.main()
