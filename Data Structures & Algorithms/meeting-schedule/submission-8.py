"""
          i
[(0,30),(5,10),(15,20)]

30

        5......10    15....20
0...................................30

          i
[(5,8),(9,15)]

nlogn

5.......8 9.......15

if not intervals: return True
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

        if not intervals:
            return True

        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True



















