import unittest
import math

MAX_NUMBER = 1000


def disableNotPrimeNumbers(prime, numberIsPrime):
    for number in range(prime * prime, len(numberIsPrime), prime):
        numberIsPrime[number] = False


def calculatePrimality(numberIsPrime):
    sqrtN = int(math.sqrt(len(numberIsPrime))) + 1
    for i in range(2, sqrtN):
        if not numberIsPrime[i]: continue
        disableNotPrimeNumbers(i, numberIsPrime)


# Alternative version for only one query
def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primality(numbers):
    # It's better to use a integer and bit manipulation instead of a list
    numberIsPrime = [True] * (MAX_NUMBER + 1)
    calculatePrimality(numberIsPrime)

    return [numberIsPrime[number] for number in numbers]


class PrimalityTest(unittest.TestCase):
    def testCase(self):
        self.assertListEqual(primality([15, 5, 7]), [False, True, True])


if __name__ == "__main__":
    unittest.main()