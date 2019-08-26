import unittest


class BitArray:
    def __init__(self, size):
        self.size = size
        self.n = 0

    def set(self, bit):
        self.n = self.n | (1 << bit)

    def get(self, bit):
        return (self.n & (1 << bit)) != 0

    def flip(self, bit):
        self.n = self.n ^ (1 << bit)

    def flipAll(self):
        self.n = ~self.n

    def clear(self, bit):
        self.n = (self.n & (~(1 << bit)))

    def update(self, bit, bitIs1):
        self.clear(bit)
        if bitIs1:
            self.set(bit)

    def clearBitsMSBThroughI(self, i):
        mask = (1 << i) - 1
        self.n = self.n & mask

    def getN(self):
        mask = (1 << self.size) - 1
        return self.n & mask


class MyTestCase(unittest.TestCase):
    def test0(self):
        bitArray = BitArray(4)
        bitArray.set(0)
        self.assertEqual(True, bitArray.get(0))
        self.assertEqual(False, bitArray.get(1))
        bitArray.set(1)
        self.assertEqual(True, bitArray.get(1))

        self.assertEqual(3, bitArray.getN())

        bitArray.flipAll()
        self.assertEqual(12, bitArray.getN())


if __name__ == '__main__':
    unittest.main()
