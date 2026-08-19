"""
0 1 2 3
1,1,3,3
          
        rob2 rob1  temp
          2   9    8    3   6 
          2   9    10

rob1 = rob2
rob2 = temp

recurrence relation:
f(i) = max(nums[i] + f(i+2), f(i+1))

                f(0) = max(1 + f(2), f(1)) -> max(1 + f(3), f(2))
                                 |
                                max(3 + f(4), f(3))
                                                |

Brute Force Recursion                                               max(3 + f(5), f(4))
TC: O(2**n)
SC: O(h)

Top Down Memoization
TC: O(n)
SC: O(n)

Bottom up: iterative DP
TC: O(n)
SC: O(1)

if i >= len(nums): return 0
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob2, rob1)
            rob2 = rob1
            rob1 = temp
        
        return rob1
            
        
        
            