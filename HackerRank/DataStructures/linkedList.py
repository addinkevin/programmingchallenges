import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def add(self, data):
        node = Node(data)
        self.len += 1
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def addFirst(self, data):
        node = Node(data)
        self.len += 1
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def iterForward(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def iterBackward(self):
        node = self.tail
        while node:
            yield node.data
            node = node.prev


class MyTestCase(unittest.TestCase):
    def testLinkedList(self):
        ll = LinkedList()
        for i in range(5):
            ll.add(i)

        self.assertEqual(5, len(ll))

        value = 0
        for i in ll.iterForward():
            self.assertEqual(i, value)
            value += 1

        value = 4
        for i in ll.iterBackward():
            self.assertEqual(i, value)
            value -= 1
