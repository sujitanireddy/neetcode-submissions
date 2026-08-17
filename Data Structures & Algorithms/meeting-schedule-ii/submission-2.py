"""
Notes:
- if not intervals: return 0
- position where both start and end time are equal- priorotize end time

(0,40),(5,10),(15,20)            

0--------------------------------------40
     5---------10
               10-------20

rooms_required = 0

sorted arrays:

                 s
start = [0,5,10]

            e
end   = [10,20,40]


while s < len(start):
    if start[s] > end[e]:
        counter += 1
        s += 1
    else:
        counter -= 1
        e += 1
    save the max here

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
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0,0
        counter, res = 0,0

        while s < len(start): 

            if start[s] < end[e]:
                counter += 1
                s += 1
            else:
                counter -= 1
                e += 1
            res = max(res, counter)
        return res
