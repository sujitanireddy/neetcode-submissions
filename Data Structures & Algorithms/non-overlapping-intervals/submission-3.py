"""
[[1,2],[2,4],[1,4]]


[1,2], [1,4], [2,4]

1,4 2,4


end > start
+1
merge them

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        intervals.sort()

        for i in range(1, len(intervals)):

            #are the intervals merging?
            if intervals[i-1][1] > intervals[i][0]:
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
                res += 1
        
        return res