import unittest


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, start, end):
    pivot = array[end]
    index = start
    for i in range(start, end):
        if array[i] < pivot:
            swap(array, index, i)
            index += 1

    swap(array, index, end)
    return index


def _quicksort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    _quicksort(array, start, p - 1)
    _quicksort(array, p + 1, end)


def quicksort(array):
    _quicksort(array, 0, len(array) - 1)


class MyTestCase(unittest.TestCase):
    def testqs0(self):
        array = list(range(10, -1, -1))
        sortedArray = list(range(11))
        quicksort(array)
        self.assertListEqual(sortedArray, array)

    def testqs1(self):
        array = [41, 15, 49, 0, 47, 19, 11, 36, 45, 28]
        sortedArray = sorted(array)
        quicksort(array)
        self.assertListEqual(sortedArray, array)


if __name__ == '__main__':
    unittest.main()
