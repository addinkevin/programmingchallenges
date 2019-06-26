import unittest
from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.components = defaultdict(lambda: None)
        self.sizes = defaultdict(lambda: 1)

    def _find(self, u):
        while self.components[u]:
            u = self.components[u]
        return u

    def find(self, u):
        if not self.components[u]:
            return u

        root = self._find(u)
        self.components[u] = root
        return root

    def getSizeComponent(self, u):
        return self.sizes[self.find(u)]

    def union(self, u, v):
        pointerU = self.find(u)
        pointerV = self.find(v)
        if pointerU == pointerV:  # same component
            return self.sizes[pointerU]

        componentUSize = self.sizes[pointerU]
        componentVSize = self.sizes[pointerV]
        if componentUSize > componentVSize:
            self.components[pointerV] = pointerU
            newComponentPointer = pointerU
        else:
            self.components[pointerU] = pointerV
            newComponentPointer = pointerV

        newSize = componentUSize + componentVSize
        self.sizes[newComponentPointer] = newSize
        return newSize


def friendCircleQueries(queries):
    unionFind = UnionFind()
    maxComponentSize = 1

    output = []
    for query in queries:
        newComponentSize = unionFind.union(query[0], query[1])
        if newComponentSize > maxComponentSize:
            maxComponentSize = newComponentSize
        output.append(maxComponentSize)

    return output


class FriendCircleQueriesTest(unittest.TestCase):
    def check(self, queries, expectedOutput):
        self.assertListEqual(friendCircleQueries(queries), expectedOutput)

    def testCase0(self):
        queries = [(1, 2), (1, 3)]
        expectedOutput = [2, 3]
        self.check(queries, expectedOutput)

    def testCase1(self):
        queries = [(1000000000, 23), (11, 3778), (7, 47), (11, 1000000000)]
        expectedOutput = [2, 2, 2, 4]
        self.check(queries, expectedOutput)

    def testCase2(self):
        queries = [(1, 2), (3, 4), (1, 3), (5, 7), (5, 6), (7, 4)]
        expectedOutput = [2, 2, 4, 4, 4, 7]
        self.check(queries, expectedOutput)

    def testCase3(self):
        queries = [(6, 4), (5, 9), (8, 5), (4, 1), (1, 5), (7, 2), (4, 2),
                   (7, 6)]
        expectedOutput = [2, 2, 3, 3, 6, 6, 8, 8]
        self.check(queries, expectedOutput)


if __name__ == "__main__":
    unittest.main()