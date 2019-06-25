import unittest


def _stepPerms(currentStep, totalSteps, mem):
    if currentStep > totalSteps:
        return 0
    elif currentStep == totalSteps:
        return 1
    elif currentStep in mem:
        return mem[currentStep]

    result = _stepPerms(currentStep+1, totalSteps, mem) \
           + _stepPerms(currentStep+2, totalSteps, mem) \
           + _stepPerms(currentStep+3, totalSteps, mem)

    mem[currentStep] = result
    return result


# Complete the stepPerms function below.
def stepPerms(n):
    return _stepPerms(0, n, {})


class DavidStaircaseTest(unittest.TestCase):
    def testCases(self):
        tests = [(1, 1), (3, 4), (7, 44)]
        for i in range(len(tests)):
            with self.subTest(i=i):
                test = tests[i]
                self.assertEqual(stepPerms(test[0]), test[1])


if __name__ == "__main__":
    unittest.main()