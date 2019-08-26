import unittest


#
# Complete the 'isPossible' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x_start
#  2. INTEGER y_start
#  3. INTEGER x_end
#  4. INTEGER y_end
#

def _isPossible(x_start, y_start, x_end, y_end):
    if x_start > x_end or y_start > y_end:
        return False
    if x_start == x_end and y_start == y_end:
        return True

    # try first possibility
    if _isPossible(x_start + y_start, y_start, x_end, y_end):
        return True

    # try second possibility
    return _isPossible(x_start, y_start + x_start, x_end, y_end)


def isPossible(x_start, y_start, x_end, y_end):
    if _isPossible(x_start, y_start, x_end, y_end):
        return "YES"
    return "NO"


class MyTestCase(unittest.TestCase):
    def test0(self):
        self.assertEqual(False, _isPossible(1, 1, 6, 3))


if __name__ == '__main__':
    unittest.main()
