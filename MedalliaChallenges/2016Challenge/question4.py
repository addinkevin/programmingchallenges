import unittest
import itertools
import collections


def getWords(phrase):
    words = []
    wordBuilder = []
    for c in phrase:
        if c in (' ', '.', ','):
            if len(wordBuilder) != 0:
                words.append(''.join(wordBuilder))
                wordBuilder = []
        else:
            wordBuilder.append(c)

    if len(wordBuilder) != 0:
        words.append(''.join(wordBuilder))

    return words


def isAnagram(word, phraseWord):
    if len(word) != len(phraseWord):
        return 0

    wordCounter = collections.Counter(word)
    phraseWordCounter = collections.Counter(phraseWord)
    for c in wordCounter:
        if wordCounter[c] != phraseWordCounter[c]:
            return False

    return True


def _anagramParty(word, phrase):
    phrase = getWords(phrase)

    count = 0
    for phraseWord in phrase:
        if isAnagram(word, phraseWord):
            count += 1
    return count


def anagramParty(word, phraseArray):
    output = []
    for phrase in phraseArray:
        output.append(_anagramParty(word, phrase))
    return output


class MyTestCase(unittest.TestCase):
    def testCase0(self):
        word = 'word'
        phraseArray = [
            'word is drow when dwor',
            'nothing to see here'
        ]
        expectedOutput = [
            3,
            0
        ]
        self.assertListEqual(expectedOutput, anagramParty(word, phraseArray))


if __name__ == '__main__':
    unittest.main()
