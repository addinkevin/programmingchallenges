import unittest


#
# Complete the 'findBookPosition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. BOOKIDLIST bookIDList
#       You could use bookIDList as a normal python list with operator "[key]" and "len".
#       Access ith element: bookIDList[i]
#       Get the length of the bookIdList: len(bookIDList)
#  2. INTEGER k
#


def checkPosition(books, k, mid):
    # check if k is in mid -1 , mid or mid + 1
    n = len(books)
    if mid - 1 >= 0 and books[mid - 1] == k:
        return mid - 1
    elif mid + 1 < n and books[mid + 1] == k:
        return mid + 1
    elif books[mid] == k:
        return mid

    return None


def getMidElement(books, mid):
    if 0 < mid < len(books) - 1:
        elements = [books[mid - 1], books[mid], books[mid + 1]]
        elements.sort()
        return elements[1]

    return books[mid]


def _findBookPosition(books, k, start, end):
    # O(lgn) "binary search"
    if start > end:
        return -1

    mid = start + (end - start) // 2

    position = checkPosition(books, k, mid)
    if position is not None:
        return position
    midElement = getMidElement(books, mid)

    if k < midElement:
        # check left
        return _findBookPosition(books, k, start, mid - 2)
    else:
        # check right
        return _findBookPosition(books, k, mid + 2, end)


def findBookPosition(bookIDList, k):
    # Write your code here
    return _findBookPosition(bookIDList, k, 0, len(bookIDList) - 1)


class MyTestCase(unittest.TestCase):
    def test0(self):
        array = [2, 1, 4, 3, 15, 20, 27, 31]
        k = 4
        expected = 2
        r = findBookPosition(array, k)
        self.assertEqual(expected, r)


if __name__ == '__main__':
    unittest.main()
