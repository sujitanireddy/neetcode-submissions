"""
nums = [2,3,1,5,4], k = 2

1,2,3,4,5

[2,3,1,1,5,5,4], k = 3

1,1,2,3,4,5,5
maxHeap = [-1,-2,-3,]

0

TC: n * logn
SC: O(n)

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = []

        for num in nums:
            heapq.heappush(maxHeap, -1 * num)
        
        while k > 0:
            val = heapq.heappop(maxHeap)
            k -= 1
        
        return -1 * val