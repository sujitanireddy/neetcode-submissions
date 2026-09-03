"""
n + 1
n = 5

1,2,3,4,5]

 nodes         0 1 2 3 4
 pointers     [1,2,3,2,2]

     S    F
0 -> 1 -> 2 <-> 3
          ^  
          |
          4

use fast and slow pointer to collide and from the collion point to the vertex of the cycle from the start of the linked list the distance is the same. 
Using this we can find the duplicate number
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0

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

