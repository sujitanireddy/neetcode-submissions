class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-n for n in nums]
        heapq.heapify(nums)

        i = 0
        while i < k:
            kth_largest = heapq.heappop(nums)
            i += 1

        return  -1 * kth_largest