class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        fast = 0
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break
        
        slow_2 = 0
        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]

            if slow == slow_2:
                return slow

