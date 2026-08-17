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

                          2,9,8,3,6 
(rob1,rob2,temp) (0,2,2) (2,9,9), 
          
          2 9 max()

          (i-2) (i-1) 

          rob1, rob2, temp = 0

          while i < len(arr):
            temp = (arr[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp

"""


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def dp(arr):
            rob1, rob2 = 0, 0

            for i in range(len(arr)):
                temp = max(arr[i] + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
            

        start = nums[1:]
        start_res = dp(start)

        end = nums[:-1]
        end_res = dp(end)

        return max(start_res, end_res)




