import unittest


def abbreviation(a, b):
    if len(b) > len(a):
        return False

    opt = [[False for j in range(len(b)+1)] for i in range(len(a)+1)]

    # Base case: Abbreviate part of string 'a' to an empty string
    opt[0][0] = True
    for i in range(1, len(a)+1):
        opt[i][0] = a[:i] == a[:i].lower()

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            charA = a[i-1]
            charB = b[j-1]
            if charA == charB:  # Match
                opt[i][j] = opt[i-1][j-1]
            elif charA.upper() == charB:
                # It can capitalize charA or not to try to find an abbreviation
                opt[i][j] = opt[i-1][j-1] | opt[i-1][j]
            elif charA == charA.lower():
                # We can delete charA because it's lowercase.
                opt[i][j] = opt[i-1][j]

    return opt[-1][-1]


class AbbreviationTest(unittest.TestCase):
    def testCase0(self):
        a = "daBcd"
        b = "ABC"
        self.assertTrue(abbreviation(a, b))


if __name__ == "__main__":
    unittest.main()
