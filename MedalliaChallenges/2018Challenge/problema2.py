import unittest


class Cosmo:
    def __init__(self, key):
        self.key = key

    @staticmethod
    def compareKeys(key1, key2):
        if key1 < key2:
            return key2
        return key1

    def tryKey(self, key):
        if self.key == key:
            return 0
        elif self.key < key:
            return 1
        return -1


def merge(keys, cosmo, start, mid, end):
    comparisons = 0
    tmpArray = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        comparisons += 1
        if cosmo.compareKeys(keys[i], keys[j]) == keys[j]:
            tmpArray.append(keys[i])
            i += 1
        else:
            tmpArray.append(keys[j])
            j += 1

    while i <= mid:
        tmpArray.append(keys[i])
        i += 1

    index = start
    for i in range(len(tmpArray)):
        keys[index] = tmpArray[i]
        index += 1

    return comparisons


def _sortKeys(keys, cosmo, start, end):
    if start >= end:
        return 0

    mid = start + (end - start) // 2
    leftComparisons = _sortKeys(keys, cosmo, start, mid)
    rightComparions = _sortKeys(keys, cosmo, mid + 1, end)
    mergeComparisons = merge(keys, cosmo, start, mid, end)

    return leftComparisons + rightComparions + mergeComparisons


def sortKeys(keys, cosmo):
    return _sortKeys(keys, cosmo, 0, len(keys) - 1)


def _binarySearch(keys, cosmo, start, end):
    if start > end:
        return None, 0

    mid = start + (end - start) // 2

    result = cosmo.tryKey(keys[mid])
    if result == 0:
        # correct key
        return keys[mid], 1
    elif result < 0:
        # key too small
        tmp = _binarySearch(keys, cosmo, mid + 1, end)
        return tmp[0], tmp[1] + 1
    else:
        tmp = _binarySearch(keys, cosmo, start, mid - 1)
        return tmp[0], tmp[1] + 1


def binarySearch(keys, cosmo):
    return _binarySearch(keys, cosmo, 0, len(keys) - 1)


def findKey(keys, cosmo):
    comparisons = sortKeys(keys, cosmo)
    key, keyTries = binarySearch(keys, cosmo)
    return key, comparisons + 30 * keyTries


class MyTestCase(unittest.TestCase):
    def test0(self):
        keys = [3, 7, 2, 8]
        cosmo = Cosmo(7)
        result = findKey(keys, cosmo)
        self.assertEqual(7, result[0])


if __name__ == '__main__':
    unittest.main()
