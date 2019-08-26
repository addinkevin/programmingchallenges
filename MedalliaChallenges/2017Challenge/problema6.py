import unittest


def checkShoots(efficiency, shoots, error):
    for goals in range(shoots + 1):
        if abs(efficiency - goals / shoots) < error:
            return True
    return False


def shootingEfficiency(efficiency):
    efficiency = efficiency / 100
    error = 0.1 / 100
    for shoots in range(1, 1000 + 1):
        if checkShoots(efficiency, shoots, error):
            return shoots

    return 1000


class MyTestCase(unittest.TestCase):
    def test0(self):
        self.assertEqual(3, shootingEfficiency(33.3))

    def test1(self):
        self.assertEqual(287, shootingEfficiency(33.4))


if __name__ == '__main__':
    unittest.main()
