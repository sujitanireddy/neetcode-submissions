"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
[(0,40),(5,10),(15,20)]

      s   
[0,5,15]

    e
[10,20,40]




"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = e = 0
        res = 0
        rooms = 0

        while s < len(start):

            if start[s] < end[e]:
                s += 1
                rooms += 1
            
            else:
                e += 1
                rooms -= 1 
            
            res = max(res, rooms)
    
        return res