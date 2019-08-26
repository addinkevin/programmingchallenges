import unittest


def getAnimalsAlternative(animalWeights, truckCapacity):
    # O(n) solution with hash
    dic = {}
    for w in animalWeights:
        dic[w] = True
        if truckCapacity - w in dic:
            # (truckCapacity - w) + (w) = truckCapacity
            return [w, truckCapacity - w]

    return []


def _getAnimals(animalWeights, truckCapacity):
    # array is sorted, so we need to check start and end
    startIndex = 0
    endIndex = len(animalWeights) - 1

    while startIndex < endIndex:
        sumValue = animalWeights[startIndex] + animalWeights[endIndex]
        if sumValue == truckCapacity:
            return [animalWeights[startIndex], animalWeights[endIndex]]
        elif sumValue < truckCapacity:
            # we need a bigger animal, move start
            startIndex += 1
        else:
            # we need a smaller animal, move end
            endIndex -= 1

    return []


def getAnimals(animalWeights, truckCapacity):
    # Write your code here
    animalWeights.sort()
    return _getAnimals(animalWeights, truckCapacity)


class MyTestCase(unittest.TestCase):
    def test0(self):
        r = getAnimals([1, 5, 2, 7, 9, 3], 10)
        self.assertEqual(10, r[0] + r[1])

    def test1(self):
        r = getAnimalsAlternative([1, 5, 2, 7, 9, 3], 10)
        self.assertEqual(10, r[0] + r[1])


if __name__ == '__main__':
    unittest.main()
