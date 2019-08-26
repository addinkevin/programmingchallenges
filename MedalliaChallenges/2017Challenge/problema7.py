import unittest
import math

MODULO = 10 ** 9 + 7


def checkIfSumIsPossible(n, unluckyNumber):
    index = (-1 + math.sqrt(1 + 8 * unluckyNumber)) / 2
    index = round(index)

    # n * (n+1)/ 2 = unlucky number
    if index * (index + 1) == 2 * unluckyNumber:
        return True

    return False


def maxMoney(taxpayers, unluckyNumber):
    n = taxpayers
    maxSum = ((n * (n + 1)) // 2) % MODULO
    if checkIfSumIsPossible(n, unluckyNumber):
        return (maxSum - 1) % MODULO
    return maxSum


class MyTestCase(unittest.TestCase):
    def test0(self):
        self.assertEqual(3, maxMoney(2, 2))
        self.assertEqual(2, maxMoney(2, 1))
        self.assertEqual(5, maxMoney(3, 3))


if __name__ == '__main__':
    unittest.main()
