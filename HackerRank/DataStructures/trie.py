import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminateFlag = False

    def addChar(self, c):
        if c in self.children:
            return self.children[c]
        newNode = TrieNode()
        self.children[c] = newNode
        return newNode

    def addWord(self, word):
        node = self
        for c in word:
            node = node.addChar(c)

        node.setTerminateFlag()

    def getChild(self, c):
        if c in self.children:
            return self.children[c]
        return None

    def setTerminateFlag(self):
        self.terminateFlag = True

    def terminates(self):
        return self.terminateFlag


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        self.root.addWord(word)

    def contains(self, prefix, exact):
        node = self.root
        for c in prefix:
            node = node.getChild(c)
            if not node:
                return False

        return not exact or node.terminates()


class MyTestCase(unittest.TestCase):
    def test0(self):
        trie = Trie()
        trie.addWord("pepe")
        trie.addWord("peron")

        self.assertEqual(True, trie.contains('pepe', True))
        self.assertEqual(True, trie.contains('per', False))
        self.assertEqual(False, trie.contains('per', True))
        self.assertEqual(False, trie.contains('pej', False))


if __name__ == '__main__':
    unittest.main()
