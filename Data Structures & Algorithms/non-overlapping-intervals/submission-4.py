class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        res = 0

        for i in range(len(intervals) - 1):

            #are the intervals conflicting?
            if intervals[i][1] > intervals[i+1][0]:
                intervals[i+1][1] = min(intervals[i][1], intervals[i+1][1])
                res += 1
        
        return res
