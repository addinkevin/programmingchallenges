import unittest


def _binarySearch(array, value, start, end):
    if start > end:
        return -1

    midIndex = start + (end - start) // 2

    if array[midIndex] == value:
        return midIndex
    elif array[midIndex] < value:
        return _binarySearch(array, value, midIndex + 1, end)
    else:
        return _binarySearch(array, value, start, midIndex - 1)


def binarySearchIterative(array, value):
    start = 0
    end = len(array) - 1
    while start <= end:
        midIndex = start + (end - start) // 2
        if array[midIndex] == value:
            return midIndex
        elif array[midIndex] < value:
            start = midIndex + 1
        else:
            end = midIndex - 1

    return -1


def binarySearch(array, x):
    return _binarySearch(array, x, 0, len(array) - 1)


class MyTestCase(unittest.TestCase):
    def test0(self):
        array = range(100)
        for i in range(len(array)):
            self.assertEqual(i, binarySearch(array, i))
        for i in range(len(array)):
            self.assertEqual(i, binarySearchIterative(array, i))


if __name__ == '__main__':
    unittest.main()
