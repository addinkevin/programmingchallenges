import unittest
import math

NUMBER_OF_BITS = 32


class Node:
    def __init__(self):
        self.children = {}
        self.value = None


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, string):
        node = self.root
        for c in string:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.value = string


def getMaxXor(trie, query):
    queryBinaryString = getBinaryString(query)
    node = trie.root
    for c in queryBinaryString:
        if c == '0':
            if '1' in node.children:
                node = node.children['1']
            else:
                node = node.children['0']
        else:
            if '0' in node.children:
                node = node.children['0']
            else:
                node = node.children['1']

    return int(node.value, 2) ^ query


def getBinaryString(number):
    n = bin(number)[2:]
    return '0' * (NUMBER_OF_BITS - len(n)) + n


def maxXor(array, queries):
    trie = Trie()
    for number in array:
        trie.add(getBinaryString(number))

    output = []
    for q in queries:
        r = getMaxXor(trie, q)
        output.append(r)

    return output


class MaximumXor(unittest.TestCase):
    def check(self, array, queries, expectedOutput):
        self.assertListEqual(maxXor(array, queries), expectedOutput)

    def testCase0(self):
        array = [0, 1, 2]
        queries = [3, 7, 2]
        expectedOutput = [3, 7, 3]
        self.check(array, queries, expectedOutput)

    def testCase1(self):
        array = [5, 1, 7, 4, 3]
        queries = [2, 0]
        expectedOutput = [7, 7]
        self.check(array, queries, expectedOutput)

    def testCase2(self):
        array = [1, 3, 5, 7]
        queries = [17, 6]
        expectedOutput = [22, 7]
        self.check(array, queries, expectedOutput)


if __name__ == "__main__":
    unittest.main()
