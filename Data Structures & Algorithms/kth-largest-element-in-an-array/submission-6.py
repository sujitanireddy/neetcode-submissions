class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        """ 
        Hepify(nums)
        pop k times
        """
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for i in range(k):
            kth_largest = -1 * heapq.heappop(nums)
        return kth_largest