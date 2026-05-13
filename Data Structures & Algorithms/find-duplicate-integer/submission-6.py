class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #BruteForce: Using hashset {1,2,3}. TC: O(n), SC: O(n)
        
        #Linkedlist
        #indexes are values.  0 -> 1 -> 2 <-> 3  4
        #values are pointers

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
                return slow
