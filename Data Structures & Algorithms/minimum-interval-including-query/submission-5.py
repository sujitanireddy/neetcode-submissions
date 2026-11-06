"""
Notes:
   
[[1,3],[2,3],[3,7],[6,6]]

   3     2     5     1

  
[2,3,1,7,6,8]

 2,2,

[2,2,3,5,1,-1]


1 <= 2 <= 3 = 2

BruteForce:
TC: O(n**2)

Algorithm:
- 
"""


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        query_length_map = {}
        intervals.sort()
        minHeap = []
        res = []
        i = 0

        for q in sorted(set(queries)):

            while i < len(intervals) and intervals[i][0] <= q:
                l , r = intervals[i]
                length = (r - l) + 1
                heapq.heappush(minHeap, (length, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            query_length_map[q] = minHeap[0][0] if minHeap else -1
        
        for q in queries:
            res.append(query_length_map[q])

        return res









