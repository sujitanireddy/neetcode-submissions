"""
Notes:
- Cannot rob two adj houses

              1      1
            3       3

Recursion (BruteForce)

Basecase: if n >= len(nums)
f(n) = max(nums[n] + f(n+2), f(n+1))

 0 1 2 3 4
[2,9,8,3,6]

          n = 0: max(2 + f(2), f(1))
          n = 2: max(8 + 6, f(3))

TC: O(2**n)
SC: O(h)

Top Down : Memoize

Map to store out compute and recuse it.
TC: O(n)
SC: O(n)

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}

        def recurse(n):

            if n >= len(nums):
                return 0
            
            if n in cache:
                return cache[n]
            
            cache[n] = max(nums[n] + recurse(n+2), recurse(n+1))

            return cache[n]
        
        return recurse(0)