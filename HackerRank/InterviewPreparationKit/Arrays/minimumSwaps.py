import unittest


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def minimumSwaps(arr):
    i = 0
    swaps = 0
    while i < len(arr):
        if arr[i] == i + 1:
            i += 1
        else:
            swap(arr, i, arr[i] - 1)
            swaps += 1

    return swaps


class MinimumSwapsTest(unittest.TestCase):
    def testCase(self):
        array = [1, 3, 5, 2, 4, 6, 7]
        expectedOutput = 3
        self.assertEqual(minimumSwaps(array), expectedOutput)


if __name__ == "__main__":
    unittest.main()