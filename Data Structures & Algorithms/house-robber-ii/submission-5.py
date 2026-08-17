"""
Note: 0th index and last index are nei.
- What is the max that can be robbed if position i is robbed

2,9,8,3,6

2 + 8 = 10
9 + 3 = 12
9 + 6 = 15
8 + 6 = 14

start = [1:]
end = [:-1]

if n starts at 0: Have to skip last idx
f(n) = max(nums[n] + f(n+2), f(n+1))

if last idx is there, skip 0th idx

BrueForce Recursive:
TC: O(2**n)
SC: O(h) where h is the height of the recursive tree

TopDown Memoization:
TC: O(n)
SC: O(n)

BottomUP (DP):


nums = []




"""


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def recurse(i,arr):

            if i >= len(arr):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(arr[i] + recurse(i+2, arr), recurse(i+1, arr))

            return cache[i]

        start = nums[1:]
        cache = {}
        start_res = recurse(0,start)

        end = nums[:-1]
        cache = {}
        end_res = recurse(0,end)

        return max(start_res, end_res)




