import unittest
from collections import deque


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        self.queue = deque()

    def append(self, value):
        self.queue.append(value)

    def pop(self):
        return self.queue.popleft()

    def isEmpty(self):
        return len(self.queue) == 0


class MyTestCase(unittest.TestCase):
    def testQueue(self):
        queue = Queue()
        for i in range(3):
            queue.append(i)
        for i in range(3):
            self.assertEqual(i, queue.pop())

    def testStack(self):
        stack = Stack()
        for i in range(3):
            stack.push(i)
        for i in range(2, -1, -1):
            self.assertEqual(i, stack.pop())


if __name__ == '__main__':
    unittest.main()
