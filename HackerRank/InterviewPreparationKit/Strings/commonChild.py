import unittest

"""
Common child
https://www.hackerrank.com/challenges/common-child/problem
"""


def commonChild(s1, s2):
    opt = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            match = 0
            if s1[i - 1] == s2[j - 1]:
                match = 1
            opt[i][j] = max(opt[i - 1][j], opt[i][j - 1], opt[i - 1][j - 1] + match)

    return opt[-1][-1]


class CommonChildTest(unittest.TestCase):
    def test0(self):
        s1 = "HARRY"
        s2 = "SALLY"
        self.assertEqual(2, commonChild(s1, s2))

    def test1(self):
        s1 = "ABCDEF"
        s2 = "FBDAMN"
        self.assertEqual(2, commonChild(s1, s2))


if __name__ == '__main__':
    unittest.main()
