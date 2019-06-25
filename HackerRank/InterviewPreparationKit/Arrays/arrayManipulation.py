import unittest


def arrayManipulation(arraySize, queries):
    openArray = [0] * arraySize
    closeArray = [0] * arraySize

    for a, b, k in queries:
        openArray[a - 1] += k
        closeArray[b - 1] += k

    maxValue = -1
    acum = 0
    for i in range(arraySize):
        acum += openArray[i]
        if acum > maxValue:
            maxValue = acum
        acum -= closeArray[i]

    return maxValue


class ArrayManipulationTest(unittest.TestCase):
    def testCase(self):
        queries = [(1, 2, 100), (2, 5, 100), (3, 4, 100)]
        arraySize = 5
        expectedOutput = 200
        self.assertEqual(arrayManipulation(arraySize, queries), expectedOutput)


if __name__ == "__main__":
    unittest.main()