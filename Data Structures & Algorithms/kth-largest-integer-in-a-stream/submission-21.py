"""
3 [1,2,3,3]

[1,2,3,3,3,5,6,]

max element out with a window of 3

min_heap = [2,3,3,3]

"""
class KthLargest:

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
        

        


        
