"""
Un banco tiene N tarjetas de crédito y quiere saber si hay un conjunto de más 
de N/2 tarjetas que corresponden a la misma cuenta. Las tarjetas no se pueden 
leer individualmente, sólo se pueden comparar entre sí mediante un aparato 
que lee dos tarjetas y responde "Iguales" o "Distitnas". Diseñar un algoritmo 
O(N log(N)) para determinar si existe o no el conjunto buscado.

isThereAMajority: O(n log(n)), 2T(n/2) + O(n)
checkMajority: O(n)

Lógica:
Sea Z la carta que tiene mayoría, tal que Z = X + Y
[  X   |    Y   ], con X= cantidad en la parte izquierda, Y idem parte derecha
Entonces si Z > N/2, no puede pasar que X <= N/4 y Y <= N/4, por lo que
se cumple que la carta Z es mayoritaria en por lo menos una de las mitades.
Luego de resolver las mitades, hay que vericar que la carta sea mayoritaría.

"""

def cardsAreEqual(card1, card2):
    return card1 == card2

def checkMajority(cards, majorityCard):
    count = 0
    for card in cards:
        if cardsAreEqual(card, majorityCard):
            count += 1

    return count > len(cards)/2


def isThereAMajority(cards):
    if len(cards) == 0:
        return None
    elif len(cards) == 1:
        return cards[0]

    resultLeft = isThereAMajority(cards[:len(cards)//2])
    resultRight = isThereAMajority(cards[len(cards)//2:])
    if resultLeft and checkMajority(cards, resultLeft):
        return resultLeft
    if resultRight and checkMajority(cards, resultRight):
        return resultRight
    return None


def _test(cards, resultExpected):
    result = isThereAMajority(cards)
    print("Cartas: ", cards, ", ", resultExpected == result,
          " ,Resultado Obtenido: ", result, ", Resultado Esperado: ",
          resultExpected)


def test():
    _test('RARBRCRDR', 'R')
    _test('AKKARAA', 'A')
    _test('ABCDEFGHIJK', None)
    _test('AAAAAAAAAA', 'A')
    _test('AAAABBBB', None)
    _test('AABAAB', 'A')
    _test('ACCAAB', None)
    _test('ABCAAA', 'A')
    _test('ABBAAA', 'A')


if __name__ == "__main__":
    test()
