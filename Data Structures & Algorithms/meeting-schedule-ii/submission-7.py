"""
early return: if not intervals: return 0

0----                           40
     5------10   15------20

sort the input array
                 s               
start_arr = [0,5,15]

             e   
end_arr =   [40,10,20]


if s < e:
    roooms += 1
    s += 1

else:
    rooms -= 1
    e += 1

TC: O(nlogn)
SC: O(n)

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

        n = len(intervals)
        start = []
        end = []

        for i in range(n):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        
        start.sort()
        end.sort()
        
        s = 0
        e = 0
        rooms = 0
        curr = 0

        while s < n:

            if start[s] < end[e]:
                curr += 1
                s += 1
            
            else:
                curr -= 1
                e += 1
            
            rooms = max(rooms, curr)
        
        return rooms

"""

1----5
     5------10
            10------15
                    15------20

  s
1,5,10,15

  e
5,10,15,20

"""

        









































