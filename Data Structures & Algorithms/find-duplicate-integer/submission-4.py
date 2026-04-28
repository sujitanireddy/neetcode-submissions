class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #Values as pointers and indexes as values the value with 2 or more pointers is the duplicate

        fast = 0
        slow = 0

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

