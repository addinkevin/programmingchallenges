import unittest


def countInversionsBetween(arr, low, mid, high):
    pointerA = low
    pointerB = mid + 1
    inversionCount = 0
    newArr = []
    while (pointerA <= mid and pointerB <= high):
        if arr[pointerA] <= arr[pointerB]:
            # No inversion
            newArr.append(arr[pointerA])
            pointerA += 1
        else:
            inversionCount += mid - pointerA + 1
            newArr.append(arr[pointerB])
            pointerB += 1

    newArr += arr[pointerA:mid + 1]
    newArr += arr[pointerB:high + 1]

    index = low
    for k in newArr:
        arr[index] = k
        index += 1

    return inversionCount


def sortAndCountInversions(arr, low, high):
    if low == high: return 0

    mid = low + (high - low) // 2

    count1 = sortAndCountInversions(arr, low, mid)
    count2 = sortAndCountInversions(arr, mid + 1, high)
    count3 = countInversionsBetween(arr, low, mid, high)

    return count1 + count2 + count3


def countingInversion(array):
    return sortAndCountInversions(array, 0, len(array) - 1)


class CountingInversionTest(unittest.TestCase):
    def check(self, arr, expectedOutput):
        self.assertEqual(countingInversion(arr), expectedOutput)

    def testCase0(self):
        arr = [1, 1, 1, 2, 2]
        expectedOutput = 0
        self.check(arr, expectedOutput)

    def testCase1(self):
        arr = [2, 1, 3, 1, 2]
        expectedOutput = 4
        self.check(arr, expectedOutput)

    def testCase2(self):
        arr = [5, 4, 3, 2, 1]
        expectedOutput = 10
        self.check(arr, expectedOutput)


if __name__ == "__main__":
    unittest.main()