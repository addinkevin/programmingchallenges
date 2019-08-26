import unittest

"""
For example, let's say that her meetings are M = {(1, 2), (4, 5), (5, 6)}.
This would mean that she has one chunk of time to code between her
meetings: (2, 4).

We should take into account the fact that sometimes employees get
invited to meetings that overlap. For example, if her meetings were M =
{(1, 3), (6, 7), (2, 9)}, she would then have 0 chunks of time to code
between her meetings.
"""


class Meeting:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def merge(self, other):
        self.start = min(self.start, other.start)
        self.finish = max(self.finish, other.finish)

    def overlap(self, other):
        return not (self.finish <= other.start or other.finish <= self.start)

    def __str__(self):
        return '[{0}, {1}]'.format(self.start, self.finish)

    def __repr__(self):
        return str(self)


def _numberOfChunks(nonOverlappingMeetings):
    chunks = 0
    for i in range(1, len(nonOverlappingMeetings)):
        prevMeeting = nonOverlappingMeetings[i - 1]
        nextMeeting = nonOverlappingMeetings[i]

        if prevMeeting.finish < nextMeeting.start:
            chunks += 1

    return chunks


def createMeetings(meetings):
    objects = []
    for start, finish in meetings:
        objects.append(Meeting(start, finish))

    return objects


def mergeOverlappingMeetings(meetingsByStart):
    if len(meetingsByStart) == 0:
        return []

    stack = [meetingsByStart[0]]

    for i in range(1, len(meetingsByStart)):
        meeting = meetingsByStart[i]
        top = stack[-1]
        if top.overlap(meeting):
            top.merge(meeting)
        else:
            stack.append(meeting)

    return stack


def numberOfChunks(meetings):
    meetings = createMeetings(meetings)

    # sort by start time
    meetingsByStart = sorted(meetings, key=lambda meeting: meeting.start)

    nonOverlappingMeetings = mergeOverlappingMeetings(meetingsByStart)

    return _numberOfChunks(nonOverlappingMeetings)


class MyTestCase(unittest.TestCase):
    def test0(self):
        meetings = [(1, 2), (4, 5), (5, 6)]
        output = 1
        self.assertEqual(output, numberOfChunks(meetings))

    def test1(self):
        meetings = [(1, 3), (6, 7), (2, 9)]
        output = 0
        self.assertEqual(output, numberOfChunks(meetings))

    def test2(self):
        meetings = [(1, 3), (6, 7)]
        output = 1
        self.assertEqual(output, numberOfChunks(meetings))

    def test3(self):
        meetings = [(1, 3), (3, 5), (6, 7), (8, 9)]
        output = 2
        self.assertEqual(output, numberOfChunks(meetings))


if __name__ == '__main__':
    unittest.main()
