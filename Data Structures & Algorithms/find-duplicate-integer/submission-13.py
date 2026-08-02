class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        """     
        0 1 2 3 4
        1 2 3 2 2
        """

        slow = 0
        fast = 0

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
                return slow_2
