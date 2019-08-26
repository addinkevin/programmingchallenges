import unittest


def arrayGame(array):
    minValue = float('inf')
    sumValue = 0
    for element in array:
        if element < minValue:
            minValue = element
        sumValue += element

    return sumValue - len(array) * minValue


class MyTestCase(unittest.TestCase):
    def testCase0(self):
        array = [1, 2, 3]
        output = 3
        self.assertEqual(output, arrayGame(array))

    def testCase1(self):
        array = [2, 2, 2]
        output = 0
        self.assertEqual(output, arrayGame(array))

    def testCase3(self):
        array = [1, 2, 3, 4]
        output = 6
        self.assertEqual(output, arrayGame(array))


if __name__ == '__main__':
    unittest.main()
