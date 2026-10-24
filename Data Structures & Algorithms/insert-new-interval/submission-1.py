"""
Notes:
- Sorted in ascending order
- Does not have any overlapping intervals

res = []

Does this new interval go at the front? 
    if intervals[i][0] > newInterval[1]:
        res.append(newInterval)
        return res + intervals[i:]

Does this new interval got at the back?
    elif newInterval[0] > intervals[i][1]:
        res.append(intervals[i])

Does this new interval merger with any exisiting intervals?
    else:
        newInterval = [min(starting), max(ending)]

"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):

            #does this newInterval come before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            #does this newInterval come after
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            #intervals are merging
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        
        res.append(newInterval)

        return res






















