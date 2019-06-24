import unittest

MAX_DIGITS = 15
MAX_VALUE = 9 * ((1 << (MAX_DIGITS - 1)) - 1)


def getTargetCount(countMatrix, digits, target):
    if digits == 0 and target == 0:
        return 1
    elif digits == 0 and target != 0:
        return 0
    elif target < 0:
        return 0
    elif countMatrix[digits][target] != -1:
        return countMatrix[digits][target]

    count = 0
    for i in range(10):
        count += getTargetCount(countMatrix, digits - 1,
                                target - i * (1 << (digits - 1)))

    countMatrix[digits][target] = count
    return count


def calculateAccumCounts(countMatrix, maxXthNumber):
    """ Generate accumulative counts,
    c[i] = a_0 + a_1 + ... + a_i
    where a_j = number of decibinaries with decimal value 'a' 
    using MAX_DIGITS digits.
    It is used so we can determine the value of the xth number.
    """
    accumCounts = [1]
    value = 1
    accumCount = 0
    while accumCount < maxXthNumber:
        accumCount = getTargetCount(countMatrix, MAX_DIGITS, value) \
            + accumCounts[-1]
        accumCounts.append(accumCount)
        value += 1

    return accumCounts


def binarySearch(accumCounts, xthNumber):
    start = 0
    stop = len(accumCounts) - 1

    while start <= stop:
        midIndex = start + (stop - start) // 2
        midValue = accumCounts[midIndex]
        if xthNumber == midValue:
            return midIndex
        elif xthNumber < midValue:
            stop = midIndex - 1
        else:
            start = midIndex + 1

    # border case
    if start > len(accumCounts) - 1:
        return len(accumCounts) - 1

    return start


def getNumberOfDigits(countMatrix, target, iteration):
    digits = 1
    while getTargetCount(countMatrix, digits, target) < iteration:
        digits += 1

    return digits


def getDigitValue(countMatrix, target, iteration, digit):
    digitValue = 0
    lastCountSum = 0
    countSum = 0
    while countSum < iteration:
        lastCountSum = countSum
        countSum += getTargetCount(countMatrix, digit - 1,
                                   target - digitValue * (1 << (digit - 1)))
        digitValue += 1

    digitValue -= 1
    newIteration = iteration - lastCountSum
    newTarget = target - digitValue * (1 << (digit - 1))
    return digitValue, newIteration, newTarget


def generateNumberWithDigits(countMatrix, target, iteration, numberOfDigits):
    result = 0
    for digit in range(numberOfDigits, 0, -1):
        tmp = getDigitValue(countMatrix, target, iteration, digit)
        digitValue, iteration, target = tmp
        result = result + digitValue * 10**(digit - 1)

    return result


def generateNumber(countMatrix, target, iteration):
    numberOfDigits = getNumberOfDigits(countMatrix, target, iteration)

    result = generateNumberWithDigits(countMatrix, target, iteration,
                                      numberOfDigits)

    return result


def generateXthNumber(countMatrix, accumCounts, xthNumber):
    """ Generate the xth number, determining the decimal value 
    using accumCounts array.
    """
    if xthNumber == 1: return 0
    value = binarySearch(accumCounts, xthNumber)
    iteration = (accumCounts[value] - accumCounts[value - 1]) \
              - (accumCounts[value] - xthNumber)
    
    return generateNumber(countMatrix, value, iteration)


def decibinaryNumbers(queries):
    maxXthNumber = max(queries)
    # countMatrix[digit][value]: numbers of decibinaries(count) with decimal value
    # 'value' using 'digit' digits
    countMatrix = [[-1 for j in range(MAX_VALUE + 1)]
                   for i in range(MAX_DIGITS + 1)]
    accumCounts = calculateAccumCounts(countMatrix, maxXthNumber)

    output = []
    for query in queries:
        result = generateXthNumber(countMatrix, accumCounts, query)
        output.append(result)

    return output


class BinarySearchTest(unittest.TestCase):
    def testCase0(self):
        arr = [1, 3, 6, 9]
        self.assertEqual(binarySearch(arr, 0), 0)
        self.assertEqual(binarySearch(arr, 2), 1)
        self.assertEqual(binarySearch(arr, 3), 1)
        self.assertEqual(binarySearch(arr, 5), 2)
        self.assertEqual(binarySearch(arr, 6), 2)
        self.assertEqual(binarySearch(arr, 8), 3)
        self.assertEqual(binarySearch(arr, 9), 3)
        self.assertEqual(binarySearch(arr, 10), 3)

    def testCase1(self):
        arr = [1, 4]
        self.assertEqual(binarySearch(arr, 3), 1)
        self.assertEqual(binarySearch(arr, 0), 0)
        self.assertEqual(binarySearch(arr, 6), 1)


class DecibinaryTest(unittest.TestCase):
    def check(self, queries, expectedOutput):
        self.assertListEqual(decibinaryNumbers(queries), expectedOutput)

    def testCase0(self):
        queries = [1, 2, 3, 4, 10]
        expectedOutput = [0, 1, 2, 10, 100]
        self.check(queries, expectedOutput)

    def testCase1(self):
        queries = [8, 23, 19, 16, 26, 7, 6]
        expectedOutput = [12, 23, 102, 14, 111, 4, 11]
        self.check(queries, expectedOutput)

    def testCase2(self):
        queries = [19, 25, 6, 8, 20, 10, 27, 24, 30, 11]
        expectedOutput = [102, 103, 11, 12, 110, 100, 8, 31, 32, 5]
        self.check(queries, expectedOutput)

    def testGenerateNumbers(self):
        countMatrix = [[-1 for j in range(MAX_VALUE + 1)]
                       for i in range(MAX_DIGITS + 1)]

        number = generateNumber(countMatrix, 4, 4)
        self.assertEqual(number, 100)


if __name__ == "__main__":
    unittest.main()
