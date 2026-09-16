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

"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}

        def recurse(i):
            
            if i in cache:
                return cache[i]
            
            if i >= len(nums):
                return 0
            
            cache[i] = max(nums[i] + recurse(i+2), recurse(i+1))

            return cache[i]
        
        recurse(0)

        return cache[0]



























        