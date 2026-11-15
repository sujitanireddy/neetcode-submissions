"""
Notes;
- Find the shortest length interval for each queri so that queir exists in that interval range 




min_heap = [1,2,3,6,7,8]

   i
[[1,3],[2,3],[3,7],[6,6]]



"""
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        query_length_map = defaultdict(int)
        i = 0
        intervals.sort()
        minHeap = []

        for q in sorted(set(queries)):

            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, ((r - l) + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            query_length_map[q] = minHeap[0][0] if minHeap else -1
        

        res = []
        for q in queries:
            res.append(query_length_map[q])
        
        return res