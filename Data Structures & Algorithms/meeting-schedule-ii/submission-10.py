"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
res = 1
if not intervals:
    return res

intervals.sort(key = lambda x: x.start)

                        2
[(0,40),(5,10),(15,20)]

0-----------------------------40
    5-----10    15-----20

s
0   5   15

e
10  20  40



if end > start:
    res += 1


[(1,5),(2,6),(3,7),(4,8),(5,9)]

         s
[1,2,3,4,5]

   e   
[5,6,7,8,9]

4

if e > s:
    s+= 1
    rooms += 1

else:
    e += 1
    rooms -= 1

"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        rooms = 0
        res = 0
        s = 0
        e = 0

        while s < len(start):

            if end[e] > start[s]:
                rooms += 1
                s += 1
            
            else:
                rooms -= 1
                e += 1
            
            res = max(res, rooms)
        
        return res



        

