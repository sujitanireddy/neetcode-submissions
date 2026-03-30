class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_list = []
        for i in range(len(nums)):
            if nums[i] in distinct_list:
                return True
            distinct_list.append(nums[i])
        return False
