class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_arr = []
        
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            self.prefix_arr.append(running_sum)
        
        print(self.prefix_arr)

    def sumRange(self, left: int, right: int) -> int:
        return (self.prefix_arr[right] - self.prefix_arr[left - 1]) if left > 0 else self.prefix_arr[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)