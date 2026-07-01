class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        """
         0,1,2,3,4 (values)
        [1,2,3,2,2] (pointers)

        0 -> 1 -> 2 <-> 3 

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
            slow_2 = nums[slow_2]
            fast = nums[fast]

            if slow_2 == fast:
                return slow_2