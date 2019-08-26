import unittest
import collections


def checkIfHasPalindromePermutation(string):
    counter = collections.Counter(string)
    flag = False
    for c in counter:
        if counter[c] % 2 == 1:
            if flag:
                return False
            flag = True

    return True


class Question9Test(unittest.TestCase):
    def testCase0(self):
        strings = ['aaabbbb', 'cdefghmnopqrstuvw']
        outputs = [True, False]
        for i, o in zip(strings, outputs):
            self.assertEqual(o, checkIfHasPalindromePermutation(i))


if __name__ == '__main__':
    unittest.main()
