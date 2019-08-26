import unittest

"""
Given an integer n, we want you to find the amount of four digit
numbers divisible by n that are not palindromes.
A palindromic number is a number that remains the same when
its digits are reversed. Like 1661, for example, it is
"symmetrical".
For example, if n equals 4000, the only four digit numbers
divisible by 4000 are 4000 and 8000. Neither of those numbers
is a palindrome, so the answer would be 2.
If n equals 2002, then the only four digit numbers divisible by
2002 are 2002, 4004, 6006 and 8008. As all of them are
palindromes, the answer would be 0.
Complete a function named nonPalindromicMultiples that
receives an integer n. It should return the amount of four digit
numbers divisible by n that are not palindromes.
"""

MAX_NUMBER = 10000


def isPalindrom(number):
    number = str(number)
    i = 0
    j = len(number) - 1
    while i < j:
        if number[i] != number[j]:
            return False
        i += 1
        j -= 1

    return True


def nonPalindromicMultiples(n):
    count = 0
    for number in range(n, MAX_NUMBER, n):
        if not isPalindrom(number):
            count += 1

    return count


class MyTestCase(unittest.TestCase):
    def test0(self):
        self.assertEqual(2, nonPalindromicMultiples(4000))
        self.assertEqual(0, nonPalindromicMultiples(2002))


if __name__ == '__main__':
    unittest.main()
