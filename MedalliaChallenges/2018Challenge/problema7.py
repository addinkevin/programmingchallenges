import unittest
import random
import math

SIMULATIONS = 10000


def getMajorityCount(coalition, votes):
    voteSum = sum(votes[member] for member in coalition)
    return math.ceil(voteSum / len(coalition))


def isASwingVoter(coalition, votes, memberWorkingFor):
    majorityCount = getMajorityCount(coalition, votes)
    voteSum = sum(votes[member] for member in coalition)

    return voteSum - votes[memberWorkingFor] < majorityCount


def getRandomCoalition(members, memberWorkingFor):
    solution = [memberWorkingFor]
    for member in members:
        if memberWorkingFor != member and random.random() < 0.5:
            solution.append(member)

    return solution


def simulateCurrentPower(votes, memberWorkingFor):
    count = 0
    for simulation in range(SIMULATIONS):
        coalition = getRandomCoalition(range(len(votes)), memberWorkingFor)
        if isASwingVoter(coalition, votes, memberWorkingFor):
            count += 1

    return count


def currentPowerLessThanDesired(memberCount, currentPower, desiredPower):
    return currentPower / SIMULATIONS < desiredPower / (1 << (memberCount - 1))


def computeVotesRequired(memberCount, currentPower, desiredPower):
    votes = desiredPower * SIMULATIONS / (1 << (memberCount - 1)) - currentPower
    votes = (votes / SIMULATIONS) * (1 << (memberCount - 1))
    return math.ceil(votes)


def poweringUp(memberCount, votes, memberWorkingFor, desiredPower):
    currentPower = simulateCurrentPower(votes, memberWorkingFor)
    if currentPowerLessThanDesired(memberCount, currentPower, desiredPower):
        return computeVotesRequired(memberCount, currentPower, desiredPower)

    return 0


class MyTestCase(unittest.TestCase):
    def test0(self):
        memberCount = 4
        votes = [3, 2, 1, 1]
        memberWorkingFor = 0
        desiredPower = 5
        self.assertEqual(0, poweringUp(memberCount, votes, memberWorkingFor, desiredPower))


if __name__ == '__main__':
    unittest.main()
