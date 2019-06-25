import unittest

CHARACTER_EMPTY_CELL = '-'
CHARACTER_NOT_AVAILABLE = '+'


def _findPositionHorizontal(crossword, i, j):
    wordSize = 0
    k = j - 1
    while (k >= 0 and crossword[i][k] != CHARACTER_NOT_AVAILABLE):
        k -= 1
        wordSize += 1

    newJ = k + 1
    k = j
    while (k < len(crossword) and crossword[i][k] != CHARACTER_NOT_AVAILABLE):
        k += 1
        wordSize += 1

    return i, newJ, wordSize


def _findPositionVertical(crossword, i, j):
    wordSize = 0
    k = i - 1
    while (k >= 0 and crossword[k][j] != CHARACTER_NOT_AVAILABLE):
        k -= 1
        wordSize += 1

    newI = k + 1
    k = i
    while (k < len(crossword) and crossword[k][j] != CHARACTER_NOT_AVAILABLE):
        k += 1
        wordSize += 1

    return newI, j, wordSize


def _findPosition(crossword, i, j):
    checkHorizontally = _findPositionHorizontal(crossword, i, j)
    if checkHorizontally[2] > 1:  # wordSize > 1
        return checkHorizontally + (True, )

    return _findPositionVertical(crossword, i, j) + (False, )


def findPosition(crossword):
    n = len(crossword)
    for i in range(n):
        for j in range(n):
            if crossword[i][j] == CHARACTER_EMPTY_CELL:
                return _findPosition(crossword, i, j)


def _fillTable(table, word, i, j, isHorizontal):
    # Primero verificacion de que la palabra puede ir.
    if isHorizontal:
        k = j
        for c in word:
            if table[i][k] != CHARACTER_EMPTY_CELL and table[i][k] != c:
                return False
            k += 1
    else:
        k = i
        for c in word:
            if table[k][j] != CHARACTER_EMPTY_CELL and table[k][j] != c:
                return False
            k += 1

    # Verificacion OK
    if isHorizontal:
        k = j
        for c in word:
            table[i][k] = c
            k += 1
    else:
        k = i
        for c in word:
            table[k][j] = c
            k += 1
    return True


def findWordAndFillTable(table, words, startIndex):
    i, j, wordSize, isHorizontal = findPosition(table)
    for wordIndex in range(startIndex, len(words)):
        word = words[wordIndex]
        if len(word) != wordSize: continue
        if _fillTable(table, word, i, j, isHorizontal):
            return wordIndex
    return -1


def _crosswordPuzzle(crossword, words):
    wordIndex = -1
    while (True):
        table = [list(s) for s in crossword]  # table copy
        wordIndex = findWordAndFillTable(table, words, wordIndex + 1)
        if (wordIndex == -1):
            # No pude encontrar ninguna palabra
            # So que se encargue el nivel de arriba.
            return -1

        newWordsList = words[:wordIndex] + words[wordIndex + 1:]
        if (len(newWordsList) == 0):
            # Termine de procesar todas las palabras, retorno la tabla
            return table
        # Llamada recursiva para que sigan completando la tabla
        result = _crosswordPuzzle(table, newWordsList)
        if result != -1:
            return result


# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    words = words.split(';')

    result = _crosswordPuzzle(crossword, words)
    return [''.join(s) for s in result]


class CrosswordPuzzleTest(unittest.TestCase):
    def check(self, puzzle, words, expectedOutput):
        puzzle = list(map(str.strip, puzzle.split('\n')))
        expectedOutput = list(map(str.strip, expectedOutput.split('\n')))
        self.assertListEqual(crosswordPuzzle(puzzle, words), expectedOutput)

    def testCase0(self):
        puzzle = """+-++++++++
                    +-++++++++
                    +-++++++++
                    +-----++++
                    +-+++-++++
                    +-+++-++++
                    +++++-++++
                    ++------++
                    +++++-++++
                    +++++-++++"""

        words = "LONDON;DELHI;ICELAND;ANKARA"

        output = """+L++++++++
                    +O++++++++
                    +N++++++++
                    +DELHI++++
                    +O+++C++++
                    +N+++E++++
                    +++++L++++
                    ++ANKARA++
                    +++++N++++
                    +++++D++++"""

        self.check(puzzle, words, output)

    def testCase1(self):
        puzzle = """+-++++++++
                    +-++++++++
                    +-------++
                    +-++++++++
                    +-++++++++
                    +------+++
                    +-+++-++++
                    +++++-++++
                    +++++-++++
                    ++++++++++"""

        words = "AGRA;NORWAY;ENGLAND;GWALIOR"

        output = """+E++++++++
                    +N++++++++
                    +GWALIOR++
                    +L++++++++
                    +A++++++++
                    +NORWAY+++
                    +D+++G++++
                    +++++R++++
                    +++++A++++
                    ++++++++++"""

        self.check(puzzle, words, output)


if __name__ == "__main__":
    unittest.main()