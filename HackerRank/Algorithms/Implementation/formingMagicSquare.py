import unittest


# https://www.hackerrank.com/challenges/magic-square-forming/

def getMatrixDiff(magicSquareMatrix, matrix):
    diff = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            diff += abs(matrix[row][col] - magicSquareMatrix[row][col])

    return diff


def formingMagicSquare(matrix):
    magicSquareMatrixes = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                           [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                           [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                           [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                           [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                           [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                           [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                           [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    minCost = float('inf')
    for magicSquareMatrix in magicSquareMatrixes:
        cost = getMatrixDiff(magicSquareMatrix, matrix)
        minCost = min(cost, minCost)

    return minCost


class FormingMagicSquareTest(unittest.TestCase):
    def testCase0(self):
        matrix = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
        expectedCost = 4
        self.assertEqual(expectedCost, formingMagicSquare(matrix))

    def testCase1(self):
        matrix = [[4, 4, 7], [3, 1, 5], [1, 7, 9]]
        expectedCost = 20
        self.assertEqual(expectedCost, formingMagicSquare(matrix))


if __name__ == '__main__':
    unittest.main()
