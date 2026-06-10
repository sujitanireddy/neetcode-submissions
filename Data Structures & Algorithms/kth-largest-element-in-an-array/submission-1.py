class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-s for s in nums]
        
        heapq.heapify(nums)

        counter = 0
        while k > counter:
            output = heapq.heappop(nums)
            counter += 1

        return -1 * output
