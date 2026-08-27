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

Top Down: Tabulation DP
TC: O(n)
SC: O(n)

   r2r1 t
 9 9 13
[9 8 3 6]

temp = max(arr[i] + r2, r1)
r2 = r1
r1 = temp

[2 9 8 3]
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(arr):

            r1, r2, i = 0, 0, 0
            
            while i < len(arr):
                temp = max(arr[i] + r2, r1)
                r2 = r1
                r1 = temp
                i += 1
            
            return r1
            
        n = len(nums)
        arr_without_first = nums[1:]
        arr_without_last  = nums[:n-1]

        res1 = helper(arr_without_first)
        res2 = helper(arr_without_last)

        return max(res1, res2, nums[0])


