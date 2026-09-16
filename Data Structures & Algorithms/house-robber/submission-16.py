"""
 0 1 2 3
[1,1,3,3]

f(n) = max(nums[i] + f(i+2), f(i+1))
                3
f(0) = max(1 + f(2), f(1))
 
                |       max(1 + 3, 3)
                                3,
                max(3 + f(4), f(3))
                         0      |

                                max(3 + f(5), f(4))
                                          0     0

Base case:
- if i >= len(nums):
        return 0

Brute Force:
 - O(2**n)
 - O(n)

Top down memoization:
- O(n)
- O(n)

True Dp solution:
- O(n)
- O(1)


  r1
     r2
         t 
1, 1, 3, 3

temp = nums[i] + r1
r1 = r2
r2 = temp


   t
r2
1  2  3 1

r2 = 1 


"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0 

        for i in range(len(nums)):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2



























        