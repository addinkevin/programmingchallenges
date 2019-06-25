import unittest


def getCandies(ratings):
    n = len(ratings)
    candies = [1 for i in range(n)]

    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-1, 0, -1):
        if ratings[i-1] > ratings[i]:
            candies[i-1] = max(candies[i-1], candies[i]+1)

    return sum(candies)


class CandiesTest(unittest.TestCase):
    def check(self, ratingsString, expectedOutput):
        ratings = list(map(int, ratingsString.split()))
        self.assertEqual(getCandies(ratings), expectedOutput)

    def testCase0(self):
        ratingsString = '1 2 2'
        expectedOutput = 4
        self.check(ratingsString, expectedOutput)

    def testCase1(self):
        ratingsString = '2 4 2 6 1 7 8 9 2 1'
        expectedOutput = 19
        self.check(ratingsString, expectedOutput)

    def testCase2(self):
        ratingsString = '2 4 3 5 2 6 4 5'
        expectedOutput = 12
        self.check(ratingsString, expectedOutput)


if __name__ == "__main__":
    unittest.main()
