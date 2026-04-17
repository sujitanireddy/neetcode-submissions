class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #len(nums) = n + 1 
        #range = [1....n]
        #consider the values of nums as pointers and indexes as values. We need to detect the cycle head which is the duplicate


        fast, slow = 0, 0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow_2 = 0
        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            if slow == slow_2:
                return slow
