"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

Notes:
- start < end
      
      15.....20
    5....10
0..............30

5....8 9....15

sort

previous meeting end time > next meeting start time: conflict
    i-1    i
[(0,30),(5,10),(15,20)]

  i-1    i
[(5,8),(9,15)]

         i-1    i  
[(0,3),(3,6),(5,10),]

"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):

            if intervals[i-1].end > intervals[i].start:
                return False
        
        return True

