"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
  0         1       2
[(0,30),(5,10),(15,20)]

0------------------------------30
        5----10
                    15---20


0 ------ 3
         3------6 
            5-----------10
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key = lambda x: x.start)

        for i in range(len(intervals)-1):

            if intervals[i].end > intervals[i+1].start:
                return False
        
        return True