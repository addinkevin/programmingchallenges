import unittest


def _waysToClimb(n, mem):
    if n in mem:
        return mem[n]
    elif n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        mem[n] = _waysToClimb(n - 1, mem) + _waysToClimb(n - 2, mem)
        return mem[n]


def waysToClimb(n):
    return _waysToClimb(n, {})


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(89, waysToClimb(10))


if __name__ == '__main__':
    unittest.main()
