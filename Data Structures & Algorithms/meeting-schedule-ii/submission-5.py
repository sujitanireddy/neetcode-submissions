"""
early return case: if not intervals: return 0
sort the start and end arrays.

[(0,40),(5,10),(15,20)]

0--------------------------------------------40
               10----------17
    5----------10    15--------20

running_counter = 0
max_so_far = 2
         
                s
start = [0,5,15]
                e
end   = [10,20,40]


condition: if start[s] < end[e]:
                  s+= 1
                  rooms_required += 1
           else:
                  e+= 1
                  rooms_required -= 1
        
TC: O(nlogn)
SC: O(n)

0--------------------------------------------40
               10----------17
    5----------10    15--------20


0  5  10 15
10 17 20 40

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

        s, e = 0, 0
        rooms_required = 0
        res = 0

        while s < len(intervals):

            if start[s] < end[e]:
                s+=1
                rooms_required += 1
            
            else:
                e+=1
                rooms_required -= 1
            
            res = max(res, rooms_required)

        return res



















