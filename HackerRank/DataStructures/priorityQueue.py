import unittest
import heapq


class PQItem:
    def __init__(self, item, comparator):
        self.item = item
        self.comparator = comparator

    def __lt__(self, other):
        return self.comparator(self.item, other.item) < 0

    def __eq__(self, other):
        return self.comparator(self.item, other.item) == 0

    def __gt__(self, other):
        return self.comparator(self.item, other.item) > 0


class PriorityQueue:
    def __init__(self, comparator):
        self.pq = []
        self.comparator = comparator

    def append(self, value):
        pqItem = PQItem(value, self.comparator)
        heapq.heappush(self.pq, pqItem)

    def peek(self):
        pqItem = self.pq[0]
        return pqItem.item

    def pop(self):
        pqItem = heapq.heappop(self.pq)
        return pqItem.item

    def isEmpty(self):
        return len(self.pq) == 0

    def __len__(self):
        return len(self.pq)


class MyTestCase(unittest.TestCase):
    def testMaxPQ(self):
        pq = PriorityQueue(lambda x, y: y - x)
        pq.append(3)
        pq.append(9)
        pq.append(5)
        pq.append(4)
        self.assertEqual(4, len(pq))
        self.assertEqual(False, pq.isEmpty())
        self.assertEqual(9, pq.peek())
        self.assertEqual(9, pq.pop())
        self.assertEqual(5, pq.peek())
        self.assertEqual(False, pq.isEmpty())
        self.assertEqual(5, pq.pop())
        self.assertEqual(4, pq.pop())
        self.assertEqual(3, pq.pop())
        self.assertEqual(True, pq.isEmpty())

    def testMinPQ(self):
        pq = PriorityQueue(lambda x, y: x - y)
        pq.append(3)
        pq.append(9)
        pq.append(5)
        pq.append(4)
        self.assertEqual(False, pq.isEmpty())
        self.assertEqual(3, pq.peek())
        self.assertEqual(3, pq.pop())
        self.assertEqual(4, pq.peek())
        self.assertEqual(False, pq.isEmpty())
        self.assertEqual(4, pq.pop())
        self.assertEqual(5, pq.pop())
        self.assertEqual(9, pq.pop())
        self.assertEqual(True, pq.isEmpty())


if __name__ == '__main__':
    unittest.main()
