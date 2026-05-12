class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
              
    #values 0 1 2 3 4
  #pointers[1,2,3,2,2]

    #Find the start of the cycle. Floy'ds tortise and hare algoritm.
    
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
            slow = nums[slow]
            if slow_2 == slow:
                return slow_2
        
        



