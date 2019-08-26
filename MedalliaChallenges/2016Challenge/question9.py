import unittest


def calculateOpt(string, opt, i, j):
    if i > j:
        return 0
    if opt[i][j] != -1:
        return opt[i][j]

    if string[i] == string[j]:
        opt[i][j] = max(calculateOpt(string, opt, i + 1, j - 1) + 2,
                        calculateOpt(string, opt, i, j - 1),
                        calculateOpt(string, opt, i + 1, j))
    else:
        opt[i][j] = max(calculateOpt(string, opt, i, j - 1),
                        calculateOpt(string, opt, i + 1, j))

    return opt[i][j]


def funPal(string):
    n = len(string)
    opt = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        opt[i][i] = 1

    for i in range(n):
        calculateOpt(string, opt, 0, i)
        calculateOpt(string, opt, i, n - 1)

    return max(opt[i][n - 1] * opt[0][i - 1] for i in range(1, n))


class MyTestCase(unittest.TestCase):
    def testCase0(self):
        string = "acdapmpomp"
        output = 15
        self.assertEqual(output, funPal(string))

    def testCase1(self):
        string = "axbawbaseksqke"
        output = 25
        self.assertEqual(output, funPal(string))


if __name__ == '__main__':
    unittest.main()
