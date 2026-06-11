class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-n for n in nums]

        heapq.heapify(nums)

        for i in range(k):
            value =heapq.heappop(nums)
        
        return -1 * value