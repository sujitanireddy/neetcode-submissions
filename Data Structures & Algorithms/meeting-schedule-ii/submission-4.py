"""
0--------------------------------------40 (1)
     5---------10
        6---8                         
                    15---------20         (2)

sort(): O(nlogn)

start_arr: start time of meetings
end_arr: end time of meetings
         
                s
start: [0,5,15]
           e
end:   [10,20,40]

rooms = 2

if start[s] < end[e]:
    room += 1
    s += 1
else:
    rooms -= 1
    e += 1

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
        s,e = 0,0
        rooms = 0
        counter = 0

        while s < len(intervals):

            if start[s] < end[e]:
                counter += 1
                s += 1
            
            else:
                counter -= 1
                e += 1
            
            rooms = max(rooms, counter)
        
        return rooms
        