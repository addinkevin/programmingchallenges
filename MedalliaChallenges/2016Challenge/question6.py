import unittest


def ironMan(energies):
    minSum = float('inf')
    currentSum = 0
    for e in energies:
        currentSum += e
        if currentSum < minSum:
            minSum = currentSum

    if minSum >= 0:
        return 1
    return -minSum + 1


class MyTestCase(unittest.TestCase):
    def testCase0(self):
        energies = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]
        output = 8
        self.assertEqual(output, ironMan(energies))

    def testCase1(self):
        energies = [-5, 4, -2, 3, 1, -1, -6, -1, 0, -5]
        output = 13
        self.assertEqual(output, ironMan(energies))


if __name__ == '__main__':
    unittest.main()
