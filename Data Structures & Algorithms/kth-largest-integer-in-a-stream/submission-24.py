"""

["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

2,3,3

min_heap

TC: O(klogn) O(n) for hepify
SC: O(k)
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
