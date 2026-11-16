"""
- sort intervals and queires so that sequence comes in play


minHeap = [(dist, right_i)]


"""
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        i = 0
        intervals.sort()
        query_length = {}
        res = []
        minHeap = [] #(length,right)
        
        for q in sorted(set(queries)):

            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i] 
                heapq.heappush(minHeap, ((r - l) + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            query_length[q] = minHeap[0][0] if minHeap else -1
        
        for q in queries:
            res.append(query_length[q])
        
        return res
            

