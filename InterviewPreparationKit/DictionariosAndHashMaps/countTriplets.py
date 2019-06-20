import unittest

def countTriplets(array, ratio):
    dic = {}
    for element in array:
        dic[element] = dic.get(element, 0) + 1

    count = 0
    for element in array:
        nextElement = element * ratio
        nextNextElement = nextElement * ratio
        if nextElement in dic and nextNextElement in dic:
            count += dic[nextElement] * dic[nextNextElement]

    return count


class TestCountTriplets(unittest.TestCase):
    def check(self, array, ratio, output):
        self.assertEqual(countTriplets(array, ratio), output)

    def testCase0(self):
        ratio = 2
        array = [1, 2, 2, 4]
        output = 2
        self.check(array, ratio, output)

    def testCase1(self):
        ratio = 3
        array = [1, 3, 9, 9, 27, 81]
        output = 6
        self.check(array, ratio, output)

    def testCase2(self):
        ratio = 5
        array = [1, 5, 5, 25, 125]
        output = 4
        self.check(array, ratio, output)


if __name__ == "__main__":
    unittest.main()
