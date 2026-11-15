"""

[(0,40),(5,10),(15,20)]

0--------------------------------40
        5-------10  15-----20

    s
0   8

e
8   10

        s
[0,5,15]

    e
[10,20,40]

conditions:

start[s] < end[e]:
    rooms += 1
    s += 1

else:
    rooms -= 1
    e += 1

2

"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s = e = max_rooms = curr_rooms = 0

        while s < len(intervals):

            if start[s] < end[e]:
                curr_rooms += 1
                s += 1
            
            else:
                curr_rooms -= 1
                e += 1
            
            max_rooms = max(max_rooms, curr_rooms)
        
        return max_rooms





















