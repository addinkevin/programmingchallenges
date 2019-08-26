import unittest

"""
In a starship with N passengers intended to be humans, you
know that exactly one of them is an android pretending to be a
passenger, and you have to discover it as soon as possible.
An android is almost indistinguishable from a human, the only
way to distinguish them is by running a blood test that takes
many hours, and there is only one machine in the ship to run it.
Fortunately, a blood test can mix the blood of various subjects,
and the result will be positive if and only if one of the subjects is
an android.
"""


class TestMachine:
    def testPassengers(self, passengers):
        pass


def _testPassengers(passengers, testMachine, start, end):
    """
    O(n) solution given by
    T(n) = T(n/2) + O(n), O(n) == testMachine process time over segment
    """
    if start > end:
        return None
    elif start == end:
        return start

    mid = start + (end - start) // 2
    alienIsInLeft = testMachine.testPassengers(passengers[start:mid + 1])
    if alienIsInLeft:
        return _testPassengers(passengers, testMachine, start, mid)

    return _testPassengers(passengers, testMachine, mid + 1, end)


def testPassengers(passengers, testMachine):
    return _testPassengers(passengers, testMachine, 0, len(passengers) - 1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
