"""
[(0,30),(5,10),(15,20)]

0 ----------------------------------------------30
      5 --------10   15 ---------20

Sort the initial array so they are in order

if intervals[i-1].end > intervals[i].start:
    return False

"""


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):

            if intervals[i-1].end > intervals[i].start:

                return False

        return True