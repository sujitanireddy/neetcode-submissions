class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while k < len(self.nums):
            heapq.heappop(self.nums)


    def add(self, val: int) -> int:
        
        heapq.heappush(self.nums, val)
        
        while self.k < len(self.nums):
            heapq.heappop(self.nums)

        return self.nums[0]
