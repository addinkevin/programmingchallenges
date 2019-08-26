import unittest
from collections import defaultdict


def getNegativePositiveDebts(debt):
    negatives = []
    positives = []
    for x in debt:
        if debt[x] < 0:
            negatives.append([x, debt[x]])
        else:
            positives.append([x, debt[x]])

    return negatives, positives


def getTransaction(negDebt, posDebt):
    moneyToTransfer = min(-negDebt[1], posDebt[1])
    negDebt[1] += moneyToTransfer
    posDebt[1] -= moneyToTransfer

    return posDebt[0], negDebt[0], moneyToTransfer


def processDebt(debt):
    negatives, positives = getNegativePositiveDebts(debt)

    negIndex = 0
    posIndex = 0
    transactions = []
    while negIndex < len(negatives) and posIndex < len(positives):
        negDebt = negatives[negIndex]
        posDebt = positives[posIndex]
        transaction = getTransaction(negDebt, posDebt)
        transactions.append(transaction)
        if negDebt[1] == 0:
            negIndex += 1
        if posDebt[1] == 0:
            posIndex += 1

    return transactions


def getTransfers(tuples):
    debt = defaultdict(int)
    for x, y, money in tuples:
        debt[x] -= money
        debt[y] += money

    return processDebt(debt)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
