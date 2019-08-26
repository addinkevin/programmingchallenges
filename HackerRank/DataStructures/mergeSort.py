import unittest


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def merge(array, start, mid, end):
    tmpArray = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if array[i] < array[j]:
            tmpArray.append(array[i])
            i += 1
        else:
            tmpArray.append(array[j])
            j += 1

    while i <= mid:
        tmpArray.append(array[i])
        i += 1
        
    index = start
    for j in range(len(tmpArray)):
        array[index] = tmpArray[j]
        index += 1


def _mergeSort(array, start, end):
    if start >= end:
        return

    midIndex = start + (end - start) // 2
    _mergeSort(array, start, midIndex)
    _mergeSort(array, midIndex + 1, end)
    merge(array, start, midIndex, end)


def mergeSort(array):
    _mergeSort(array, 0, len(array) - 1)


class MyTestCase(unittest.TestCase):
    def testms0(self):
        array = list(range(10, -1, -1))
        sortedArray = list(range(11))
        mergeSort(array)
        self.assertListEqual(sortedArray, array)

    def testms1(self):
        array = [41, 15, 49, 0, 47, 19, 11, 36, 45, 28]
        sortedArray = sorted(array)
        mergeSort(array)
        self.assertListEqual(sortedArray, array)


if __name__ == '__main__':
    unittest.main()
