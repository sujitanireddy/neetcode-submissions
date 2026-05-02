import heapq

class KthLargest:

    #3 [4,5,8,2]

    #[3,5,6] # O(nlogn)

    #heap(min) = (pop() = logn)
    
    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:

        heapq.heappush(self.nums, val)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]

        
