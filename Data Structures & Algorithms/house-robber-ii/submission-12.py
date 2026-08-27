"""
0 1 2 3 4
2,9,8,3,6 
                      0 1 2 3
arr_withtout_first = [9 8 3 6]
arr_without_last =   [2 9 8 3]

basecase: if i >= len(nums): return 0
f(i) = max(nums[i] + f(i+2), f(i+1))
               9   +   f(2),   f(1)
                         |
                         8  + f(3), f(2)
                               |
                               6 + f(5), f(6)
Brute Force:
TC: O(2 ** n)
SC: O(n)

Top Down: Memoize
TC: O(n)
SC: O(n)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        def recurse(i, arr):
            
            if i in cache:
                return cache[i]
            
            if i >= len(arr):
                return 0
            
            cache[i] = max(arr[i] + recurse(i+2,arr), recurse(i+1,arr))

            return cache[i]

        n = len(nums)
        arr_without_first = nums[1:]
        arr_without_last  = nums[:n-1]

        cache = {}
        res1 = recurse(0,arr_without_first)

        cache = {}
        res2 = recurse(0,arr_without_last)

        return max(res1, res2, nums[0])


