import unittest


def operationInsert(valueFrequencies, frequencyFrequencies, value):
    currentFreq = valueFrequencies.get(value, 0)
    valueFrequencies[value] = currentFreq + 1
    if currentFreq > 0:
        frequencyFrequencies[currentFreq] -= 1

    frequencyFrequencies[currentFreq + 1] = (
        frequencyFrequencies.get(currentFreq + 1, 0) + 1
    )


def operationDelete(valueFrequencies, frequencyFrequencies, value):
    if value not in valueFrequencies or valueFrequencies[value] == 0:
        return

    currentFreq = valueFrequencies[value]
    valueFrequencies[value] -= 1
    frequencyFrequencies[currentFreq] -= 1
    if currentFreq - 1 > 0:
        frequencyFrequencies[currentFreq - 1] += 1


def operationCheck(valueFrequencies, frequencyFrequencies, frequency):
    if (frequency not in frequencyFrequencies
            or frequencyFrequencies[frequency] == 0):
        return 0
    return 1


def freqQuery(queries):
    valueFrequencies = {}
    frequencyFrequencies = {}
    outputArray = []
    for q in queries:
        if q[0] == 1:
            operationInsert(valueFrequencies, frequencyFrequencies, q[1])
        elif q[0] == 2:
            operationDelete(valueFrequencies, frequencyFrequencies, q[1])
        else:
            result = operationCheck(
                valueFrequencies, frequencyFrequencies, q[1])
            outputArray.append(result)

    return outputArray


class TestFrequencyQuieries(unittest.TestCase):
    def testCase0(self):
        queries = [(1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]
        expectedOutput = [0, 1]

        ans = freqQuery(queries)
        self.assertListEqual(ans, expectedOutput)


if __name__ == "__main__":
    unittest.main()
