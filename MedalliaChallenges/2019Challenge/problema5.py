import unittest


class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []

    def push(self, element):
        if self.getCount() < self.maxSize:
            self.stack.append(element)

    def pop(self):
        if self.getCount() > 0:
            return self.stack.pop()

    def getCount(self):
        return len(self.stack)

    def isFull(self):
        return self.getCount() == self.maxSize

    def isEmpty(self):
        return self.getCount() == 0


class StackOfStacks:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stacks = []

    def add(self, element):
        if len(self.stacks) == 0:
            self.stacks.append(Stack(self.maxSize))

        lastStack = self.stacks[-1]
        if lastStack.isFull():
            newStack = Stack(self.maxSize)
            self.stacks.append(newStack)
            newStack.push(element)
        else:
            lastStack.push(element)

    def _fillStack(self, stackIndex):
        # fill stackIndex with next stack element
        if not (stackIndex + 1 < len(self.stacks)):
            # no next stack
            return

        currentStack = self.stacks[stackIndex]
        nextStack = self.stacks[stackIndex + 1]
        currentStack.push(nextStack.pop())
        self._fillStack(stackIndex + 1)

    def remove(self):
        if len(self.stacks) == 0:
            return
        element = self.stacks[0].pop()
        self._fillStack(0)
        lastStack = self.stacks[-1]
        if lastStack.isEmpty():
            self.stacks.pop()

        return element

    def count(self, stackIndex):
        if stackIndex >= len(self.stacks) or stackIndex < 0:
            return -1

        return self.stacks[stackIndex].getCount()


# Write your code here
class Solution:
    def __init__(self, max_stack_size):
        self.stackOfStacks = StackOfStacks(max_stack_size)

    def add(self, element):
        self.stackOfStacks.add(element)

    def remove(self):
        return self.stackOfStacks.remove()

    def count(self, stack_index):
        return self.stackOfStacks.count(stack_index)


class MyTestCase(unittest.TestCase):
    def test0(self):
        s = StackOfStacks(2)
        s.add(13)
        s.add(7)
        s.add(17)
        self.assertEqual(2, s.count(0))
        self.assertEqual(1, s.count(1))
        s.add(2)
        self.assertEqual(2, s.count(1))
        s.add(47)
        self.assertEqual(7, s.remove())
        self.assertEqual(2, s.count(0))
        self.assertEqual(2, s.count(1))
        self.assertEqual(-1, s.count(2))


if __name__ == '__main__':
    unittest.main()
