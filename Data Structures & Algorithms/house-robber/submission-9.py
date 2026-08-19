"""
0 1 2 3
1,1,3,3

2 9 8 3 6

recurrence relation:
f(i) = max(nums[i] + f(i+2), f(i+1))

                f(0) = max(1 + f(2), f(1)) -> max(1 + f(3), f(2))
                                 |
                                max(3 + f(4), f(3))
                                                |
                                               max(3 + f(5), f(4))
TC: O(2**n)
SC: O(h)

if i >= len(nums): return 0
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

        return recurse(0)
            