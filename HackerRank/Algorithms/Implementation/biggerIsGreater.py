import unittest

# https://www.hackerrank.com/challenges/bigger-is-greater/problem


def reverseSuffix(seq, pivotIndex):
    i = pivotIndex + 1
    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1


def getNextPermutation(seq):
    # find longest weak increasing prefix
    i = len(seq) - 1
    while i > 0 and seq[i - 1] >= seq[i]:
        i -= 1

    # there's no next permutation
    if i <= 0:
        return False

    pivotIndex = i - 1
    i = len(seq) - 1
    # find rightmost element that exceeds the pivot value
    while seq[pivotIndex] >= seq[i]:
        i -= 1

    # increase prefix
    seq[i], seq[pivotIndex] = seq[pivotIndex], seq[i]

    reverseSuffix(seq, pivotIndex)

    return True


def getPrevPermutation(seq):
    # find longest weak decreasing prefix
    i = len(seq) - 1
    while i > 0 and seq[i - 1] <= seq[i]:
        i -= 1

    # there's no prev permutation
    if i <= 0:
        return False

    pivotIndex = i - 1
    i = len(seq) - 1
    # find rightmost element that is below the pivot value
    while seq[pivotIndex] <= seq[i]:
        i -= 1

    # decrease prefix
    seq[i], seq[pivotIndex] = seq[pivotIndex], seq[i]

    reverseSuffix(seq, pivotIndex)
    return True


def biggerIsGreater(string):
    seq = list(string)
    r = getNextPermutation(seq)
    if r:
        return ''.join(seq)
    return 'no answer'


def lowerIsGreater(string):
    seq = list(string)
    r = getPrevPermutation(seq)
    if r:
        return ''.join(seq)
    return 'no answer'


class BiggerIsGreaterTest(unittest.TestCase):
    def testCase0(self):
        inputStrings = ['ab', 'bb', 'hefg', 'dhck', 'dkhc']
        outputStrings = ['ba', 'no answer', 'hegf', 'dhkc', 'hcdk']
        for i in range(len(inputStrings)):
            with self.subTest(i=i):
                inputString = inputStrings[i]
                outputString = outputStrings[i]
                self.assertEqual(outputString, biggerIsGreater(inputString))

    def testCase1(self):
        inputStrings = ['ba', 'abc', 'hegf', 'dhkc', 'hcdk']
        outputStrings = ['ab', 'no answer', 'hefg', 'dhck', 'dkhc']
        for i in range(len(inputStrings)):
            with self.subTest(i=i):
                inputString = inputStrings[i]
                outputString = outputStrings[i]
                self.assertEqual(outputString, lowerIsGreater(inputString))


if __name__ == '__main__':
    unittest.main()
