import unittest

"""
Given N people with the following features:
Id
Salary
Number of children
Civil Status
Age
We want you to return the id of the person with the third best
final salary between the group of people that fulfill the next
conditions:
Being single.
Having 1 to 3 children.
Having between 30 and 40 years old
where the final salary is obtained with the following formulae:
A first discount of 15 percent of the salary and after that
another discount of max(0, (4 - amount of children)) percent
of the previous result
"""

import heapq

STATUS_DIVORCED = "divorced"
STATUS_SINGLE = "single"
STATUS_WIDOWED = "widowed"


class Heap:
    def __init__(self, size):
        self.heap = []
        self.size = size

    def insert(self, item):
        if len(self.heap) < self.size:
            heapq.heappush(self.heap, item)
        else:
            heapq.heappushpop(self.heap, item)

    def peek(self):
        return self.heap[0]


class Person:
    def __init__(self, id, salary, childrenCount, civilStatus, age):
        self.id = id
        self.salary = salary
        self.childrenCount = childrenCount
        self.civilStatus = civilStatus
        self.age = age
        self.finalSalary = self.calculateFinalSalary()

    def __lt__(self, other):
        return self.finalSalary < other.finalSalary

    def calculateFinalSalary(self):
        return self.salary * 0.85 * max(0, 4 - self.childrenCount) / 100


def meetConditions(person):
    isSingle = (person.civilStatus == STATUS_SINGLE)
    oneToThreeChildren = (1 <= person.childrenCount <= 3)
    ageCondition = (30 <= person.age <= 40)
    return isSingle and oneToThreeChildren and ageCondition


def createPersonsArray(persons):
    personArray = []
    for id, salary, childrenCount, civilStatus, age in persons:
        person = Person(id, salary, childrenCount, civilStatus, age)
        personArray.append(person)

    return personArray


def getThirdBestFinalSalary(persons):
    persons = createPersonsArray(persons)
    heap = Heap(3)
    for person in persons:
        if meetConditions(person):
            heap.insert(person)

    return heap.peek().id


class MyTestCase(unittest.TestCase):
    def test0(self):
        persons = [
            (1, 100, 2, 'single', 32),
            (2, 1000, 2, 'single', 30),
            (3, 10000, 3, 'single', 40),
            (4, 1000000, 2, 'single', 39),
            (5, 12, 1, 'divorced', 34)
        ]
        self.assertEqual(2, getThirdBestFinalSalary(persons))


if __name__ == '__main__':
    unittest.main()
