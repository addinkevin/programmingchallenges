import unittest


class Person:
    def __init__(self, city, country):
        self.city = city
        self.country = country


class Call:
    def __init__(self, callee, receiver, duration):
        self.callee = callee
        self.receiver = receiver
        self.duration = duration

    def getCallCost(self):
        raise NotImplementedError


class LocalCall(Call):
    def __init__(self, callee, receiver, duration):
        super().__init__(callee, receiver, duration)
        self.costPerSecond = 1

    def getCallCost(self):
        return self.costPerSecond * self.duration


class NationalCall(Call):
    def __init__(self, callee, receiver, duration):
        super().__init__(callee, receiver, duration)
        self.costLessThanMinute = 10
        self.costAfterMinutePerSec = 1

    def getCallCost(self):
        if self.duration < 60:
            return self.costLessThanMinute
        return self.costLessThanMinute + (self.duration - 60) * self.costAfterMinutePerSec


class InternationalCall(Call):
    def __init__(self, callee, receiver, duration):
        super().__init__(callee, receiver, duration)
        self.costPerSecond = 20
        self.costPerSecondDiscount = 15

    def getCallCost(self):
        if self.duration < 10 * 60:
            return self.costPerSecond * self.duration

        return self.costPerSecondDiscount * self.duration


def createCallObjects(array):
    pass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
