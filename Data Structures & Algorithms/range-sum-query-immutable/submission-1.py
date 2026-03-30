class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = []
        sum = 0
        for num in nums:
            sum += num
            self.prefix_sums.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        left_prefix = self.prefix_sums[left - 1] if left > 0 else 0  
        right_prefix = self.prefix_sums[right]
        return right_prefix - left_prefix
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)