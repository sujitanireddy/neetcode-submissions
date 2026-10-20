"""
[1,2] [1,4] [2,4]

1   4   2   4

- 2 > 1

[[1,100],[11,22],[1,11],[2,12]]

        i
  0     1     2
[1,2],[1,2],[1,2]

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        res = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(end, prev_end)

        return res
            