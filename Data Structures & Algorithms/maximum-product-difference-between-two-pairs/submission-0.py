class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        heapq.heapify(nums)
        
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        largest_value_1 = -1 * heapq.heappop(max_heap)
        largett_value_2 = -1 * heapq.heappop(max_heap)

        smallest_value_1 = heapq.heappop(nums)
        smallest_value_2 = heapq.heappop(nums)

        return (largest_value_1 * largett_value_2) - (smallest_value_1 * smallest_value_2)