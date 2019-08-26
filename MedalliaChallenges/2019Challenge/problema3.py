import unittest


def getExpectedResult(questionOptions, pointsCorrect, pointsWrong):
    # 1 / questionOption -> points correct
    # (question - 1) / question -> point wrong
    return (pointsCorrect - (questionOptions - 1) * pointsWrong) / questionOptions


def _isExpectedToPassExam(N, P, q, pc, pw):
    expectedResult = 0
    for question in range(N):
        result = getExpectedResult(q[question], pc[question], pw[question])
        # only when the expected result of the question is positive
        if result > 0:
            expectedResult += result

    return expectedResult >= P


def isExpectedToPassExam(N, P, q, pc, pw):
    if _isExpectedToPassExam(N, P, q, pc, pw):
        return "YES"
    return "NO"


class MyTestCase(unittest.TestCase):
    def test0(self):
        r = _isExpectedToPassExam(3, 2, [2, 4, 2], [1, 4, 1], [0.5, 1, 1])
        self.assertEqual(False, r)


if __name__ == '__main__':
    unittest.main()
